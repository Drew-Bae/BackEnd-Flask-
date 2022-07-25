from distutils.log import debug
from flask import Flask, render_template
app = Flask (__name__)

@app.route ('/')
def index ():
    name="Drew"
    name_list = ['D','r','e','w']
    return render_template('exercise2.html',my_name=name,mylist=name_list)

if __name__ == '__main__':
    app.run(debug=True)