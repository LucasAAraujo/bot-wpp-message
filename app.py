from flask import Flask, request, jsonfy
#from whatsapp import send_whatsapp_message

app = Flask(__name__)

@app.route("/github-webhook", methods=["POST"])

def github_webhook():
    data = request.json

    if "commits" in data:
        for commit in data["commits"]:
            message = f"🚀 Nova atualização na plataforma v2 - {commit['message']} - acesse em: sitedaweb.com"
            send_whatsapp_message(message)

    return jsonfy({"status":"ok"})

if __name__ == "__main__":
    app.run(port=5000, debug=True)

