from flask import Flask
from flask import render_template, request, redirect, url_for, send_from_directory
from datetime import datetime
import time

app = Flask(__name__)

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route("/countdown")
def countdown():

    launchTime = datetime(2022, 6, 1)
    currentTime = datetime.now()
    diff = launchTime - currentTime
    numberOfDays = diff.days

   return render_template(
      "countdown.html",
      time=numberOfDays
   )
    
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello received from name=%s' % name)    
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))

if __name__ == '__main__':
  app.run()      
