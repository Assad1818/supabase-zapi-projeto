# Supabase + Z-API WhatsApp

Projeto desenvolvido em Python para ler contatos armazenados no Supabase e enviar mensagens personalizadas via WhatsApp utilizando a Z-API.

## Estrutura da tabela

Criar uma tabela chamada `contatos` no Supabase:

| Campo    | Tipo               |
| -------- | ------------------ |
| id       | int8 (Primary Key) |
| nome     | text               |
| telefone | text               |

Exemplo de registro:

| id | nome            | telefone      |
| -- | --------------- | ------------- |
| 1  | Guilherme Assad | 5513996720969 |

## Variáveis de ambiente

Criar um arquivo `.env` na raiz do projeto:

```env
SUPABASE_URL=https://seu-projeto.supabase.co
SUPABASE_KEY=sua_chave_supabase

ZAPI_INSTANCE_ID=seu_instance_id
ZAPI_TOKEN=seu_token
```

## Instalação

```bash
pip install -r requirements.txt
```

## Execução

```bash
python main.py
```

## Mensagem enviada

O sistema envia a seguinte mensagem para cada contato encontrado:

```text
Olá, <nome_contato> tudo bem com você?
```

O envio é limitado a até 3 contatos por execução.
