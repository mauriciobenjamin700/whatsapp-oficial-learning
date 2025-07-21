# PyWa - Python WhatsApp Cloud API Wrapper

## O que é PyWa?

PyWa é um wrapper Python para a WhatsApp Cloud API que simplifica o processo de integração e desenvolvimento de aplicações WhatsApp Business. É uma biblioteca não oficial mantida pela comunidade que oferece uma interface pythônica para todas as funcionalidades da API.

## Instalação

### Instalação Básica

```bash
pip3 install -U pywa
```

### Instalação do Código Fonte (versão mais recente)

```bash
git clone https://github.com/david-lev/pywa.git
cd pywa && pip3 install -U .
```

### Instalações com Dependências Específicas

Para usar recursos de webhook:

```bash
# Com FastAPI
pip3 install -U "pywa[fastapi]"

# Com Flask
pip3 install -U "pywa[flask]"
```

Para usar recursos de Flow com criptografia:

```bash
pip3 install -U "pywa[cryptography]"
```

## Configuração Inicial

### 1. Criando uma Aplicação WhatsApp

**Pré-requisitos:**

- Conta de desenvolvedor do Facebook ([registre-se aqui](https://developers.facebook.com))
- Meta Business Account

**Passos:**

1. Acesse [Meta for Developers > My Apps](https://developers.facebook.com/apps/)
2. Clique em "Create App"
3. Selecione "Business" como tipo de app
4. Preencha nome da aplicação e email
5. Na tela "Add products to your app", procure por "WhatsApp" e clique em "Set Up"
6. Selecione ou crie uma Meta Business Account

### 2. Configurando a App

Após criar a aplicação:

1. No menu lateral, expanda "WhatsApp" e clique em "API Setup"
2. Anote o **Temporary access token** (válido por 24 horas)
3. Anote o **Phone number ID**

> **Atenção:** Para produção, você precisará criar um token permanente.

### 3. Número de Teste

Se não tiver um número real conectado:
- Use o número de teste fornecido pela Meta
- Adicione até 5 números na lista "Allowed Numbers"
- Mensagens só podem ser enviadas para números autorizados

## Uso Básico

### Iniciando o Cliente WhatsApp

```python
from pywa import WhatsApp

wa = WhatsApp(
    phone_id='SEU_PHONE_ID',  # ID do número obtido na configuração
    token='SEU_TOKEN'         # Token obtido na configuração
)
```

### Enviando Mensagens

#### Mensagem de Texto
```python
wa.send_message(
    to='NUMERO_DESTINATARIO',
    text='Olá! Esta mensagem foi enviada com PyWa!'
)
```

#### Enviando Imagem
```python
wa.send_image(
    to='NUMERO_DESTINATARIO',
    image='https://exemplo.com/imagem.jpg'
)
```

### Formato do Número de Telefone

- **Obrigatório:** Incluir código do país
- **Exemplos válidos:** `+5511999999999`, `16315551234`
- **Sem:** Parênteses, traços ou espaços

### Importante - Política de Mensagens

- **Mensagens livres:** Só podem ser enviadas se o destinatário tiver enviado uma mensagem nas últimas 24 horas
- **Mensagens de template:** Podem ser enviadas a qualquer momento (após aprovação)

## Componentes Principais do PyWa

### 1. WhatsApp Client
**Funcionalidade central** que permite:
- Enviar e receber mensagens e mídia
- Registrar callbacks para eventos
- Gerenciar perfil e configurações do negócio
- Administrar configurações da conta

### 2. Handlers (Manipuladores)
**Sistema de callbacks** para:
- Registrar funções que respondem a eventos específicos
- Processar mensagens recebidas
- Lidar com callbacks de botões e interações

### 3. Listeners (Ouvintes)
**Monitoramento de eventos** para:
- Escutar atualizações de usuários em tempo real
- Processar diferentes tipos de mensagens
- Reagir a mudanças de status

### 4. Filters (Filtros)
**Sistema de condições** para:
- Filtrar mensagens por conteúdo específico
- Aplicar lógica condicional a callbacks
- Direcionar mensagens para handlers específicos

**Exemplo:**
```python
# Processar apenas mensagens que contenham "olá"
@wa.on_message(filters.text.contains("olá"))
def handle_greeting(client, message):
    message.reply("Olá! Como posso ajudar?")
```

### 5. Updates (Atualizações)
**Tipos de eventos** que o cliente pode receber:
- Mensagens de texto, mídia, documentos
- Callbacks de botões e menus
- Mudanças de status de entrega
- Eventos de usuário (online/offline)

### 6. Flows (Fluxos)
**Criação de fluxos interativos** para:
- Criar formulários e questionários
- Coletar informações do usuário
- Guiar conversas estruturadas

### 7. Error Handling (Tratamento de Erros)
**Gerenciamento de exceções** para:
- Capturar erros da API
- Lidar com falhas de conexão
- Implementar retry automático

## Exemplo Prático Completo

```python
from pywa import WhatsApp
from pywa.filters import text

# Inicializar cliente
wa = WhatsApp(
    phone_id='your_phone_id',
    token='your_token'
)

# Handler para mensagens de texto que contêm "oi"
@wa.on_message(text.contains("oi"))
def cumprimentar(client, message):
    client.send_message(
        to=message.from_user.wa_id,
        text=f"Olá {message.from_user.name}! Como posso ajudar?"
    )

# Handler para receber qualquer mensagem
@wa.on_message()
def processar_mensagem(client, message):
    print(f"Mensagem recebida de {message.from_user.name}: {message.text}")

# Iniciar o webhook (para receber mensagens)
if __name__ == "__main__":
    wa.run()
```

## Recursos Avançados

### Webhook Configuration
Para receber mensagens, configure webhooks:

```python
# Com FastAPI (recomendado)
wa = WhatsApp(
    phone_id='your_phone_id',
    token='your_token',
    server='fastapi',
    webhook_endpoint='/webhook',
    webhook_verify_token='your_verify_token'
)
```

### Enviando Diferentes Tipos de Mídia

```python
# Documento
wa.send_document(
    to='numero',
    document='https://exemplo.com/arquivo.pdf',
    caption='Documento importante'
)

# Áudio
wa.send_audio(
    to='numero',
    audio='https://exemplo.com/audio.mp3'
)

# Vídeo
wa.send_video(
    to='numero',
    video='https://exemplo.com/video.mp4',
    caption='Vídeo explicativo'
)
```

### Usando Templates

```python
wa.send_template(
    to='numero',
    template='nome_do_template',
    language='pt_BR',
    components=[
        {
            "type": "body",
            "parameters": [
                {"type": "text", "text": "João"}
            ]
        }
    ]
)
```

## Vantagens do PyWa

✅ **Interface Pythônica**: Sintaxe limpa e intuitiva
✅ **Documentação Completa**: Exemplos e guias detalhados  
✅ **Suporte a Webhooks**: Recepção de mensagens em tempo real
✅ **Filtros Avançados**: Sistema flexível de roteamento
✅ **Tratamento de Erros**: Gerenciamento robusto de exceções
✅ **Tipos de Mídia**: Suporte completo para todos os formatos
✅ **Flows Interativos**: Criação de formulários dinâmicos
✅ **Comunidade Ativa**: Mantido pela comunidade open-source

## Links Úteis

- 📖 [Documentação Oficial](https://pywa.readthedocs.io/)
- 🐙 [Repositório GitHub](https://github.com/david-lev/pywa)
- 💡 [Exemplos Práticos](https://github.com/david-lev/pywa/tree/main/examples)
- 🔧 [Issues e Suporte](https://github.com/david-lev/pywa/issues)

---

> **Nota**: PyWa é um projeto de código aberto não afiliado à Meta. Para funcionalidades oficiais, sempre consulte a documentação da WhatsApp Cloud API.