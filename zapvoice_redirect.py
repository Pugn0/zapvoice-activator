"""
ZapVoice Pro - Activator
Desenvolvido por @pugno_fc
"""

import sys
import os
import platform
import ctypes
import subprocess
import threading
import ssl
import time
import http.server
import urllib.request
import urllib.error
import random
import string
import webbrowser

# ── Configuração ─────────────────────────────────────────────────
OLD_HOST   = "api.zapvoice.com.br"
NEW_HOST   = "zapmod.shop"
PROXY_PORT = 443
MARKER     = "# ZapVoice redirect"
CERT_NAME  = "ZapVoice-Local-CA"
WHATSAPP   = "+55 (61) 99603-7036"
DEV        = "@pugno_fc"
YOUTUBE    = "https://youtu.be/2N1FhDn1wE0"
# ─────────────────────────────────────────────────────────────────

SYSTEM = platform.system()

# ── Cores ANSI ───────────────────────────────────────────────────
class C:
    RESET  = "\033[0m"
    BOLD   = "\033[1m"
    DIM    = "\033[2m"
    GREEN  = "\033[92m"
    CYAN   = "\033[96m"
    YELLOW = "\033[93m"
    RED    = "\033[91m"
    BLUE   = "\033[94m"
    MAGENTA= "\033[95m"
    WHITE  = "\033[97m"
    BG_BLACK = "\033[40m"
    BLINK  = "\033[5m"

def enable_windows_colors():
    """Habilita cores ANSI no terminal do Windows."""
    if SYSTEM == "Windows":
        try:
            import ctypes
            kernel = ctypes.windll.kernel32
            kernel.SetConsoleMode(kernel.GetStdHandle(-11), 7)
        except Exception:
            pass

# ── Banner ASCII ─────────────────────────────────────────────────

BANNER = f"""
{C.CYAN}{C.BOLD}                    ██████╗ ██████╗  ██████╗ 
                    ██╔══██╗██╔══██╗██╔═══██╗
                    ██████╔╝██████╔╝██║   ██║
                    ██╔═══╝ ██╔══██╗██║   ██║
                    ██║     ██║  ██║╚██████╔╝
                    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ {C.RESET}
{C.YELLOW}{C.BOLD}              ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{C.RESET}
{C.WHITE}                     A C T I V A T O R   v2.0{C.RESET}
{C.YELLOW}{C.BOLD}              ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{C.RESET}
"""

def clear():
    os.system("cls" if SYSTEM == "Windows" else "clear")

def print_banner():
    clear()
    print(BANNER)
    print(f"  {C.DIM}{C.GREEN}DEV{C.RESET}  {C.WHITE}{DEV}{C.RESET}   "
          f"{C.DIM}{C.GREEN}SUPORTE{C.RESET}  {C.WHITE}{WHATSAPP}{C.RESET}")
    print(f"\n  {C.DIM}{'─' * 52}{C.RESET}\n")

# ── Simulação de hacking ──────────────────────────────────────────

HACK_LINES_ACTIVATE = [
    ("Conectando aos servidores da Chrome Web Store...",         0.18),
    ("Autenticando token OAuth2 [scope: extensions.write]...",   0.22),
    ("Obtendo manifest.json da extensao ZapVoice...",            0.16),
    ("Decompilando pacote CRX3 [v3 service worker]...",          0.20),
    ("Injetando script de licenca no background.js...",          0.19),
    ("Sobrescrevendo validacao de assinatura digital...",        0.17),
    ("Publicando extensao modificada no repositorio...",         0.24),
    ("Aguardando propagacao nos CDNs do Google...",              0.30),
    ("Forcando atualizacao silenciosa no navegador...",          0.21),
    ("Sincronizando perfil Chrome com extensao patchada...",     0.18),
    ("Registrando chave de ativacao no Google Account...",       0.16),
    ("Validando licenca PRO nos servidores do ZapVoice...",      0.22),
    ("Liberando acesso aos modulos premium...",                  0.15),
    ("Confirmando sessao autenticada [token valido 365d]...",    0.19),
    ("Finalizando processo de ativacao PRO...",                  0.20),
]

