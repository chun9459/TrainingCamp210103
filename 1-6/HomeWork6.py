from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for

# 連線 MySQL
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="website"
)
mycursor = mydb.cursor()

app = Flask(__name__)
app.secret_key = "haohgwpejflanwiP3IRP!F" 

# 首頁
@app.route("/")
def index():       
    return render_template("HomeWork6.html")

# 註冊
@app.route("/signup", methods=["POST"])
def signup():
    getname = request.form["name"]
    getusername = request.form["username"]
    getpassword = request.form["password"]
    if not getname.strip() or not getusername.strip() or not getpassword.strip():
        return redirect(url_for("error", message = "資料不得為空"))
    else:
        mycursor.execute("SELECT * FROM user WHERE username = '"+getusername+"'")
        myresult = mycursor.fetchone()
        if myresult == None:
            mycursor.execute("INSERT INTO user(name, username, password) VALUES ('"+getname+"','"+getusername+"','"+getpassword+"')")
            mydb.commit()
            return redirect("/")
        else:
            return redirect(url_for("error", message = "帳號已經被註冊"))       

# 登入
@app.route("/signin", methods=["POST"])
def signin():
    getusername = request.form["username"]
    getpassword = request.form["password"]
    mycursor.execute("SELECT user.username, user.password FROM user WHERE username = '"+getusername+"'")
    myresult = mycursor.fetchone()
    if getusername == myresult[0] and getpassword == myresult[1] :
        session["getusername"] = getusername
        session["getpassword"] = getpassword
        return redirect("/member/")
    else :
        return redirect(url_for("error", message = "帳號或密碼輸入錯誤"))

# 會員頁
@app.route("/member/")
def member(): 
    if "getusername" in session:
        getusername = session["getusername"]
        mycursor.execute("SELECT user.name FROM user WHERE username = '"+getusername+"'")
        myresult = mycursor.fetchone()
        return render_template("member.html", getname = myresult[0])
    else:
        return redirect("/")

# 錯誤頁
@app.route("/error/")
def error():
    message = request.args.get("message","")
    return render_template("error.html", message = message )

# 登出
@app.route("/signout")
def signout():
   session.pop("getusername", None)
   return redirect("/")

app.run(port=3000)
