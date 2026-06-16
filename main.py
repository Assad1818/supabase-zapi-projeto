from supabase import create_client
from dotenv import load_dotenv
import requests
import os

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

contatos = (
    supabase
    .table("contatos")
    .select("*")
    .limit(3)
    .execute()
)

for contato in contatos.data:
    nome = contato["nome"]
    telefone = contato["telefone"]

    mensagem = f"Olá, {nome} tudo bem com você?"

    url = (
        f"https://api.z-api.io/instances/"
        f"{os.getenv('ZAPI_INSTANCE_ID')}"
        f"/token/{os.getenv('ZAPI_TOKEN')}/send-text"
    )

    payload = {
        "phone": telefone,
        "message": mensagem
    }

    response = requests.post(url, json=payload)

    print(
        f"Mensagem enviada para {nome} - "
        f"Status: {response.status_code}"
    )