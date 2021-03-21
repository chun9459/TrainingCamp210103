from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session

app = Flask(__name__) 
app.secret_key = "haohgwpejflanwiP3IRPF"

@app.route("/")
def index():       
    return render_template("HomeWork4.html")


@app.route("/siqnin", methods=["POST"])
def siqnin():
    getid = request.form["yourid"]
    getpassword = request.form["yourpassword"]
    if getid == "test" and getpassword == "test" :
        session["getid"] = getid
        session["getpassword"] = getpassword
        return redirect("/member/")
    else :
        return redirect("/error/")

@app.route("/member/")
def member(): 
    if "getid" in session:
        getid = session["getid"]
        return render_template("member.html")
    else:
        return redirect("/")

@app.route("/error/")
def error():     
    return render_template("error.html")

@app.route("/signout")
def logout():
   session.pop("getid", None)
   return redirect("/")

app.run(port=3000)
