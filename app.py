from flask import Flask, request, render_template, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key="AIzaSyCBJmCHBTXWVgpGgYpduODdD_f3ZVnE4uU")
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/send", methods=["POST"])
def send():
    user_message = request.json["message"]
    response = chat.send_message(user_message)
    return jsonify({"reply": response.text})


import os

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))  # Use Render-assigned port or 5000 locally
    )


