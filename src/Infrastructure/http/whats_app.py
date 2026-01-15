import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()  # Carrega variáveis do .env


def format_phone(telefone: str) -> str:
    """
    Normaliza o telefone para o padrão E.164 exigido pelo Twilio
    Ex: 11970507045 -> +5511970507045
    """
    telefone = telefone.replace(" ", "").replace("-", "")

    if not telefone.startswith("+"):
        telefone = "+55" + telefone

    return telefone


def enviar_codigo_whatsapp(telefone: str, codigo: str):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_number = os.getenv("TWILIO_WHATSAPP_FROM", "whatsapp:+14155238886")

    # 🔒 Validação mínima
    if not account_sid or not auth_token:
        raise RuntimeError("Credenciais do Twilio não configuradas")

    telefone_formatado = format_phone(telefone)

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_=from_number,
        to=f"whatsapp:{telefone_formatado}",
        body=f"Seu código de ativação é: {codigo}"
    )

    print(
        f"[Twilio] Mensagem enviada para {telefone_formatado}, SID: {message.sid}"
    )

    return message.sid
