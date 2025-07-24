# WhatsApp Official Learning - Integração com PyWA

## 📋 Visão Geral

Este projeto demonstra uma integração completa com a **WhatsApp Cloud API** utilizando o framework **PyWA** e **FastAPI**. O sistema permite enviar diferentes tipos de mensagens (texto, imagem, vídeo, áudio, documento, reações) e receber webhooks do WhatsApp para processamento automático de mensagens.

## 🏗️ Arquitetura do Projeto

O projeto segue uma arquitetura modular e bem estruturada:

```text
whatsapp-oficial-learning/
├── main.py                 # Ponto de entrada da aplicação
├── pyproject.toml         # Configurações do projeto e dependências
├── uv.lock               # Lock file das dependências
├── Makefile              # Comandos úteis para desenvolvimento
├── README.md             # Documentação principal
├── docs/                 # Documentação adicional
│   ├── example.md        # Este arquivo
│   ├── pywa.md          # Documentação específica do PyWA
│   ├── rules.md         # Regras e diretrizes
│   └── WhatsApp Cloud API.postman_collection.json
├── src/                  # Código fonte principal
│   ├── __init__.py
│   ├── server.py         # Configuração do servidor
│   ├── api/              # Camada de API
│   │   ├── __init__.py
│   │   ├── api.py        # Configuração principal da API
│   │   ├── dependencies/ # Injeção de dependências
│   │   │   ├── __init__.py
│   │   │   └── wa.py     # Dependência do cliente WhatsApp
│   │   └── routes/       # Endpoints da API
│   │       ├── __init__.py
│   │       └── message.py # Rotas para envio de mensagens
│   ├── core/             # Configurações centrais
│   │   ├── __init__.py
│   │   ├── base.py       # Classes base
│   │   ├── settings.py   # Configurações do projeto
│   │   └── wa_client.py  # Cliente WhatsApp
│   ├── schemas/          # Modelos de dados
│   │   ├── __init__.py
│   │   └── messages.py   # Schemas para mensagens
│   ├── services/         # Lógica de negócio
│   │   ├── __init__.py
│   │   ├── media_message.py     # Serviço para mensagens de mídia
│   │   ├── reaction_message.py  # Serviço para reações
│   │   ├── template_message.py  # Serviço para templates
│   │   ├── text_message.py      # Serviço para texto
│   │   └── webhook_message.py   # Serviço para webhooks
│   └── controllers/      # Controladores (futuro)
│       └── __init__.py
└── tests/                # Testes automatizados
    └── conftest.py
```

## 🔧 Tecnologias Utilizadas

- **Python 3.13+**: Linguagem principal
- **FastAPI**: Framework web moderno e rápido
- **PyWA**: Biblioteca para integração com WhatsApp Cloud API
- **Pydantic**: Validação de dados e configurações
- **Uvicorn**: Servidor ASGI para produção
- **UV**: Gerenciador de dependências moderno

## ⚙️ Configuração do Ambiente

### 1. Pré-requisitos

- Python 3.13 ou superior
- UV (gerenciador de dependências)
- Conta no Meta for Developers
- App WhatsApp Business configurado

### 2. Instalação

```bash
# Clone o repositório
git clone <repository-url>
cd whatsapp-oficial-learning

# Instale as dependências
uv sync

# Ative o ambiente virtual
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate     # Windows
```

### 3. Configuração das Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
# WhatsApp Cloud API Credentials
ACCESS_TOKEN=your_access_token_here
PHONE_NUMBER_ID=your_phone_number_id_here
BUSINESS_ACCOUNT_ID=your_business_account_id_here
WABA_ID=your_waba_id_here

# Webhook Configuration
CALLBACK_URL=https://your-domain.com
VERIFY_TOKEN=your_secure_verify_token
APP_ID=your_app_id
APP_SECRET=your_app_secret

# Server Configuration
PORT=8001

