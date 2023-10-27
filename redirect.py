from flask import Flask,redirect,url_for,request

app=Flask(__name__)

@app.route('/redirect2')
def func1():
    return redirect(url_for('flask.html'))

if __name__=='__main__':
     app.run(debug=True)