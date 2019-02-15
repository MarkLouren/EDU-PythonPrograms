#First Flask application

from flask import Flask

#creating an object  Flask using unique name
app =Flask(__name__)

@app.route('/') #creating a root for home app -http://google.com/
#asign a method to it. it has return something
def home():
    return "hello world"
#run application 
app.run(port=5000)
