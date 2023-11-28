from flask import Flask,redirect,url_for,request,render_template

app=Flask(__name__)

@app.route('/hi')
def func1():
    return render_template('flask.html')

@app.route('/validate', methods = ["GET"] )  
def validate():  
    if request.method == 'GET':
            if(request.args.get('fname') == 'devi'):
                 return redirect(url_for("success"))

@app.route('/success')
def success():
     return "Success!"

if __name__=='__main__':
     app.run(debug=True)