from flask import Flask, request, jsonify
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

client = Groq()

@app.route("/ask", methods=["POST"])
def ask_groq():
    data = request.json
    user_question = data.get("question", "")

    if not user_question:
        return jsonify({"error": "Question is required"}), 400

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful web3 assistant. Respond in 30 words or less."},
            {"role": "user", "content": user_question}
        ],
        model="llama-3.3-70b-versatile",
    )

    response = chat_completion.choices[0].message.content
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
