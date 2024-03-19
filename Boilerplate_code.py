#Importing flask module in the project
from flask import Flask,render_template

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/activity")

#‘/’ URL is bound with first_flask function.
def first_flask():

    name = "naman pandey"
    return render_template('s.html',student_name = name)

#run the application on local server
app.run()
