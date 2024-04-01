from flask import Flask, render_template, request, redirect, url_for
from openai import OpenAI
import json

app = Flask(__name__)
app.static_folder = "static"

with open("api.json", "r") as keys:
    data = json.load(keys)

key = data['key']

keys.close()

math_messages = [{'sender': 'ai', 'message': ['Hello! I am your Math AI Tutor. I will help you with anything you need by making practice questions about Math! If you don\'t get the question, just ask me to explain. Thanks!.']}]
english_messages = [{'sender': 'ai', 'message': ['Hello! I am your English AI Tutor. I will help you with anything you need by making practice questions about Math! If you don\'t get the question, just ask me to explain. Thanks!.']}]
history_messages = [{'sender': 'ai', 'message': ['Hello! I am your History AI Tutor. I will help you with anything you need by making practice questions about Math! If you don\'t get the question, just ask me to explain. Thanks!.']}]
science_messages = [{'sender': 'ai', 'message': ['Hello! I am your Science AI Tutor. I will help you with anything you need by making practice questions about Math! If you don\'t get the question, just ask me to explain. Thanks!.']}]


client = OpenAI(api_key=key)

@app.route('/')
def home():
    return render_template("index.html", messsages=math_messages)

@app.route('/math')
def math():
    return render_template('math.html', messages=math_messages)

@app.route('/math', methods=['GET', 'POST'])
def math_submit():
    if request.method == 'POST':
        message = request.form['message']
        
        math_messages.append({'sender': 'human', 'message': [message]})
        
        no_messages_intro = "You are a math tutor. The following message will either either ask you to clarify a question, ask you for test questions, or ask you to explain a question. Answer the question to the best of your ability and try your hardest to replicate how a real tutor would answer the quesiton."
        
        prev_messages = ""
        for i in range(1, len(math_messages)):
            prev_messages += f"Message {i} from {math_messages[i]['sender']}: {'\n'.join(math_messages[i]['message'])}\n"
        message_intro = f"You are a math tutor. The following message will either either ask you to clarify a question, ask you for test questions, or ask you to explain a question. Answer the question to the best of your ability and try your hardest to replicate how a real tutor would answer the quesiton.\nTo Clarify the Conversation, Here are the previous messages (These are both from you (The AI, and The User (The Human))):\n{prev_messages}"
        
        intro = no_messages_intro if len(math_messages) == 1 else message_intro
        print(intro)        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": intro},
                {"role": "user", "content": f"{message}"}
            ]
        )
        
        ai_response = response.choices[0].message.content
        ai_response = ai_response.split("\n")
        print(ai_response)
        math_messages.append({'sender': 'ai', 'message': ai_response})        
    return redirect(url_for('math'))


@app.route('/english')
def english():
    return render_template("english.html", messages=english_messages)

@app.route('/english', methods=['GET', 'POST'])
def english_submit():
    if request.method == 'POST':
        message = request.form['message']
        
        english_messages.append({'sender': 'human', 'message': [message]})
        
        no_messages_intro = "You are an english tutor. The following message will either either ask you to clarify a question, ask you for test questions, or ask you to explain a question. Answer the question to the best of your ability and try your hardest to replicate how a real tutor would answer the quesiton."
        
        prev_messages = ""
        for i in range(1, len(english_messages)):
            prev_messages += f"Message {i} from {english_messages[i]['sender']}: {'\n'.join(english_messages[i]['message'])}\n"
        message_intro = f"You are an english tutor. The following message will either either ask you to clarify a question, ask you for test questions, or ask you to explain a question. Answer the question to the best of your ability and try your hardest to replicate how a real tutor would answer the quesiton.\nTo Clarify the Conversation, Here are the previous messages (These are both from you (The AI, and The User (The Human))):\n{prev_messages}"
        
        intro = no_messages_intro if len(english_messages) == 1 else message_intro
        print(intro)        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": intro},
                {"role": "user", "content": f"{message}"}
            ]
        )
                
        ai_response = response.choices[0].message.content
        
        ai_response = ai_response.split('\n')
        
        english_messages.append({'sender': 'ai', 'message': ai_response})     
    return redirect(url_for('english'))


@app.route('/history')
def history():
    return render_template("history.html", messages=history_messages)

@app.route('/history', methods=['GET', 'POST'])
def history_submit():
    if request.method == 'POST':
        message = request.form['message']
        
        history_messages.append({'sender': 'human', 'message': [message]})
        
        no_messages_intro = "You are a history tutor. The following message will either either ask you to clarify a question, ask you for test questions, or ask you to explain a question. Answer the question to the best of your ability and try your hardest to replicate how a real tutor would answer the quesiton."
        
        prev_messages = ""
        for i in range(1, len(history_messages)):
            prev_messages += f"Message {i} from {history_messages[i]['sender']}: {'\n'.join(history_messages[i]['message'])}\n"
        message_intro = f"You are a history tutor. The following message will either either ask you to clarify a question, ask you for test questions, or ask you to explain a question. Answer the question to the best of your ability and try your hardest to replicate how a real tutor would answer the quesiton.\nTo Clarify the Conversation, Here are the previous messages (These are both from you (The AI, and The User (The Human))):\n{prev_messages}"
        
        intro = no_messages_intro if len(history_messages) == 1 else message_intro
        print(intro)        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": intro},
                {"role": "user", "content": f"{message}"}
            ]
        )
        
        ai_response = response.choices[0].message.content
        
        ai_response = ai_response.split('\n')
        
        history_messages.append({'sender': 'ai', 'message': ai_response})      
    return redirect(url_for('history'))

@app.route('/science')
def science():
    return render_template("science.html", messages=science_messages)

@app.route('/science', methods=['GET', 'POST'])
def science_submit():
    if request.method == 'POST':
        message = request.form['message']
        
        science_messages.append({'sender': 'human', 'message': [message]})
        
        no_messages_intro = "You are a science tutor. The following message will either either ask you to clarify a question, ask you for test questions, or ask you to explain a question. Answer the question to the best of your ability and try your hardest to replicate how a real tutor would answer the quesiton."
        
        prev_messages = ""
        for i in range(1, len(science_messages)):
            prev_messages += f"Message {i} from {science_messages[i]['sender']}: {'\n'.join(science_messages[i]['message'])}\n"
        message_intro = f"You are a science tutor. The following message will either either ask you to clarify a question, ask you for test questions, or ask you to explain a question. Answer the question to the best of your ability and try your hardest to replicate how a real tutor would answer the quesiton.\nTo Clarify the Conversation, Here are the previous messages (These are both from you (The AI, and The User (The Human))):\n{prev_messages}"
        
        intro = no_messages_intro if len(science_messages) == 1 else message_intro
        print(intro)        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": intro},
                {"role": "user", "content": f"{message}"}
            ]
        )
        
        ai_response = response.choices[0].message.content
        
        ai_response = ai_response.split('\n')
        
        science_messages.append({'sender': 'ai', 'message': ai_response})
        print(ai_response)
    return redirect(url_for('science'))

if __name__ == "__main__":
    app.run(debug=True)