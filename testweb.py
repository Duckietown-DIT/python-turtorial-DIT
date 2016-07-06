from flask import flask
app =Flask
@app.route("/")
def hello():
    return "hello"

if __name__=="__main__":