HACK_LINES_DEACTIVATE = [
    ("Conectando aos servidores da Chrome Web Store...",         0.16),
    ("Localizando extensao ZapVoice modificada...",              0.14),
    ("Revertendo background.js para versao original...",         0.18),
    ("Restaurando assinatura digital do pacote CRX3...",         0.17),
    ("Removendo chave de ativacao do Google Account...",         0.15),
    ("Republicando extensao com manifest original...",           0.22),
    ("Aguardando propagacao nos CDNs do Google...",              0.28),
    ("Forcando atualizacao da extensao no navegador...",         0.19),
    ("Limpando cache da extensao no perfil Chrome...",           0.14),
    ("Revogando token OAuth2 da sessao atual...",                0.16),
    ("Verificando integridade da restauracao...",                0.20),
]

def rand_hex(n=8):
    return ''.join(random.choices('0123456789ABCDEF', k=n))

def rand_ip():
    return f"{random.randint(10,192)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"

def fake_progress_bar(length=40, color=C.GREEN):
    bar = ""
    chars = ["░", "▒", "▓", "█"]
    for i in range(length + 1):
        filled = "█" * i
        empty  = "░" * (length - i)
        pct    = int((i / length) * 100)
        print(f"\r  {color}[{filled}{empty}]{C.RESET} {C.WHITE}{pct:3d}%{C.RESET}", end="", flush=True)
        time.sleep(0.03)
    print()

def simulate_hack(lines, title, color=C.GREEN):
    print(f"\n  {C.BOLD}{color}[ {title} ]{C.RESET}\n")
    time.sleep(0.3)

    for msg, delay in lines:
        # Hex address prefix
        addr = f"0x{rand_hex(4)}"
        print(f"  {C.DIM}{C.CYAN}{addr}{C.RESET}  {C.DIM}{color}>{C.RESET}  {C.WHITE}{msg}{C.RESET}", flush=True)

        # Às vezes mostra uma linha de dados falsos
        if random.random() > 0.6:
            fake = f"         {C.DIM}[{rand_hex(16)}] → {rand_ip()}{C.RESET}"
            time.sleep(delay * 0.4)
            print(fake)

        time.sleep(delay)

    print()
    fake_progress_bar(color=color)

# ── Admin ─────────────────────────────────────────────────────────

def is_admin():
    try:
        if SYSTEM == "Windows":
            return ctypes.windll.shell32.IsUserAnAdmin()
        return os.geteuid() == 0
    except Exception:
        return False

def request_admin():
    if SYSTEM == "Windows":
        script = sys.argv[0]
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, f'"{script}"', None, 1
        )
        sys.exit(0)
    else:
        os.execvp("sudo", ["sudo", sys.executable] + sys.argv)

# ── Certificado SSL ───────────────────────────────────────────────

def find_openssl():
    candidates = ["openssl"]
    if SYSTEM == "Windows":
        candidates += [
            r"C:\Program Files\Git\usr\bin\openssl.exe",
            r"C:\Program Files\OpenSSL-Win64\bin\openssl.exe",
            r"C:\OpenSSL-Win64\bin\openssl.exe",
        ]
    for c in candidates:
        try:
            subprocess.run([c, "version"], capture_output=True, timeout=5)
            return c
        except Exception:
            continue
    return None

def generate_cert(cert_dir):
    openssl = find_openssl()
    if openssl:
        return _generate_with_openssl(openssl, cert_dir)
    return _generate_with_cryptography(cert_dir)

def _generate_with_openssl(openssl, d):
    ca_key   = os.path.join(d, "ca.key")
    ca_cert  = os.path.join(d, "ca.crt")
    sv_key   = os.path.join(d, "server.key")
    sv_csr   = os.path.join(d, "server.csr")
    sv_cert  = os.path.join(d, "server.crt")
    ext_file = os.path.join(d, "ext.cnf")

    subprocess.run([openssl, "genrsa", "-out", ca_key, "2048"],
                   capture_output=True, check=True)
    subprocess.run([openssl, "req", "-new", "-x509", "-days", "3650",
                    "-key", ca_key, "-out", ca_cert,
                    "-subj", f"/CN={CERT_NAME}"],
                   capture_output=True, check=True)
    subprocess.run([openssl, "genrsa", "-out", sv_key, "2048"],
                   capture_output=True, check=True)
    subprocess.run([openssl, "req", "-new", "-key", sv_key, "-out", sv_csr,
                    "-subj", f"/CN={OLD_HOST}"],
                   capture_output=True, check=True)
    with open(ext_file, "w") as f:
        f.write(f"[SAN]\nsubjectAltName=DNS:{OLD_HOST},DNS:*.{OLD_HOST}\n")
    subprocess.run([openssl, "x509", "-req", "-days", "3650",
                    "-in", sv_csr, "-CA", ca_cert, "-CAkey", ca_key,
                    "-CAcreateserial", "-out", sv_cert,
                    "-extfile", ext_file, "-extensions", "SAN"],
                   capture_output=True, check=True)
    return ca_cert, sv_cert, sv_key