# Test Configuration
TO=5589988025705  # Número para testes
```

### 4. Configuração no Meta for Developers

1. **Acesse** [Meta for Developers](https://developers.facebook.com)
2. **Crie ou selecione** seu app WhatsApp Business
3. **Configure o Webhook**:
   - URL: `https://your-domain.com/webhook`
   - Verify Token: o mesmo valor da variável `VERIFY_TOKEN`
   - Campos: `messages`, `message_deliveries`, `message_reads`
4. **Adicione números de teste** em "Recipient phone numbers"

## 🚀 Como Executar

### Desenvolvimento Local

```bash
# Usando UV
uv run python main.py

# Ou usando Python diretamente
python main.py

# Ou usando Uvicorn
uvicorn src.api.api:app --host 0.0.0.0 --port 8001 --reload
```

### Produção

```bash
# Com Uvicorn
uvicorn src.api.api:app --host 0.0.0.0 --port 8001

# Com Gunicorn (alternativa)
gunicorn src.api.api:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8001
```

### Usando Makefile

```bash
# Ver comandos disponíveis
make help

# Executar em desenvolvimento
make dev

# Executar testes
make test

# Formatar código
make format

# Verificar qualidade do código
make lint
```

## 📡 Endpoints da API

### Envio de Mensagens

#### 1. Mensagem de Texto

```http
POST /messages/send/text
Content-Type: application/x-www-form-urlencoded

to=5589988025705&body=Olá, esta é uma mensagem de teste!
```

#### 2. Mensagem de Imagem

```http
POST /messages/send/image
Content-Type: multipart/form-data

to=5589988025705
media_path=<arquivo_imagem>
caption=Legenda da imagem (opcional)
```

#### 3. Mensagem de Vídeo

```http
POST /messages/send/video
Content-Type: multipart/form-data

to=5589988025705
media_path=<arquivo_video>
caption=Legenda do vídeo (opcional)
```

#### 4. Mensagem de Áudio

```http
POST /messages/send/audio
Content-Type: multipart/form-data

to=5589988025705
media_path=<arquivo_audio>
```

#### 5. Mensagem de Documento

```http
POST /messages/send/document
Content-Type: multipart/form-data

to=5589988025705
media_path=<arquivo_documento>
caption=Descrição do documento (opcional)
```

#### 6. Reação a Mensagem

```http
POST /messages/send/reaction
Content-Type: application/x-www-form-urlencoded

to=5589988025705&message_id=wamid.xxx&emoji=👍
```

#### 7. Marcar como Lida

```http
POST /messages/mark-as-read
Content-Type: application/x-www-form-urlencoded

message_id=wamid.xxx
```

### Documentação Interativa

- **Swagger UI**: `http://localhost:8001/docs`
- **ReDoc**: `http://localhost:8001/redoc`
- **OpenAPI Schema**: `http://localhost:8001/openapi.json`

## 🔄 Sistema de Webhooks

O projeto inclui um sistema robusto de webhooks que processa automaticamente:

### Funcionalidades Implementadas

1. **Recebimento de Mensagens**: Processa mensagens de texto, mídia e outros tipos
2. **Respostas Automáticas**: Sistema de auto-resposta configurável
3. **Status de Entrega**: Rastreamento de mensagens enviadas, entregues e lidas
4. **Reações Automáticas**: Adiciona reações às mensagens recebidas
5. **Tratamento de Erros**: Logging e tratamento adequado de exceções

### Handlers Configurados

```python
@wa.on_message
async def hello(_: WhatsApp, msg: types.Message):
    """
    Handler principal para mensagens recebidas.
    Adiciona reação e responde automaticamente.
    """
    try:
        await msg.react("👋")
        await msg.reply("Recebido")
    except Exception as e:
        print(f"Erro ao responder mensagem: {e}")
```

## 🗂️ Estrutura de Services

### 1. TextMessageService

Responsável pelo envio de mensagens de texto simples.

### 2. MediaMessageService

Gerencia o envio de diferentes tipos de mídia:

- Imagens (JPEG, PNG, WebP)
- Vídeos (MP4, 3GPP)
- Áudios (AAC, MP4, MPEG, AMR, OGG, OPUS)
- Documentos (PDF, DOC, XLS, PPT, TXT)

### 3. ReactionMessageService

