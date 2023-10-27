from flask import Flask

app=Flask(__name__) #constructor of flask

#decorator is used to tell application which URL is associated with function
@app.route('/') #when home page of webserver is opened in browser , output of hello function is rendered
def hello():
    return"Hi Devi!"

if __name__=='__main__':
    app.run() #flask application started