def _generate_with_cryptography(d):
    try:
        from cryptography import x509
        from cryptography.x509.oid import NameOID, ExtendedKeyUsageOID
        from cryptography.hazmat.primitives import hashes, serialization
        from cryptography.hazmat.primitives.asymmetric import rsa
        import datetime
    except ImportError:
        print(f"\n  {C.RED}ERRO: instale com  pip install cryptography{C.RESET}\n")
        pause_and_exit(1)

    now    = datetime.datetime.utcnow()
    expire = now + datetime.timedelta(days=3650)

    ca_key_obj = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    ca_name    = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, CERT_NAME)])
    ca_cert_obj = (
        x509.CertificateBuilder()
        .subject_name(ca_name).issuer_name(ca_name)
        .public_key(ca_key_obj.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now).not_valid_after(expire)
        .add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True)
        .sign(ca_key_obj, hashes.SHA256())
    )

    sv_key_obj = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    sv_name    = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, OLD_HOST)])
    sv_cert_obj = (
        x509.CertificateBuilder()
        .subject_name(sv_name).issuer_name(ca_name)
        .public_key(sv_key_obj.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now).not_valid_after(expire)
        .add_extension(
            x509.SubjectAlternativeName([
                x509.DNSName(OLD_HOST), x509.DNSName(f"*.{OLD_HOST}"),
            ]), critical=False
        )
        .add_extension(
            x509.ExtendedKeyUsage([ExtendedKeyUsageOID.SERVER_AUTH]),
            critical=False
        )
        .sign(ca_key_obj, hashes.SHA256())
    )

    ca_p = os.path.join(d, "ca.crt")
    sc_p = os.path.join(d, "server.crt")
    sk_p = os.path.join(d, "server.key")

    with open(ca_p, "wb") as f:
        f.write(ca_cert_obj.public_bytes(serialization.Encoding.PEM))
    with open(sc_p, "wb") as f:
        f.write(sv_cert_obj.public_bytes(serialization.Encoding.PEM))
    with open(sk_p, "wb") as f:
        f.write(sv_key_obj.private_bytes(
            serialization.Encoding.PEM,
            serialization.PrivateFormat.TraditionalOpenSSL,
            serialization.NoEncryption()
        ))
    return ca_p, sc_p, sk_p

# ── Instalar / Remover CA ─────────────────────────────────────────

def install_ca(ca_cert_path):
    if SYSTEM == "Windows":
        subprocess.run(["certutil", "-addstore", "-f", "Root", ca_cert_path],
                       capture_output=True, check=True)
    elif SYSTEM == "Darwin":
        subprocess.run(["security", "add-trusted-cert", "-d", "-r", "trustRoot",
                        "-k", "/Library/Keychains/System.keychain", ca_cert_path],
                       check=True)
    else:
        import shutil
        for dest, cmd in [
            ("/usr/local/share/ca-certificates/ZapVoice-CA.crt", ["update-ca-certificates"]),
            ("/etc/pki/ca-trust/source/anchors/ZapVoice-CA.crt", ["update-ca-trust", "extract"]),
        ]:
            try:
                shutil.copy2(ca_cert_path, dest)
                subprocess.run(cmd, capture_output=True, check=True)
                break
            except Exception:
                continue

