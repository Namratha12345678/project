from flask import *
from cascon import *
app=Flask(__name__)

session=cascon()
app.secret_key="nams08"

@app.route("/lapins",methods=["GET","POST"]) #Route decorator
def lapins():
    global session
    if request.method=="GET":
        return render_template("lapins.html") 
    else:
        lapname=request.form["lapname"]
        lapos=request.form["lapos"]
        lapprice=int(request.form["lapprice"])
        lapprocessor=request.form["lapprocessor"]
        lapram=request.form["lapram"]
        lapid=request.form["lapid"]
        session.execute("""insert into laptop(lapname,lapos,lapprice,lapprocessor,lapram,lapid)
         values(%(lapname)s,%(lapos)s,%(lapprice)s,%(lapprocessor)s,%(lapram)s),%(lapid)s)""",
        {"lapname":lapname,"lapos":lapos,"lapprice":lapprice,"lapprocessor":lapprocessor,"lapram":lapram,"lapid":lapid});
    return "Insertion successful"


@app.route("/lapupd",methods=["GET","POST"]) #Route decorator
def lapupd():
    global session
    if request.method=="GET":
        return render_template("lapupd.html")
    else:
        lname=request.form["lname"]
        los=request.form["los"]
        lprice=int(request.form["lprice"])
        lprocessor=request.form["lprocessor"]
        lram=request.form["lram"]
        session.execute("""
        UPDATE laptop SET los=%(los)s,lprice=%(lprice)s,lprocessor=%(lprocessor)s,lram=%(lram)s
         WHERE lname=%(lname)s""",
        {"lname":lname,"los":los,"lprice":lprice,"lprocessor":lprocessor,"lram":lram});
        return "Updation successful"


@app.route("/lapdel",methods=["GET","POST"])
def lapdel():
    global session
    if request.method=="GET":
        return render_template("lapdel.html")
    else:
        lname=(request.form["lname"])
        session.execute("""
        DELETE FROM laptop where lname=%(lname)s
        """,{"lname":lname});
        return "Deletion successful"

@app.route("/lapdis",methods=["GET","POST"])
def lapdis():
    global session
    rows=session.execute("select * from laptop")
    r=[]
    for row in rows:
         r.append([row.lname,row.los,row.lprice,row.lprocessor,row.lram])
    rt=tuple(r)
    return render_template("lapdis.html",rt=rt)


@app.route("/lapsearch",methods=["GET","POST"])
def lapsearch():
    
    if request.method=="GET":
     return render_template("lapsearch.html")
    else:
        lname=request.form['lname']
        rows=session.execute("select * from laptop where lname='"+lname+"'")
        r=[]
        for row in rows:
            r.append([row.lname,row.los,row.lprice,row.lprocessor,row.lram])
        rt=tuple(r)
        return render_template("lapdis.html",rt=rt)


@app.route("/laptop")
def laptop():
    return render_template("laptop.html")


if __name__=="__main__":
   app.run(debug=True,port=5000)

  