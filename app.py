#ENGI E1006 Final Assignment#
#Melissa Emerson            #
#############################

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template('index.html')
@app.route("/assignments")
def page2():
    return render_template('page2.html')
@app.route("/classes")
def page3():
    return render_template('page3.html')

#start the server
if __name__ == "__main__":
    app.run()
    