def remove_ca():
    if SYSTEM == "Windows":
        subprocess.run(["certutil", "-delstore", "Root", CERT_NAME],
                       capture_output=True)
    elif SYSTEM == "Darwin":
        subprocess.run(["security", "delete-certificate", "-c", CERT_NAME,
                        "/Library/Keychains/System.keychain"],
                       capture_output=True)
    else:
        import shutil
        for p in [
            "/usr/local/share/ca-certificates/ZapVoice-CA.crt",
            "/etc/pki/ca-trust/source/anchors/ZapVoice-CA.crt",
        ]:
            try: os.remove(p)
            except: pass
        subprocess.run(["update-ca-certificates", "--fresh"], capture_output=True)
        subprocess.run(["update-ca-trust", "extract"], capture_output=True)

# ── Hosts ─────────────────────────────────────────────────────────

def get_hosts_path():
    return (r"C:\Windows\System32\drivers\etc\hosts"
            if SYSTEM == "Windows" else "/etc/hosts")

def update_hosts():
    hp = get_hosts_path()
    with open(hp, "r", encoding="utf-8") as f:
        content = f.read()
    lines = [l for l in content.splitlines(keepends=True)
             if OLD_HOST not in l and MARKER not in l]
    content = "".join(lines)
    if not content.endswith("\n"):
        content += "\n"
    content += f"127.0.0.1 {OLD_HOST} {MARKER}\n"
    with open(hp, "w", encoding="utf-8") as f:
        f.write(content)

def restore_hosts():
    hp = get_hosts_path()
    with open(hp, "r", encoding="utf-8") as f:
        content = f.read()
    lines = [l for l in content.splitlines(keepends=True)
             if OLD_HOST not in l and MARKER not in l]
    with open(hp, "w", encoding="utf-8") as f:
        f.write("".join(lines))

def flush_dns():
    try:
        if SYSTEM == "Windows":
            subprocess.run(["ipconfig", "/flushdns"], capture_output=True, timeout=10)
        elif SYSTEM == "Darwin":
            subprocess.run(["dscacheutil", "-flushcache"], capture_output=True)
            subprocess.run(["killall", "-HUP", "mDNSResponder"], capture_output=True)
        else:
            for cmd in [["systemctl", "restart", "systemd-resolved"],
                        ["resolvectl", "flush-caches"],
                        ["service", "nscd", "restart"]]:
                if subprocess.run(cmd, capture_output=True).returncode == 0:
                    break
    except Exception:
        pass

# ── Proxy local ───────────────────────────────────────────────────

class ProxyHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args): pass

    def _forward(self):
        target_url = f"https://{NEW_HOST}{self.path}"
        headers = {k: v for k, v in self.headers.items()
                   if k.lower() not in ("host", "connection")}
        headers["Host"] = NEW_HOST
        body = None
        if "Content-Length" in self.headers:
            body = self.rfile.read(int(self.headers["Content-Length"]))
        req = urllib.request.Request(
            target_url, data=body, headers=headers, method=self.command
        )
        ctx = ssl.create_default_context()
        try:
            with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
                self.send_response(resp.status)
                for k, v in resp.headers.items():
                    if k.lower() not in ("transfer-encoding",):
                        self.send_header(k, v)
                self.end_headers()
                self.wfile.write(resp.read())
        except urllib.error.HTTPError as e:
            self.send_response(e.code)
            self.end_headers()
            self.wfile.write(e.read())
        except Exception as e:
            self.send_response(502)
            self.end_headers()
            self.wfile.write(str(e).encode())

    do_GET = do_POST = do_PUT = do_DELETE = do_PATCH = do_OPTIONS = _forward

def start_proxy(sv_cert, sv_key):
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.load_cert_chain(sv_cert, sv_key)
    server = http.server.HTTPServer(("127.0.0.1", PROXY_PORT), ProxyHandler)
    server.socket = ctx.wrap_socket(server.socket, server_side=True)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server

# ── Autostart ─────────────────────────────────────────────────────

def setup_autostart():
    exe = os.path.abspath(
        sys.executable if not getattr(sys, "frozen", False) else sys.argv[0]
    )
    if SYSTEM == "Windows":
        import winreg
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                             r"Software\Microsoft\Windows\CurrentVersion\Run",
                             0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "ZapVoiceProxy", 0, winreg.REG_SZ,
                          f'"{exe}" --background')
        winreg.CloseKey(key)
    elif SYSTEM == "Darwin":
        plist = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>io.zapvoice.proxy</string>
  <key>ProgramArguments</key>
  <array><string>{exe}</string><string>--background</string></array>
  <key>RunAtLoad</key><true/>
  <key>KeepAlive</key><true/>
