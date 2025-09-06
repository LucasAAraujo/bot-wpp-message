# 📢 Bot GitHub → WhatsApp  

Este bot envia mensagens no **WhatsApp** automaticamente sempre que houver um **novo commit** em um repositório GitHub.  

---

## ⚙️ Funcionalidades  
- 🔔 Recebe notificações de **Webhooks do GitHub** (evento `push`).  
- 📝 Extrai a **mensagem do commit** e formata o aviso.  
- 📲 Envia a mensagem via **WhatsApp Cloud API (Meta)**.  

---

## 📦 Tecnologias Utilizadas  

### 🔹 Backend  
- **[Python](https://www.python.org/)** → Linguagem principal do projeto.  
- **[Flask](https://flask.palletsprojects.com/)** → Servidor HTTP para receber o webhook do GitHub.  

### 🔹 Comunicação HTTP  
- **[Requests](https://requests.readthedocs.io/)** → Para enviar requisições ao WhatsApp Cloud API.  

### 🔹 Integração  
- **[WhatsApp Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/)** → Canal oficial de envio das mensagens no WhatsApp.  
