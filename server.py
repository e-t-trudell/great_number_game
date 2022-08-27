from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'secret0192837465key'

@app.route('/')
def index():
    # no number in session create one
    if 'start' not in session:
        session['start']= random.randint(1,100)
    # print the 'session start' outside the for loop
    print('Start=', session['start'])
    return render_template("index.html")

# this method may need a methods = ['POST'] to return data from the form?
@app.route('/answer', methods=['POST'])
def answerme():
    # enter int before the request.form to return an interger value
    session['answer'] = int(request.form['answer'])
    print('Answer=', session['answer'])
    return redirect("/")

@app.route('/play_again')
def playagain():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port= 5002)