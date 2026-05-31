from flask import Blueprint, render_template, current_app, request, jsonify, json
from flask_login import login_required
from openai import OpenAI
import os


ai = Blueprint("ai", __name__)

client= OpenAI(
    base_url=os.getenv("base_url"),
    api_key=os.getenv("API_KEY")
)

messages= [
    {
        "role" : "system",
        "content" : 
        """Y
        You are the AI assistant for Aroku's website.

About Aroku:
- Independent developer from India.
- Building AI, web, and backend projects.
- Works mainly with Python, Flask, APIs, and AI technologies.
- Passionate about learning and creating useful software.

Your role:
- Help users navigate the website.
- Answer questions about projects.
- Explain features.
- Provide friendly technical assistance.
- If asked personal questions about Aroku, answer using available information but do not invent details.
- If information is unknown, say so honestly.
"""
    }
]

@ai.route("/chat", methods=["GET","POST"])
@login_required
def ai_chat():

    if request.method == "GET" : 
        return render_template(
            "ai/index.html"
        )
    

    user_message= request.json.get("message")

    messages.append(
        {
            "role" : "user",
            "content" : user_message
        }
    )
    
    response = client.chat.completions.create(
        model="openrouter/owl-alpha",
        messages=messages
    )
    
    ai_reply= response.choices[0].message.content

    messages.append(
        {
            "role" : "assistant",
            "content": ai_reply
        }
    )

    return jsonify({
        "reply" : ai_reply
    })