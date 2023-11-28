from flask import Flask,request,render_template,jsonify,redirect,url_for

app=Flask(__name__)

@app.route('/')
def hithere():
    return render_template('flask2.html')


@app.route('/validate2', methods = ["POST","GET"] )  
def validate2():
     if request.method == 'POST':
        return redirect(url_for("success"))
        username = request.form['username']
        return jsonify({'username': username})

@app.route('/success')
def success():
     return "Success!"


if __name__ == '__main__':
    app.run(debug=True)




