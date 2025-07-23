# WhatsApp Cloud API - Documentação Resumida

## Visão Geral

A **API de Nuvem do WhatsApp**, hospedada pela Meta, é uma solução empresarial que permite comunicação em escala entre empresas de grande e médio porte e seus clientes. A API possibilita:

- Conexão de milhares de clientes com agentes ou bots
- Comunicação programática e manual
- Integração com sistemas de back-end (CRM, marketing, etc.)

## Protocolo e Tecnologia

### HTTP e Graph API

A API é baseada na Graph API do Facebook e utiliza protocolo HTTP com:

- Parâmetros de URL
- Cabeçalhos de solicitação
- Corpos de solicitação em JSON

### Exemplo de Chamada API

```bash
curl 'https://graph.facebook.com/v22.0/106540352242922/messages' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer EAAJB...' \
-d '{
  "messaging_product": "whatsapp",
  "recipient_type": "individual",
  "to": "+16505555555",
  "type": "text",
  "text": {
    "preview_url": true,
    "body": "Aqui está a informação solicitada! https://www.meta.com/quest/quest-3/"
  }
}'
```

## Recursos Principais

### 1. Portfólios Empresariais

- **Obrigatório** para usar a API
- Contêiner para contas do WhatsApp Business (WABA) e números de telefone
- Criado durante o processo de integração

### 2. Contas do WhatsApp Business (WABA)

- Representa uma empresa na plataforma
- Contém metadados sobre o negócio
- Associada a números de telefone e modelos de mensagem

### 3. Números de Telefone Comerciais

- Números reais registrados para uso com a API
- Permitem troca de mensagens com usuários do WhatsApp
- Contêm metadados exibidos no cliente WhatsApp

### 4. Modelos de Mensagem

- Templates personalizáveis criados via API
- Passam por processo de análise e aprovação
- Reduzem feedback negativo dos destinatários

## Tipos de Mensagens

1. **Mensagens em Formato Livre**: Mais flexíveis
2. **Mensagens de Template**: Mais restritivas, mas com menor probabilidade de feedback negativo

## Webhooks

- Cargas JSON enviadas para endpoints públicos
- **Essenciais** para o funcionamento da API
- Transmitem:
  - Conteúdo de mensagens recebidas
  - Atualizações de status de entrega

## Autenticação e Autorização

### Tipos de Token de Acesso

1. Tokens de acesso de usuário do sistema
2. Tokens de acesso do usuário do sistema de integração comercial
3. Tokens de acesso do usuário

### Permissões Necessárias

- `business_management`: Interação com portfólio empresarial
- `whatsapp_business_management`: Interação com WABA e recursos associados
- `whatsapp_business_messaging`: Troca de mensagens com usuários

## Limites e Taxa de Transferência

### Taxa de Transferência Padrão

- **80 mensagens por segundo (mps)** por número comercial
- Pode aumentar para **1.000 mps** automaticamente
- Números coexistentes (app + API): **5 mps** fixo

### Limite de Volume de Emparelhamento

- **1 mensagem a cada 6 segundos** para o mesmo usuário
- Equivale a ~10 mensagens/minuto ou 600 mensagens/hora
- Possibilidade de envio em série: até 45 mensagens em 6 segundos

### Requisitos para Taxa Mais Alta (1.000 mps)

- Capacidade de iniciar conversas ilimitadas em 24h
- Registro na API de Nuvem
- Classificação de qualidade mínima: nível médio

## Recursos de Teste

- WABA e número de telefone de teste criados automaticamente
- Ignoram a maioria dos limites de mensagens
- Não exigem forma de pagamento registrada

## Ferramentas

### Gerenciador do WhatsApp

- Interface web para gerenciamento manual de recursos
- Visualização de insights e classificação de qualidade
- Acesso via Meta Business Suite, Painel de Apps ou URL direto

### SDKs de Terceiros

- **PyWa**: Wrapper em Python para a API
- **Postman**: Coleção com perguntas comuns

## Segurança

### Criptografia

- Mensagens protegidas por criptografia do protocolo Signal
- Técnicas padrão de criptografia para dados em trânsito e repouso
- HTTPS com TLS para Graph API e Webhooks

## Controle de Versões

- Baseado no protocolo de controle de versões da Graph API
- Cada versão disponível por aproximadamente 2 anos
- Suporte a múltiplas versões simultâneas

## Métricas e Análises

- Número de mensagens enviadas e entregues
- Métricas de engajamento e qualidade
- Análises detalhadas via API ou Gerenciador do WhatsApp

---

## Links Úteis

- [Documentação oficial da Graph API](https://developers.facebook.com/docs/graph-api/)
- [Meta Business Suite](https://business.facebook.com/)
- [Coleção Postman da API](https://www.postman.com/meta-whatsapp/)

---

**Nota**: Esta documentação é um resumo das principais funcionalidades da API de Nuvem do WhatsApp. Para informações detalhadas e atualizadas, consulte sempre a documentação oficial da Meta.