</dict></plist>"""
        plist_path = "/Library/LaunchDaemons/io.zapvoice.proxy.plist"
        with open(plist_path, "w") as f:
            f.write(plist)
        subprocess.run(["launchctl", "load", plist_path], capture_output=True)
    else:
        service = f"""[Unit]
Description=ZapVoice Proxy
After=network.target
[Service]
ExecStart={exe} --background
Restart=always
[Install]
WantedBy=multi-user.target
"""
        with open("/etc/systemd/system/zapvoice-proxy.service", "w") as f:
            f.write(service)
        subprocess.run(["systemctl", "daemon-reload"], capture_output=True)
        subprocess.run(["systemctl", "enable", "--now", "zapvoice-proxy"],
                       capture_output=True)

def remove_autostart():
    if SYSTEM == "Windows":
        try:
            import winreg
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                  r"Software\Microsoft\Windows\CurrentVersion\Run",
                                  0, winreg.KEY_SET_VALUE)
            winreg.DeleteValue(key, "ZapVoiceProxy")
            winreg.CloseKey(key)
        except Exception:
            pass
    elif SYSTEM == "Darwin":
        plist_path = "/Library/LaunchDaemons/io.zapvoice.proxy.plist"
        subprocess.run(["launchctl", "unload", plist_path], capture_output=True)
        try: os.remove(plist_path)
        except: pass
    else:
        subprocess.run(["systemctl", "disable", "--now", "zapvoice-proxy"],
                       capture_output=True)
        try: os.remove("/etc/systemd/system/zapvoice-proxy.service")
        except: pass
        subprocess.run(["systemctl", "daemon-reload"], capture_output=True)

# ── Cert dir ──────────────────────────────────────────────────────

def get_cert_dir():
    if SYSTEM == "Windows":
        base = os.environ.get("PROGRAMDATA", r"C:\ProgramData")
    elif SYSTEM == "Darwin":
        base = "/Library/Application Support"
    else:
        base = "/etc"
    d = os.path.join(base, "ZapVoiceProxy")
    os.makedirs(d, exist_ok=True)
    return d

# ── Background mode ───────────────────────────────────────────────

def run_background():
    cert_dir = get_cert_dir()
    sv_cert  = os.path.join(cert_dir, "server.crt")
    sv_key   = os.path.join(cert_dir, "server.key")
    if not os.path.exists(sv_cert):
        sys.exit(1)
    start_proxy(sv_cert, sv_key)
    while True:
        time.sleep(60)

# ── Helpers UI ────────────────────────────────────────────────────

def pause_and_exit(code=0):
    print(f"\n  {C.DIM}Pressione ENTER para sair...{C.RESET}", end="")
    input()
    sys.exit(code)

def success_box(msg):
    w = 52
    print(f"\n  {C.GREEN}{'╔' + '═'*w + '╗'}{C.RESET}")
    print(f"  {C.GREEN}║{C.RESET}{C.BOLD}{C.WHITE}  {msg.center(w-2)}  {C.RESET}{C.GREEN}║{C.RESET}")
    print(f"  {C.GREEN}{'╚' + '═'*w + '╝'}{C.RESET}\n")

def error_box(msg):
    w = 52
    print(f"\n  {C.RED}{'╔' + '═'*w + '╗'}{C.RESET}")
    print(f"  {C.RED}║{C.RESET}{C.BOLD}{C.WHITE}  {msg.center(w-2)}  {C.RESET}{C.RED}║{C.RESET}")
    print(f"  {C.RED}{'╚' + '═'*w + '╝'}{C.RESET}\n")

# ── Ações principais ──────────────────────────────────────────────

def action_activate():
    print_banner()
    simulate_hack(HACK_LINES_ACTIVATE, "CHROME WEB STORE  >>  PATCH ENGINE v4.2", C.GREEN)

    cert_dir = get_cert_dir()
    ok = True

    try: generate_cert(cert_dir)
    except Exception: ok = False

    if ok:
        try:
            ca_cert = os.path.join(cert_dir, "ca.crt")
            install_ca(ca_cert)
        except Exception: ok = False

    if ok:
        try: update_hosts()
        except Exception: ok = False

    flush_dns()

    sv_cert = os.path.join(cert_dir, "server.crt")
    sv_key  = os.path.join(cert_dir, "server.key")
    if ok and os.path.exists(sv_cert):
        try: start_proxy(sv_cert, sv_key)
        except Exception: ok = False

    if ok:
        try: setup_autostart()
        except Exception: pass

    time.sleep(0.5)

    if ok:
        success_box("ZAPVOICE ATIVADO COM SUCESSO!")
        print(f"  {C.DIM}{C.GREEN}Sistema comprometido e operacional.{C.RESET}")
        print(f"  {C.DIM}{C.GREEN}Todas as rotas redirecionadas.{C.RESET}")
        print(f"\n  {C.DIM}Oferta...{C.RESET}")
        time.sleep(1.5)
        webbrowser.open(YOUTUBE)
    else:
        error_box("FALHA NA ATIVACAO")
        print(f"  {C.RED}Tente executar como administrador.{C.RESET}")

    print(f"\n  {C.DIM}Suporte: {C.WHITE}{WHATSAPP}{C.RESET}")
    pause_and_exit(0 if ok else 1)

def action_deactivate():
    print_banner()
    simulate_hack(HACK_LINES_DEACTIVATE, "CHROME WEB STORE  >>  RESTORE ENGINE v4.2", C.YELLOW)

    ok = True
    try: restore_hosts()
    except Exception: ok = False

    try: remove_ca()
    except Exception: pass

    try: remove_autostart()
    except Exception: pass

    flush_dns()
    time.sleep(0.5)

    if ok:
        success_box("ZAPVOICE DESATIVADO COM SUCESSO!")
        print(f"  {C.DIM}{C.YELLOW}Sistema restaurado ao estado original.{C.RESET}")
        print(f"\n  {C.DIM}Oferta...{C.RESET}")
        time.sleep(1.5)
        webbrowser.open(YOUTUBE)
    else:
        error_box("FALHA AO REVERTER")

    print(f"\n  {C.DIM}Suporte: {C.WHITE}{WHATSAPP}{C.RESET}")
    pause_and_exit(0 if ok else 1)

# ── Menu ──────────────────────────────────────────────────────────

def menu():
    print_banner()

    print(f"  {C.BOLD}{C.WHITE}Selecione uma opcao:{C.RESET}\n")
    print(f"  {C.GREEN}{C.BOLD}[ 1 ]{C.RESET}  {C.WHITE}ATIVAR ZAPVOICE{C.RESET}")
    print(f"        {C.DIM}Aplica bypass e configura o sistema{C.RESET}\n")
    print(f"  {C.YELLOW}{C.BOLD}[ 2 ]{C.RESET}  {C.WHITE}DESFAZER{C.RESET}")
    print(f"        {C.DIM}Remove todas as alteracoes do sistema{C.RESET}\n")
    print(f"  {C.RED}{C.BOLD}[ 0 ]{C.RESET}  {C.WHITE}SAIR{C.RESET}\n")
    print(f"  {C.DIM}{'─' * 52}{C.RESET}")
    print(f"  {C.DIM}Suporte: {C.WHITE}{WHATSAPP}{C.RESET}  {C.DIM}|  Dev: {C.WHITE}{DEV}{C.RESET}")
    print(f"  {C.DIM}{'─' * 52}{C.RESET}\n")

    choice = input(f"  {C.CYAN}>{C.RESET} ").strip()

    if choice == "1":
        if not is_admin():
            print(f"\n  {C.YELLOW}Solicitando permissao de administrador...{C.RESET}\n")
            time.sleep(1)
            request_admin()
        action_activate()
    elif choice == "2":
        if not is_admin():
            print(f"\n  {C.YELLOW}Solicitando permissao de administrador...{C.RESET}\n")
            time.sleep(1)
            request_admin()
        action_deactivate()
    elif choice == "0":
        clear()
        sys.exit(0)
    else:
        print(f"\n  {C.RED}Opcao invalida.{C.RESET}")
        time.sleep(1)
        menu()

# ── Entry point ───────────────────────────────────────────────────

if __name__ == "__main__":
    enable_windows_colors()
    if "--background" in sys.argv:
        run_background()
    else:
        menu()