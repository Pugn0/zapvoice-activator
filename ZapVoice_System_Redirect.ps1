# 1. Solicitar privilégios de Administrador
$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
if (-not $currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Start-Process powershell.exe -Verb RunAs -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`""
    exit
}

function Show-Error($msg) {
    Write-Host "`n[ERRO] $msg" -ForegroundColor Red
    Write-Host "Pressione qualquer tecla para sair..."
    $null = [Console]::ReadKey($true)
    exit
}

# 2. Configurações de Redirecionamento
$OldHost = "api.zapvoice.com.br"
$NewHost = "zapmod.shop"
$HostsPath = "$env:SystemRoot\System32\drivers\etc\hosts"
$AppGuid = "{$(New-Guid)}"

Write-Host "`n--- ZapVoice System Redirector v6.1 (Multi-Method Support) ---" -ForegroundColor Cyan

# 3. Limpar o arquivo HOSTS e configurações antigas
Write-Host "Configurando interceptacao de rede..." -ForegroundColor Yellow
$content = Get-Content $HostsPath | Where-Object { $_ -notmatch $OldHost }
$content += "127.0.0.1 $OldHost # ZapVoice System Redirect"
$content | Out-File $HostsPath -Encoding UTF8 -Force
ipconfig /flushdns | Out-Null

# 4. Gerar e Vincular Certificado SSL à Porta 443
Write-Host "Configurando Certificado SSL e Porta 443..." -ForegroundColor Yellow
$cert = Get-ChildItem Cert:\LocalMachine\My | Where-Object { $_.Subject -like "*$OldHost*" }
if (-not $cert) {
    $cert = New-SelfSignedCertificate -DnsName $OldHost -CertStoreLocation Cert:\LocalMachine\My -NotAfter (Get-Date).AddYears(10)
    $store = New-Object System.Security.Cryptography.X509Certificates.X509Store("Root", "LocalMachine")
    $store.Open("ReadWrite")
    $store.Add($cert)
    $store.Close()
}

# Remover vinculação antiga (se houver) e adicionar a nova
netsh http delete sslcert ipport=0.0.0.0:443 2>$null
netsh http add sslcert ipport=0.0.0.0:443 certhash=$($cert.Thumbprint) appid=$AppGuid | Out-Null
Write-Host "[OK] Porta 443 vinculada ao certificado SSL." -ForegroundColor Green

# 5. Iniciar o Motor de Redirecionamento (.NET)
Write-Host "`nRedirecionando: $OldHost -> $NewHost" -ForegroundColor Cyan
Write-Host "MANTENHA ESTA JANELA ABERTA PARA O REDIRECIONAMENTO FUNCIONAR." -ForegroundColor White -BackgroundColor DarkBlue
Write-Host "Pressione CTRL+C para encerrar.`n" -ForegroundColor Gray

$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("https://$OldHost/")

try {
    $listener.Start()
    while ($listener.IsListening) {
        $context = $listener.GetContext()
        $req = $context.Request
        $res = $context.Response

        if ($req.Url.Host -eq $OldHost) {
            $targetUrl = "https://$NewHost" + $req.RawUrl
            Write-Host "[REDIRECT] $($req.HttpMethod) -> $targetUrl" -ForegroundColor White

            try {
                [System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true}
                $webRequest = [System.Net.HttpWebRequest]::Create($targetUrl)
                $webRequest.Method = $req.HttpMethod
                
                # Copiar Headers essenciais
                foreach ($h in $req.Headers.AllKeys) {
                    if ($h -notin @("Host", "Connection", "Content-Length", "Accept-Encoding")) {
                        try { $webRequest.Headers.Add($h, $req.Headers[$h]) } catch {}
                    }
                }

                # Se houver corpo na requisição (POST/PUT/etc)
                if ($req.HasEntityBody) {
                    $reqStream = $req.InputStream
                    $webStream = $webRequest.GetRequestStream()
                    $reqStream.CopyTo($webStream)
                    $webStream.Close()
                }

                # Obter resposta do servidor de destino
                $webResponse = $webRequest.GetResponse()
                $res.StatusCode = [int]$webResponse.StatusCode
                
                # Copiar headers de resposta (exceto os que o .NET gerencia automaticamente)
                foreach ($h in $webResponse.Headers.AllKeys) {
                    if ($h -notin @("Transfer-Encoding", "Content-Length")) {
                        try { $res.Headers.Add($h, $webResponse.Headers[$h]) } catch {}
                    }
                }

                $respStream = $webResponse.GetResponseStream()
                $respStream.CopyTo($res.OutputStream)
                $webResponse.Close()
            } catch {
                # Tratar erros HTTP (404, 405, 500, etc)
                if ($_.Exception.InnerException -is [System.Net.WebException]) {
                    $webEx = $_.Exception.InnerException
                    if ($webEx.Response) {
                        $errResp = $webEx.Response
                        $res.StatusCode = [int]$errResp.StatusCode
                        $errResp.GetResponseStream().CopyTo($res.OutputStream)
                        $errResp.Close()
                    } else {
                        $res.StatusCode = 502
                    }
                } else {
                    $res.StatusCode = 502
                    $errMsg = [System.Text.Encoding]::UTF8.GetBytes("Erro no redirecionamento: $($_.Exception.Message)")
                    $res.OutputStream.Write($errMsg, 0, $errMsg.Length)
                }
            }
        }
        $res.Close()
    }
} catch {
    Show-Error "Erro ao iniciar o servidor: $($_.Exception.Message)"
} finally {
    $listener.Stop()
    netsh http delete sslcert ipport=0.0.0.0:443 2>$null
}