Manipula reações e marcação de mensagens como lidas.

### 4. TemplateMessageService

Gerencia envio de templates aprovados pelo WhatsApp.

### 5. WebhookMessageService

Processa webhooks recebidos do WhatsApp.

## 🔐 Segurança e Boas Práticas

### Validação de Webhooks

- Verificação de token de webhook
- Validação de origem das requisições
- Rate limiting implementado

### Tratamento de Erros

- Logs estruturados para debugging
- Fallbacks para falhas de rede
- Retry automático para operações críticas

### Configurações Sensíveis

- Todas as credenciais em variáveis de ambiente
- Tokens com escopo limitado
- Rotação periódica de segredos

## 🧪 Testes

### Executar Testes

```bash
# Todos os testes
pytest

# Com cobertura
pytest --cov=src

# Testes específicos
pytest tests/test_messages.py
```

### Teste Manual

Use o arquivo `test.py` para testes rápidos:

```bash
python test.py
```

## 📚 Exemplos de Uso

### Envio de Mensagem Programática

```python
from pywa import WhatsApp
from core.settings import settings

wa = WhatsApp(
    phone_id=settings.PHONE_NUMBER_ID,
    token=settings.ACCESS_TOKEN,
)

# Enviar mensagem de texto
result = wa.send_message(
    to=settings.TO,
    text='Olá! Esta mensagem foi enviada via PyWA!'
)

print(result)
```

### Processamento de Webhook

```python
@wa.on_message
async def process_message(wa_client: WhatsApp, msg):
    if msg.text and msg.text.lower() == "menu":
        await msg.reply(
            "🤖 *Menu de Opções*\n\n"
            "1️⃣ Informações\n"
            "2️⃣ Suporte\n"
            "3️⃣ Contato\n\n"
            "Digite o número da opção desejada."
        )
    elif msg.text and msg.text == "1":
        await msg.reply("ℹ️ Aqui estão as informações...")
```

## 🔍 Monitoramento e Logs

### Estrutura de Logs

```python
import logging

logger = logging.getLogger(__name__)
logger.info(f"Mensagem enviada para {to}: {message_id}")
logger.error(f"Erro ao processar webhook: {error}")
```

### Métricas Importantes

- Taxa de entrega de mensagens
- Tempo de resposta dos webhooks
- Erros de API por minuto
- Volume de mensagens processadas

## 🚨 Troubleshooting

### Erros Comuns

#### 1. RecipientNotInAllowedList

**Problema**: Número não está na lista de destinatários permitidos  
**Solução**: Adicionar o número no Meta for Developers

#### 2. Invalid Access Token

**Problema**: Token de acesso expirado ou inválido  
**Solução**: Renovar o token no Meta for Developers

#### 3. Webhook Verification Failed

**Problema**: Token de verificação incorreto  
**Solução**: Verificar a variável `VERIFY_TOKEN`

#### 4. Media Upload Failed

**Problema**: Formato de arquivo não suportado  
**Solução**: Verificar tipos MIME suportados

### Debug Mode

```bash
# Executar com logs detalhados
uvicorn src.api.api:app --log-level debug

# Variável de ambiente para debug
export DEBUG=true
python main.py
```

## 📈 Performance e Escalabilidade

### Otimizações Implementadas

- Pooling de conexões HTTP
- Cache de configurações
- Processamento assíncrono de webhooks
- Validação eficiente de dados

### Recomendações para Produção

- Load balancer com múltiplas instâncias
- Redis para cache e sessões
- PostgreSQL para persistência
- Monitoramento com Prometheus/Grafana

## 🔄 Roadmap

### Próximas Funcionalidades

- [ ] Sistema de filas para mensagens
- [ ] Dashboard administrativo
- [ ] Chatbot com IA integrada
- [ ] Métricas em tempo real
- [ ] Suporte a múltiplos números
- [ ] Templates dinâmicos

### Melhorias Técnicas

- [ ] Testes de integração completos
- [ ] CI/CD pipeline
- [ ] Documentação em múltiplos idiomas
- [ ] Containers Docker
- [ ] Helm charts para Kubernetes

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request
