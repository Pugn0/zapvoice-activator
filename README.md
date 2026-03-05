# ZapVoice Pro — Activator

> Ferramenta de ativação automática do ZapVoice PRO.  
> Substitui a configuração manual do Charles Proxy por um executável simples.

---

## Como funciona

O activator realiza todo o processo de ativação automaticamente:

- Gera um certificado SSL local para o domínio da API
- Instala o certificado CA na loja de certificados do sistema
- Redireciona o tráfego da API via arquivo hosts
- Sobe um proxy HTTPS local transparente
- Configura inicialização automática com o sistema

---

## Requisitos

- Python 3.10 ou superior
- pip
- Git (opcional, recomendado — inclui OpenSSL no Windows)

---

## Instalação e build

### 1. Clone o repositório

```bash
git clone https://github.com/Pugn0/zapvoice-activator.git
cd zapvoice-activator
```

### 2. Crie o ambiente virtual e instale as dependências

**Windows:**
```powershell
py -m venv venv
venv\Scripts\activate
pip install pyinstaller cryptography
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install pyinstaller cryptography
```

### 3. Gere o executável

**Windows** (com ícone):
```powershell
pyinstaller --onefile --icon="zapvoice.ico" --name "ZapVoice-Activator" zapvoice_redirect.py
```

**macOS / Linux:**
```bash
pyinstaller --onefile --name "ZapVoice-Activator" zapvoice_redirect.py
```

O executável gerado estará em:
```
dist/ZapVoice-Activator.exe   ← Windows
dist/ZapVoice-Activator        ← macOS / Linux
```

---

## Rebuild rápido

Com o ambiente virtual já criado, para rebuildar após editar o script:

**Windows:**
```powershell
venv\Scripts\activate && pyinstaller --onefile --icon="zapvoice.ico" --name "ZapVoice-Activator" zapvoice_redirect.py
```

**macOS / Linux:**
```bash
source venv/bin/activate && pyinstaller --onefile --name "ZapVoice-Activator" zapvoice_redirect.py
```

---

## Dependências

| Pacote | Versão mínima | Uso |
|---|---|---|
| `pyinstaller` | 6.0+ | Empacotamento do executável |
| `cryptography` | 40.0+ | Geração de certificados SSL |

> A lib `cryptography` é usada como fallback caso o OpenSSL não esteja disponível no sistema.  
> Se o Git for Windows estiver instalado, o OpenSSL nativo será usado automaticamente.

---

## Estrutura do projeto

```
zapvoice-activator/
├── zapvoice_redirect.py   # Script principal
├── zapvoice.ico           # Ícone do executável
├── README.md              # Este arquivo
├── venv/                  # Ambiente virtual (não versionar)
├── build/                 # Gerado pelo PyInstaller (não versionar)
└── dist/                  # Executável final (não versionar)
```

---

## .gitignore recomendado

```
venv/
build/
dist/
*.spec
__pycache__/
*.pyc
```

---

## Uso do executável

Execute como **administrador** e selecione uma opção no menu:

```
[ 1 ]  ATIVAR ZAPVOICE    → aplica todas as configurações
[ 2 ]  DESFAZER           → remove todas as alterações do sistema
[ 0 ]  SAIR
```

---

## Suporte

- 📱 WhatsApp: +55 (61) 99603-7036
- 📺 Tutorial: https://youtu.be/2N1FhDn1wE0
- 💻 Dev: @pugno_fc
