from flask import Flask,render_template,url_for,request

app=Flask(__name__)

@app.route('/home')
def func1():
    return render_template('flask.html')

if __name__=='__main__':
     app.run(debug=True)
       


