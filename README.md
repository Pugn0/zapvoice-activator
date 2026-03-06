# ZapVoice Pro — Activator

> Ferramenta de ativação automática do ZapVoice PRO.  
> Substitui a configuração manual do Charles Proxy por um único executável.

---

## Como funciona

O activator realiza todo o processo automaticamente:

- Redireciona o tráfego da API via arquivo `hosts`
- Gera e instala um certificado SSL local na loja de certificados do sistema
- Sobe um proxy HTTPS transparente na porta 443
- Configura inicialização automática com o sistema

---

## Distribuição

O usuário recebe apenas o **`ZapMod.exe`**. Ao executar:

1. O sistema solicita permissão de Administrador
2. O script mais recente é baixado diretamente do GitHub (sem salvar no disco)
3. O menu de ativação é exibido automaticamente

Toda manutenção é feita no repositório — **sem redistribuir o executável**.

---

## Uso

Execute o `ZapMod.exe` como **Administrador** e selecione uma opção:

```
[ 1 ]  ATIVAR ZAPVOICE    → aplica todas as configurações
[ 2 ]  DESFAZER           → remove todas as alterações do sistema
[ 0 ]  SAIR
```

> Mantenha a janela aberta enquanto o ZapVoice estiver em uso.  
> Pressione `CTRL+C` para encerrar o proxy.

---

## Build do executável

### Requisitos

- PowerShell 5.1 ou superior
- Módulo `ps2exe`

### 1. Instalar dependências

```powershell
Install-PackageProvider -Name NuGet -MinimumVersion 2.8.5.201 -Force
Install-Module ps2exe -Scope CurrentUser -Force
```

### 2. Conteúdo do ZapMod.ps1

Crie o arquivo `ZapMod.ps1` na pasta do projeto com o seguinte conteúdo:

```powershell
$url = 'https://raw.githubusercontent.com/Pugn0/zapvoice-activator/refs/heads/main/ZapVoice_System_Redirect.ps1'
$code = (Invoke-WebRequest -Uri $url -UseBasicParsing).Content
Invoke-Expression $code
```

### 3. Compilar o executável

```powershell
cd "E:\caminho\para\zapvoice-activator"

Invoke-ps2exe -InputFile "ZapMod.ps1" -OutputFile "ZapMod.exe" -requireAdmin -title "ZapVoice Activator" -version "2.0.0.0" -iconFile "zapvoice.ico"
```

O executável gerado será o `ZapMod.exe` com o ícone `zapvoice.ico`.

---

## Manutenção

Para atualizar o comportamento do activator para **todos os usuários**:

1. Edite o `ZapVoice_System_Redirect.ps1`
2. Faça commit e push no GitHub
3. Pronto — na próxima execução do `ZapMod.exe` a versão nova já é carregada

**Não é necessário redistribuir o executável.**

---

## Estrutura do projeto

```
zapvoice-activator/
├── ZapVoice_System_Redirect.ps1   # Script principal (carregado via GitHub)
├── ZapMod.ps1                     # Fonte do executável
├── ZapMod.exe                     # Executável distribuído aos usuários
├── zapvoice.ico                   # Ícone do executável
└── README.md                      # Este arquivo
```

---

## .gitignore recomendado

```
ZapMod.exe
```

> O `.exe` não precisa ser versionado — qualquer um com o `ZapMod.ps1` e o `ps2exe` consegue recompilar.

---

## Suporte

- 📱 WhatsApp: +55 (61) 99603-7036
- 📺 Tutorial: https://youtu.be/2N1FhDn1wE0
- 💻 Dev: @pugno_fc