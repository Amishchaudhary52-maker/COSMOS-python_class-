from flask import Flask, request
from flask import render_template
app= Flask(__name__)
@app.route("/")
def home():
    return "Hello world"
@app.route("/add/<int:a>/<int:b>")
def add(a,b):
    return f"{a}+{b}={a+b}"

@app.route("/template")
def templateCall():
    return render_template("index.html",name="Amish")

@app.route("/newtemplate")
def newtemplate():
    return render_template("page.html")
@app.route("/submit", methods=["GET","POST"])
def submit():
    if request.method=="POST":
        name=request.form["name"]
        return f"Hello,{name}"
    return render_template("form.html")
if __name__=="__main__":
    app.run(debug=True)