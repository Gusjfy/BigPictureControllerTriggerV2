# 🎮 Steam Big Picture Trigger + Áudio Automático

Este script em Python detecta quando um controle de Xbox é conectado ao computador e:

1. **Abre a Steam**, caso ela não esteja rodando.
2. **Ativa automaticamente o modo Big Picture**.
3. **Altera a saída de áudio** para a **TV** (ou qualquer dispositivo configurado por você).

Ideal para setups de jogos com controle em ambientes como salas, TVs ou home theaters.

---

## 🎮 Compatibilidade com Controles

Este script utiliza a API **XInput** do Windows para detectar se um controle está conectado. Por isso, apenas dispositivos compatíveis com XInput serão reconhecidos.

### ✅ Compatíveis
Os seguintes controles funcionam corretamente com este script:

- Xbox 360 (USB ou sem fio com receptor)
- Xbox One
- Xbox Series X|S
- Controles genéricos com suporte a XInput (alguns modelos imitam controles Xbox)

### ❌ Não compatíveis
Controles que **não usam XInput** não serão detectados:

- PlayStation 3 / 4 / 5
- Controles genéricos Bluetooth (sem XInput)
- Controles DirectInput ou HID convencionais
- Joy-Cons, Switch Pro Controller, etc.

> 💡 Se você precisa de suporte a outros controles além dos da Microsoft, será necessário adaptar o script para usar bibliotecas como `inputs`, `pygame` ou APIs como DirectInput.

---

## 🚀 Como usar

1. Clone este repositório.
2. Edite a variável `TV_AUDIO_NAME` no script `script_bp_steam.py` para corresponder ao primeiro nome/palavra da sua saída de áudio (ex: `"SAMSUNG"`). Para saber qual o nome da saida de audio, instale o modulo do proximo AudioDeviceCmdlets tópico.
3. Use o comando de build descrito no arquivo `Build Command.txt` para empacotar o script como um `.exe`.

O script ficará rodando em **segundo plano**. Quando detectar que o controle foi conectado, ele:
- Abre a Steam (caso esteja fechada).
- Ativa o Big Picture.
- Altera a saída de som automaticamente.

---

## 🔊 Como instalar o módulo AudioDeviceCmdlets

Este script usa o módulo `AudioDeviceCmdlets` do PowerShell para alterar a saída de áudio do sistema.

### ✅ Passo a passo para instalar:

1. **Abra o PowerShell como administrador**:
   - Pressione `Win + S`, digite `PowerShell`, clique com o botão direito e selecione **"Executar como administrador"**.

2. **Execute o comando abaixo para instalar o módulo:**

   ```powershell
   Install-Module -Name AudioDeviceCmdlets -Scope CurrentUser
   ```

3. Quando perguntado sobre confiar no repositório, digite `S` e pressione Enter.

4. Para testar se funcionou, execute:

   ```powershell
   Get-AudioDevice -List
   ```

   Isso deve listar todos os dispositivos de saída de som disponíveis.

> ⚠️ Este módulo é necessário para que a função de troca de áudio funcione corretamente.

---

## ⚠️ Alerta do Windows Defender

Durante a build para `.exe`, **o Windows Defender pode detectar o executável como um Trojan (falso positivo)**.

Isso acontece por alguns motivos:
- O script **acessa processos do sistema** (para detectar se a Steam está rodando).
- Ele **executa comandos PowerShell** para alterar a saída de áudio.
- O código é empacotado em um único `.exe` com `PyInstaller`, que é uma técnica frequentemente usada por malwares.

**Como resolver:**
- Você pode permitir manualmente o `.exe` na quarentena do Windows Defender.
- Ou clonar o repositório e rodar o script diretamente com Python, sem gerar um `.exe`.

> Nenhuma parte do código realiza atividades maliciosas. Todo o comportamento é transparente e focado apenas em automação local para jogos.

---

## 🔄 Inicializar com o Windows

Se você quiser que o script seja executado automaticamente ao ligar o computador, siga os passos abaixo:

1. Compile o script `.py` para `.exe` (veja instruções no item "Build Command").
2. Copie o `.exe` gerado para um local fixo, como:  
   `C:\Users\SeuUsuario\AppData\Local\Programs\SteamBigPictureTrigger\`
3. Pressione `Win + R`, digite `shell:startup` e pressione Enter.
4. Na pasta que abrir, crie um **atalho** para o seu `.exe`.
5. Pronto! Agora, o script será iniciado automaticamente com o Windows.

> 💡 **Dica:** Você pode configurar esse atalho para "Executar minimizado", evitando que a janela apareça momentaneamente.

---

## 📦 Build do executável

No arquivo `Build Command.txt`, você encontrará o comando `pyinstaller` para empacotar o projeto com tudo necessário. Ele usa:
- `--onefile` para gerar um único `.exe`
- `--noconsole` para esconder o terminal (o terminal só aparece temporariamente quando o trigger é ativado)

---

## 🛠️ Requisitos

- Python 3.8+
- Módulos Python:
  - `psutil`
  - `ctypes`
  - `subprocess`

- Módulo PowerShell:
  - `AudioDeviceCmdlets` (ver instruções acima)

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

**Contribuições e melhorias são bem-vindas!**
