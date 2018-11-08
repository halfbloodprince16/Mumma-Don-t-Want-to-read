from flask import Flask,render_template,url_for,request
import talkey
tts = talkey.engines.FestivalTTS()
app = Flask(__name__)

@app.route('/input', methods = ['Get', 'Post'])
def input():
         return render_template('HTML_for_Textbox.html')

@app.route('/output',methods = ['POST'])
def output():
  if request.method == 'POST':
    try:
         Text = request.form['text'] 
    finally:
    	tts.say(Text)
        return render_template('Result_for_Textbox.html', Text = Text) 




app.run(host = 'localhost', port = 8008 , debug=True)    
