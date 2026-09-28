from flask import Flask
app= Flask(__name__)
@app.route("/")
def home():
    return "Hello world"
@app.route("/add/<int:a>/<int:b>")
def add(a,b):
    return f"{a}+{b}={a+b}"

if __name__=="__main__":
    app.run(debug=True)