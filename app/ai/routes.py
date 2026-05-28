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
        "you are a ai assistant"
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