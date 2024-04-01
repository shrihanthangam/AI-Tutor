from flask import Flask, render_template, request, redirect, url_for
from openai import OpenAI

app = Flask(__name__)

app.static_folder = "static"

math_messages = [{'sender': 'ai', 'message': 'Hello! I am your Math AI Tutor. I will help you with anything you need by making practice questions about Math! If you don\'t get the question, just ask me to explain. Thanks!.'}]
english_messages = [{'sender': 'ai', 'message': 'Hello! I am your English AI Tutor. I will help you with anything you need by making practice questions about Math! If you don\'t get the question, just ask me to explain. Thanks!.'}]
history_messages = [{'sender': 'ai', 'message': 'Hello! I am your History AI Tutor. I will help you with anything you need by making practice questions about Math! If you don\'t get the question, just ask me to explain. Thanks!.'}]
science_messages = [{'sender': 'ai', 'message': 'Hello! I am your Science AI Tutor. I will help you with anything you need by making practice questions about Math! If you don\'t get the question, just ask me to explain. Thanks!.'}]


client = OpenAI(api_key="<APIKEY>")

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
        
        math_messages.append({'sender': 'human', 'message': message})
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": "You are a math tutor. The following message will either either ask you to clarify a question, ask you for test questions, or ask you to explain a question. Answer the question to the best of your ability and try your hardest to replicate how a real tutor would answer the quesiton."},
                {"role": "user", "content": f"{message}"}
            ]
        )
        
        ai_response = response.choices[0].message.content
        
        math_messages.append({'sender': 'ai', 'message': f'{ai_response}'})        
    return redirect(url_for('math'))


@app.route('/english')
def english():
    return render_template("english.html")

@app.route('/english', methods=['GET', 'POST'])
def english_submit():
    if request.method == 'POST':
        message = request.form['message']
        
        english_messages.append({'sender': 'human', 'message': message})
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": "You are an english tutor. The following message will either either ask you to clarify a question, ask you for test questions, or ask you to explain a question. Answer the question to the best of your ability and try your hardest to replicate how a real tutor would answer the quesiton."},
                {"role": "user", "content": f"{message}"}
            ]
        )
        
        ai_response = response.choices[0].message.content
        
        english_messages.append({'sender': 'ai', 'message': f'{ai_response}'})        
    return redirect(url_for('english'))


@app.route('/history')
def history():
    return render_template("history.html")

@app.route('/history', methods=['GET', 'POST'])
def history_submit():
    if request.method == 'POST':
        message = request.form['message']
        
        history_messages.append({'sender': 'human', 'message': message})
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": "You are an history tutor. The following message will either either ask you to clarify a question, ask you for test questions, or ask you to explain a question. Answer the question to the best of your ability and try your hardest to replicate how a real tutor would answer the quesiton."},
                {"role": "user", "content": f"{message}"}
            ]
        )
        
        ai_response = response.choices[0].message.content
        
        history_messages.append({'sender': 'ai', 'message': f'{ai_response}'})        
    return redirect(url_for('history'))

@app.route('/science')
def science():
    return render_template("science.html")

@app.route('/science', methods=['GET', 'POST'])
def science_submit():
    if request.method == 'POST':
        message = request.form['message']
        
        science_messages.append({'sender': 'human', 'message': message})
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": "You are an science tutor. The following message will either either ask you to clarify a question, ask you for test questions, or ask you to explain a question. Answer the question to the best of your ability and try your hardest to replicate how a real tutor would answer the quesiton."},
                {"role": "user", "content": f"{message}"}
            ]
        )
        
        ai_response = response.choices[0].message.content
        
        science_messages.append({'sender': 'ai', 'message': f'{ai_response}'})        
    return redirect(url_for('science'))

if __name__ == "__main__":
    app.run(debug=True)