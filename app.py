from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText

load_dotenv()

app = Flask(__name__)
CORS(app)

EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "API está ativa"}), 200


@app.route("/contact", methods=["POST"])
def contact():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    # Enviar e-mail
    body = f"Nome: {name}\nEmail: {email}\nMensagem:\n{message}"
    msg = MIMEText(body)
    msg["Subject"] = "Nova mensagem do portfólio"
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg["Reply-To"] = email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_FROM, EMAIL_PASSWORD)
            server.send_message(msg)

        return jsonify({"message": "Message send!"}), 200

    except Exception as e:
        print("Erro ao enviar:", e)
        return jsonify({"error": "Oops, something went wrong."}), 500

if __name__ == "__main__":
    app.run()
