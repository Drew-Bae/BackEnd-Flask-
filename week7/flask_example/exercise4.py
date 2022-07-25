from distutils.log import debug
from flask import Flask, render_template
app = Flask (__name__)

@app.route ('/')
def index ():
    days= ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return render_template('exercise4.html', days=days)

if __name__ == '__main__':
    app.run(debug=True)