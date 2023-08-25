# Flask Packages

from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect,
    url_for,
    session,
    make_response,
    jsonify,
)

# from flask_mysqldb import MySQL

# from flask_cors import CORS

# Database Connectivity Driver

import mysql.connector

# Random String Generator(Otp Code)

import random

# Showing Errors

import traceback

# Locate Disc Address

import os
from werkzeug.utils import secure_filename

# Flask App Initialization

app = Flask(__name__)
# CORS(app)

# Image Uplaod Folder Destination

app.secret_key = "food"
# app.config["MYSQL_HOST"] = "localhost"
# app.config["MYSQL_USER"] = "root"
# app.config["MYSQL_PASSWORD"] = "Imman@123"
# app.config["MYSQL_DB"] = "foodwastage"
# app.config["CORS_HEADERS"] = "Content-Type"
UPLOAD_FOLDER = "static/upload"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
UPLOAD_FOLDER1 = "static/upload1"
app.config["UPLOAD_FOLDER1"] = UPLOAD_FOLDER1

# mysql = MySQL(app)


# Make connection between php admin database and flask app


def getconnection():
    return mysql.connector.connect(
        user="root", database="foodwastage", password="Imman@123"
    )
    # return mysql.connection


# WELCOME PAGE CODE


@app.route("/", methods=["POST", "GET"])  # Url Decalaration
def startup_page():  # Url Function
    return render_template("welcomepage.html")  # Response as a template


# LOGIN PAGE CODE
@app.route("/loginentry", methods=["POST", "GET"])  # Url Decalaration
def loginentry():  # Url Function
    return render_template("loginentry.html")  # Response as a template


# lOGIN DETAILS VERIFICATION WITH DATABASE


@app.route("/loginauth", methods=["POST", "GET"])  # Url Decalaration
def login_entry():  # Url Function
    try:
        connection = getconnection()
        cur = connection.cursor()
        em = request.args["email"]
        # ps = request.args["password2"]
        session["current_email"] = em  # Maintaining sessions on server

        cur.execute(
            "SELECT 'User' AS type,email FROM signupentry WHERE email = '"
            + em
            + "' UNION SELECT 'Community' AS type, cemail FROM communitysignup WHERE cemail = '"
            + em
            + "'"
        )  #   Query Execution
        result = cur.fetchone()
        print(result)  # Print the Statement
        if result is None:
            return render_template("loginentry.html")
        else:
            if result[0] == "User":
                return redirect("landingpage")
            else:
                return redirect("landingpage1")
    except Exception as e:
        print(e)
        return render_template("loginentry.html")  # Response as a template


# SIGNUP ENTRY PAGE


@app.route("/signupentry")  # Url Decalaration
def signupentry():  # Url Function
    return render_template("signupentry.html")  # Response as a template


# SIGNUP SAVE


@app.route("/signupsave", methods=["POST", "GET"])
def signup_save():
    if request.method == "POST":
        file = request.files["file"]
        file1 = request.files["file1"]
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        if file1:
            filename1 = secure_filename(file1.filename)
            file1.save(os.path.join(app.config["UPLOAD_FOLDER1"], filename1))

        uphoto = file.filename
        fname = request.form["fname"]
        lname = request.form["lname"]
        phno = request.form["phno"]
        email = request.form["email"]
        address = request.form["address"]
        pname = request.form["pname"]
        pnumber = request.form["pnumber"]
        pfile = file1.filename
        password2 = request.form["password2"]
        con = getconnection()
        cur = con.cursor()

        cur.execute(
            "SELECT 'User' AS type,email FROM signupentry WHERE email = '"
            + email
            + "' UNION SELECT 'Community' AS type, cemail FROM communitysignup WHERE cemail = '"
            + email
            + "'"
        )  #   Query Execution
        email1 = cur.fetchone()
        print(email1)
        if email1 is None:
            cur.execute(
                "insert into `signupentry`(`fname`,`lname`,`uphoto`,`phno`,`email`,`address`,`pname`,`pnumber`,`pfile`,`password`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                    fname,
                    lname,
                    uphoto,
                    phno,
                    email,
                    address,
                    pname,
                    pnumber,
                    pfile,
                    password2,
                ),
            )
            con.commit()
            return render_template("loginentry.html")
        return render_template("signupentry.html")


# COMMUNITY ENTRY PAGE


@app.route("/communitysignup")  # Url Decalaration
def communitysignup():  # Url Function
    return render_template("communitysignup.html")  # Response as a template


# COMMUNITY SAVE


@app.route("/communitysignupsave", methods=["POST", "GET"])
def community_signup_save():
    if request.method == "POST":
        file = request.files["file"]
        file1 = request.files["file1"]
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        if file1:
            filename1 = secure_filename(file1.filename)
            file1.save(os.path.join(app.config["UPLOAD_FOLDER1"], filename1))

        cuphoto = file.filename
        orgname = request.form["orgname"]
        comname = request.form["comname"]
        ctype = request.form["cphno"]
        cemail = request.form["cemail"]
        cphno = request.form["cphno"]
        caddress = request.form["caddress"]
        regcertphoto = file1.filename
        regcertnumber = request.form["regcertnumber"]
        cpassword = request.form["password2"]
        con = getconnection()
        cur = con.cursor()
        cur.execute(
            "SELECT 'User' AS type,email FROM signupentry WHERE email = '"
            + cemail
            + "' UNION SELECT 'Community' AS type, cemail FROM communitysignup WHERE cemail = '"
            + cemail
            + "'"
        )  #   Query Execution
        email1 = cur.fetchone()
        print(email1)

        if email1 is None:
            cur.execute(
                "insert into `communitysignup`(`cuphoto`,`orgname`,`comname`,`ctype`,`cemail`,`cphno`,`caddress`,`regcertphoto`,`regcertnumber`,`cpassword`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                    cuphoto,
                    orgname,
                    comname,
                    ctype,
                    cemail,
                    cphno,
                    caddress,
                    regcertphoto,
                    regcertnumber,
                    cpassword,
                ),
            )
            con.commit()
            return render_template("loginentry.html")
        return render_template("communitysignup.html")


# MAINPAGE


@app.route("/landingpage")  # Url Decalaration
def landingpage():  # Url Function
    con = getconnection()
    cur = con.cursor()
    cur.execute(
        "Select count(fid) FROM donor where email!=%s", (session["current_email"],)
    )  # Query Execution
    result = cur.fetchone()
    print(result)  # Print the Statement
    # cur.execute(
    #     "Select count(o.order_id),d.*,o.order_id from donor as d JOIN orders as o on d.fid = o.food_id where o.receiver_id=(SELECT uid from signupentry WHERE email=%s)",
    #     (session["current_email"],),
    # )  # Query Execution
    # result1 = cur.fetchone()
    # print(result1)  # Print the Statement
    cur.execute(
        "Select * FROM signupentry where email=%s", (session["current_email"],)
    )  # Query Execution
    result2 = cur.fetchone()
    print(result2)  # Print the Statement
    cur.execute(
        "Select d.fname,d.lname,r.fname,r.lname from orders as o join signupentry as d on d.uid=o.donor_id join signupentry as r on r.uid=o.receiver_id where o.is_received='Yes'"
    )  # Query Execution
    result3 = cur.fetchone()
    print(result3)  # Print the Statement
    return render_template(
        "landingpage1.html",
        data=result[0],
        # data1=result1[0],
        profile=result2[1] + " " + result2[2],
        # image=result2[3],
        dname=result3[0] + " " + result3[1],
        rname=result3[2] + " " + result3[3],
    )  # Response as a template


@app.route("/landingpage1")  # Url Decalaration
def landingpage1():  # Url Function
    con = getconnection()
    cur = con.cursor()
    cur.execute(
        "Select * FROM communitysignup where cemail=%s", (session["current_email"],)
    )  # Query Execution
    data = cur.fetchone()
    print(data)  # Print the Statement
    cur.execute(
        "Select cs.orgname,r.fname,r.lname from orders as o join communitysignup as cs on cs.cuid=o.donor_id join signupentry as r on r.uid=o.receiver_id where o.is_received='Yes'"
    )  # Query Execution
    result3 = cur.fetchone()
    print(result3)  # Print the Statement
    return render_template(
        "landingpage2.html",
        profile=data[2],
        image=data[1],
        c_dname=result3[0],
        c_rname=result3[1] + " " + result3[2],
    )  # Response as a template


# CONTACT PAGE


@app.route("/contact", methods=["POST"])  # Url Declaration
def contact():  # Url Function
    name = request.form["name"]  # Getting value from request object
    email = request.form["email"]  # Getting value from request object
    msg = request.form["msg"]  # Getting value from request object
    phno = request.form["phno"]  # Getting value from request object
    con = getconnection()
    cur = con.cursor()
    cur.execute(
        "INSERT INTO `feedback` (`name`, `email`, `msg`,`phno`) VALUES (%s, %s, %s, %s)",
        (name, email, msg, phno),
    )  # Query Execution
    con.commit()  # Save the current connection data
    cur.close()  # Close the cursor object
    return redirect(url_for("landingpage"))  # Response as a redirect


# DONOR FOOD ENTRY PAGE


@app.route("/donorentry", methods=["POST", "GET"])  # Url Decalaration
def donor_entry():  # Url Function
    con = getconnection()
    cur = con.cursor()
    cur.execute(
        "select * from signupentry where email=%s", (session["current_email"],)
    )  # Query Execution
    result = cur.fetchone()  # Retrieving Table data from database
    print(result)  # Print the Statement
    cur.close()  # Close the cursor object
    return render_template(
        "donorentry.html",
        id=result[0],
        name=result[1] + " " + result[2],
        email=result[5],
        phno=result[4],
    )  # Response as a template


# COMMUNITY ENTRY PAGE


@app.route("/communityentry", methods=["POST", "GET"])  # Url Decalaration
def community_entry():  # Url Function
    con = getconnection()
    cur = con.cursor()
    cur.execute(
        "select * from communitysignup where cemail=%s", (session["current_email"],)
    )  # Query Execution
    result = cur.fetchone()  # Retrieving Table data from database
    print(result)  # Print the Statement
    cur.close()  # Close the cursor object
    return render_template(
        "communityentry.html",
        cid=result[0],
        cname=result[2],
        cemail=result[5],
        cphno=result[4],
    )  # Response as a template


# DONOR SAVE


@app.route("/donorsave", methods=["POST", "GET"])  # Url Decalaration
def donor_save():  # Url Function
    if request.method == "POST":  # Checking methos of Request
        file = request.files["file"]
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        uid = request.form["uid"]  # Getting value from request object
        uname = request.form["uname"]  # Getting value from request object
        email = request.form["email"]  # Getting value from request object
        phno = request.form["phno"]  # Getting value from request object
        fdname = request.form["fdname"]  # Getting value from request object
        fdtype = request.form["fdtype"]  # Getting value from request object
        fdq = request.form["fdq"]  # Getting value from request object
        fd = request.form["fd"]  # Getting value from request object
        address = request.form["address"]  # Getting value from request object
        fphoto = file.filename  # Getting file from request object
        frdate = request.form["frdate"]  # Getting value from request object
        exdate = request.form["exdate"]  # Getting value from request object
        frtime = request.form["frtime"]  # Getting value from request object
        extime = request.form["extime"]  # Getting value from request object

        print("imman   ", fdq, fd)  # Print the Statement

        con = getconnection()
        cur = con.cursor()
        cur.execute(
            "INSERT INTO `donor` (`uid`, `uname`, `email`,`phno`,`fphoto`,`fdname`,`fdtype`,`fdq`,`address`,`frdate`,`exdate`,`frtime`,`extime`,`orderconform`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (
                uid,
                uname,
                email,
                phno,
                fphoto,
                fdname,
                fdtype,
                fd if fdq == "custom" else fdq,
                address,
                frdate,
                exdate,
                frtime,
                extime,
                "pending",
            ),
        )  # Query Execution
        con.commit()  # Save the current connection data
        return redirect(url_for("landingpage"))  # Response as a redirect


# COMMUNITY ENTRY SAVE


@app.route("/communityentrysave", methods=["POST", "GET"])  # Url Decalaration
def community_entry_save():  # Url Function
    if request.method == "POST":  # Checking methos of Request
        file = request.files["file"]
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        cuid = request.form["cuid"]  # Getting value from request object
        cuname = request.form["cuname"]  # Getting value from request object
        cemail = request.form["cemail"]  # Getting value from request object
        cphno = request.form["cphno"]  # Getting value from request object
        cfdname = request.form["cfdname"]  # Getting value from request object
        cfdtype = request.form["cfdtype"]  # Getting value from request object
        cfdq = request.form["cfdq"]  # Getting value from request object
        cfd = request.form["cfd"]  # Getting value from request object
        caddress = request.form["caddress"]  # Getting value from request object
        cphoto = file.filename  # Getting file from request object
        cfrdate = request.form["cfrdate"]  # Getting value from request object
        cexdate = request.form["cexdate"]  # Getting value from request object
        cfrtime = request.form["cfrtime"]  # Getting value from request object
        cextime = request.form["cextime"]  # Getting value from request object

        print("imman   ", cfdq, cfd)  # Print the Statement

        con = getconnection()
        cur = con.cursor()
        cur.execute(
            "INSERT INTO `communityentry` (`cuid`, `cuname`, `cemail`,`cphno`,`cfdname`,`cfdtype`,`cfdq`,`caddress`,`cphoto`,`cfrdate`,`cexdate`,`cfrtime`,`cextime`,`corderconform`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (
                cuid,
                cuname,
                cemail,
                cphno,
                cfdname,
                cfdtype,
                cfd if cfdq == "custom" else cfdq,
                caddress,
                cphoto,
                cfrdate,
                cexdate,
                cfrtime,
                cextime,
                "pending",
            ),
        )  # Query Execution
        con.commit()  # Save the current connection data
        return redirect(url_for("landingpage1"))  # Response as a redirect


# RECEIVER PAGE


@app.route("/receiver")  # Url Decalaration
def receiver():  # Url Function
    con = getconnection()
    cur = con.cursor()
    cur.execute(
        "select d.*,s.* from donor as d JOIN signupentry as s on s.uid = d.uid where d.email!=%s",
        (session["current_email"],),
    )  # Query Execution
    result = cur.fetchall()
    print(result)  # Print the Statement
    cur.execute(
        "select ce.*,cs.* from communityentry as ce JOIN communitysignup as cs on cs.cuid = ce.cuid where ce.cemail!=%s",
        (session["current_email"],),
    )  # Query Execution
    result1 = cur.fetchall()
    print(result1)  # Print the Statement
    cur.close()  # Close the cursor object
    return render_template(
        "receiver.html", data=result, data1=result1
    )  # Response as a template


# REQUEST PAGE


@app.route("/requestpage")  # Url Decalaration
def requestpage():  # Url Function
    con = getconnection()
    cur = con.cursor()
    cur.execute(
        "select s.*,d.*,o.order_id from donor as d JOIN orders as o on d.fid = o.food_id join signupentry as s on s.uid=o.receiver_id where o.donor_id=(SELECT uid from signupentry WHERE email=%s) and o.status='Pending'",
        (session["current_email"],),
    )  # Query Execution
    result = cur.fetchall()
    print(result)  # Print the Statement
    cur.close()  # Close the cursor object
    return render_template("requestpage.html", data=result)  # Response as a template


# REQUEST PAGE


@app.route("/requestpage1")  # Url Decalaration
def request_page1():  # Url Function
    con = getconnection()
    cur = con.cursor()
    cur.execute(
        "select s.*,ce.*,o.order_id from communityentry as ce JOIN orders as o on ce.cfid = o.food_id join signupentry as s on s.uid=o.receiver_id where o.donor_id=(SELECT cuid from communitysignup WHERE cemail=%s) and o.status='Pending'",
        (session["current_email"],),
    )  # Query Execution
    result = cur.fetchall()
    print(result)  # Print the Statement
    cur.close()  # Close the cursor object
    return render_template("requestpage1.html", data=result)  # Response as a template


# ACCEPT ORDER IN REQUEST PAGE


@app.route("/acceptorder")  # Url Decalaration
def acceptorder():  # Url Function
    oid = request.args.get("oid")  # Getting value from request object
    otp = random.randint(1000, 9999)  # Generate secret code
    con = getconnection()
    cur = con.cursor()
    cur.execute(
        "UPDATE orders AS o "
        "INNER JOIN (SELECT food_id FROM orders WHERE order_id = %s) AS subquery "
        "ON o.food_id = subquery.food_id "
        "SET o.status = CASE WHEN o.order_id = %s THEN 'Accepted' ELSE 'Rejected' END, "
        "o.otp = %s",
        (
            oid,
            oid,
            otp,
        ),
    )  # Query Execution
    con.commit()  # Save the current connection data
    cur.close()  # Close the cursor object
    return render_template("requestpage.html")  # Response as a template


# ACCEPT ORDER IN REQUEST PAGE


@app.route("/acceptorder1")  # Url Decalaration
def acceptorder1():  # Url Function
    oid = request.args.get("oid")  # Getting value from request object
    otp = random.randint(1000, 9999)  # Generate secret code
    con = getconnection()
    cur = con.cursor()
    cur.execute(
        "UPDATE orders AS o "
        "INNER JOIN (SELECT food_id FROM orders WHERE order_id = %s) AS subquery "
        "ON o.food_id = subquery.food_id "
        "SET o.status = CASE WHEN o.order_id = %s THEN 'Accepted' ELSE 'Rejected' END, "
        "o.otp = %s",
        (
            oid,
            oid,
            otp,
        ),
    )  # Query Execution
    con.commit()  # Save the current connection data
    print(otp)
    print(oid)
    cur.close()  # Close the cursor object
    return render_template("requestpage1.html")  # Response as a template


# REJECT ORDER IN COMMUNITY REQUEST PAGE


@app.route("/rejectorder")  # Url Decalaration
def rejectorder():  # Url Function
    oid = request.args.get("oid")  # Getting value from request object
    con = getconnection()
    cur = con.cursor()
    cur.execute(
        "update orders set status='Rejected' where order_id=%s", (oid,)
    )  # Query Execution
    con.commit()  # Save the current connection data
    cur.close()  # Close the cursor object
    return redirect(url_for("requestpage"))  # Response as a redirect


# REJECT ORDER IN COMMUNITY REQUEST PAGE


@app.route("/rejectorder1")  # Url Decalaration
def rejectorder1():  # Url Function
    oid = request.args.get("oid")  # Getting value from request object
    con = getconnection()
    cur = con.cursor()
    cur.execute(
        "update orders set status='Rejected' where order_id=%s", (oid,)
    )  # Query Execution
    con.commit()  # Save the current connection data
    cur.close()  # Close the cursor object
    return redirect(url_for("requestpage1"))  # Response as a redirect


# ADD REQUEST IN ORDER PAGE


@app.route("/addrequest", methods=["POST"])  # Url Decalaration
def add_request():  # Url Function
    did = request.form["did"]  # Getting value from request object
    fid = request.form["fid"]  # Getting value from request object
    rid = request.form["rid"]  # Getting value from request object
    con = getconnection()
    cur = con.cursor()
    cur.execute(
        "INSERT INTO `orders` (`donor_id`, `food_id`, `receiver_id`) VALUES (%s, %s, %s)",
        (did, fid, rid),
    )  # Query Execution
    con.commit()  # Save the current connection data
    cur.close()  # Close the cursor object
    return redirect(url_for("myorder"))  # Response as a redirect


# ADD REQUEST IN COMMUNITYORDER PAGE


@app.route("/addrequest1", methods=["POST"])  # Url Decalaration
def add_request1():  # Url Function
    cd_did = request.form["cd_did"]  # Getting value from request object
    cd_fid = request.form["cd_fid"]  # Getting value from request object
    r_uid = request.form["r_uid"]  # Getting value from request object
    con = getconnection()
    cur = con.cursor()
    cur.execute(
        "INSERT INTO `orders` (`donor_id`, `food_id`, `receiver_id`) VALUES (%s, %s, %s)",
        (cd_did, cd_fid, r_uid),
    )  # Query Execution
    con.commit()  # Save the current connection data
    cur.close()  # Close the cursor object
    return redirect(url_for("myorder"))  # Response as a redirect


# ORDER PAGE


@app.route("/myorder")  # Url Decalaration
def myorder():  # Url Function
    con = getconnection()
    cur = con.cursor()
    cur.execute(
        "select d.*,o.order_id,o.status,s.*,o.otp from orders as o JOIN donor as d on o.food_id=d.fid join signupentry as s on o.donor_id = s.uid where o.receiver_id=(SELECT uid from signupentry WHERE email=%s)",
        (session["current_email"],),
    )  # Query Execution
    result = cur.fetchall()
    print(result)  # Print the Statement
    cur.execute(
        "select ce.*,o.order_id,o.status,cs.*,o.otp from orders as o JOIN communityentry as ce on o.food_id=ce.cfid join communitysignup as cs on o.donor_id = cs.cuid where o.receiver_id=(SELECT uid from signupentry WHERE email=%s)",
        (session["current_email"],),
    )  # Query Execution
    result1 = cur.fetchall()
    print(result1)  # Print the Statement
    cur.close()  # Close the cursor object
    return render_template(
        "myorder.html", data=result, data1=result1
    )  # Response as a template


# CANCEL ORDER IN ORDER PAGE


@app.route("/cancelorder")  # Url Decalaration
def cancelorder():  # Url Function
    oid = request.args.get("oid")  # Getting value from request object
    con = getconnection()
    cur = con.cursor()
    cur.execute("delete from orders where order_id=%s", (oid,))  # Query Execution
    con.commit()
    result = cur.fetchone()
    print(result)  # Print the Statement
    cur.close()  # Close the cursor object
    return redirect(url_for("myorder"))  # Response as a redirect


# COMMUNTIY CANCEL ORDER IN ORDER PAGE


@app.route("/cancelorder1")  # Url Decalaration
def cancelorder1():  # Url Function
    oid = request.args.get("oid")  # Getting value from request object
    con = getconnection()
    cur = con.cursor()
    cur.execute("delete from orders where order_id=%s", (oid,))  # Query Execution
    con.commit()
    result = cur.fetchone()
    print(result)  # Print the Statement
    cur.close()  # Close the cursor object
    return redirect(url_for("myorder"))  # Response as a redirect


# RESPONSE PAGE


@app.route("/response")  # Url Decalaration
def response():  # Url Function
    msg = request.args.get("msg")  # Getting value from request object
    con = getconnection()
    cur = con.cursor()
    cur.execute(
        "select s.*,d.*,o.order_id,o.otp from donor as d JOIN orders as o on d.fid = o.food_id join signupentry as s on s.uid=o.receiver_id where o.donor_id=(SELECT uid from signupentry WHERE email=%s) and o.status='Accepted'",
        (session["current_email"],),
    )  # Query Execution

    result = cur.fetchall()
    print(result)  # Print the Statement
    cur.close()  # Close the cursor object
    return render_template(
        "response.html", data=result, msg=msg
    )  # Response as a template


# RESPONSE COMMUNITY PAGE


@app.route("/response1")  # Url Decalaration
def response1():  # Url Function
    msg = request.args.get("msg")  # Getting value from request object
    con = getconnection()
    cur = con.cursor()
    cur.execute(
        "select s.*,ce.*,o.order_id,o.otp from communityentry as ce JOIN orders as o on ce.cfid = o.food_id join signupentry as s on s.uid=o.receiver_id where o.donor_id=(SELECT cuid from communitysignup WHERE cemail=%s) and o.status='Accepted'",
        (session["current_email"],),
    )  # Query Execution
    result = cur.fetchall()
    print(result)  # Print the Statement
    cur.close()  # Close the cursor object
    return render_template(
        "response1.html", data=result, msg=msg
    )  # Response as a template


# OTP VERIFICATION IN RESPONSE PAGE


@app.route("/otpverification", methods=["POST"])  # Url Decalaration
def otp_verification():  # Url Function
    msg = None
    oid = request.form["oid"]  # Getting value from request object
    otp = request.form["otp"]  # Getting value from request object
    con = getconnection()
    cur = con.cursor()
    cur.execute("select otp from orders where order_id=%s", (oid,))  # Query Execution

    result = cur.fetchone()
    print(result)
    if result[0] == otp:
        cur.execute("update orders set is_received='Yes'")  # Query Execution
        con.commit()  # Save the current connection data
        msg = "Thanks for your donation...!!!"
    else:
        msg = "Secret code was wrong??"
    print(result)  # Print the Statement
    cur.close()  # Close the cursor object

    return redirect(url_for("response", msg=msg))  # Response as a redirect


# OTP VERIFICATION IN COMMUNITY RESPONSE PAGE


@app.route("/otpverification1", methods=["POST"])  # Url Decalaration
def otp_verification1():  # Url Function
    msg = None
    oid = request.form["oid"]  # Getting value from request object
    otp = request.form["otp"]  # Getting value from request object
    con = getconnection()
    cur = con.cursor()
    cur.execute("select otp from orders where order_id=%s", (oid,))  # Query Execution

    result = cur.fetchone()
    if result[0] == otp:
        cur.execute("update orders set is_received='Yes'")  # Query Execution
        con.commit()  # Save the current connection data
        msg = "Thanks for your donation...!!!"
    else:
        msg = "Secret code was wrong??"
    print(result)  # Print the Statement
    cur.close()  # Close the cursor object

    return redirect(url_for("response1", msg=msg))  # Response as a redirect


# USER FOOD_TRACK1 PAGE


@app.route("/sharelocation")  # Url Decalaration
def share_location():  # Url Function
    fid = request.args.get("fid")  # Getting value from request object
    return render_template("food_track1.html", fid=fid)  # Response as a template


# DONOR SHARE LOCATION TO DATABASE


@app.route("/dstorelocation")  # Url Decalaration
def d_store_location():  # Url Function
    try:
        fid = request.args.get("fid")  # Getting value from request object
        lat = request.args.get("lat")  # Getting value from request object
        lng = request.args.get("lng")  # Getting value from request object
        acc = request.args.get("acc")  # Getting value from request object
        print(fid, lat, lng)  # Print the statement
        con = getconnection()
        cur = con.cursor()
        cur.execute(
            "select * from foodtrack where food_id=%s", (fid,)
        )  # Query Execution
        flag = cur.fetchone()
        if flag is None:
            cur.execute(
                "INSERT INTO `foodtrack`(`food_id`, `longitude`, `latitude`,`accuracy`) VALUES (%s,%s,%s,%s)",
                (
                    fid,
                    lat,
                    lng,
                    acc,
                ),
            )  # Query Execution
            con.commit()  # Save the current connection data
        else:
            cur.execute(
                "UPDATE `foodtrack` SET `longitude`=%s,`latitude`=%s,`accuracy`=%s WHERE `food_id`=%s",
                (
                    lat,
                    lng,
                    acc,
                    fid,
                ),
            )  # Query Execution
            con.commit()  # Save the current connection data
        return make_response(
            jsonify({"success": True}), 200
        )  # Making response as a json object
    except Exception:
        traceback.print_exc()
        return make_response(
            jsonify({"success": False}), 500
        )  # Making response as a json object


# FOOD_TRACK2 PAGE


@app.route("/sharelocation1")  # Url Decalaration
def share_location1():  # Url Function
    fid = request.args.get("fid")  # Getting value from request object
    return render_template("food_track2.html", fid=fid)  # Response as a template


# RECEIVER FOOD TRACK LOCATION


@app.route("/rtracklocation")  # Url Decalaration
def r_track_location():  # Url Function
    try:
        fid = request.args.get("fid")  # Getting value from request object
        print(fid)  # Print the statement
        con = getconnection()
        cur = con.cursor()
        cur.execute(
            "select * from foodtrack where food_id=%s", (fid,)
        )  # Query Execution
        current_location = cur.fetchone()
        return make_response(
            jsonify({"current_location": current_location, "success": True}), 200
        )  # Making response as a json object
    except Exception:
        traceback.print_exc()  # Print the current exception
        return make_response(
            jsonify({"success": False}), 500
        )  # Making response as a json object


# COMMUNITY FOOD_TRACK1 PAGE


@app.route("/c_sharelocation")  # Url Decalaration
def c_share_location():  # Url Function
    fid = request.args.get("fid")  # Getting value from request object
    return render_template("cfood_track1.html", fid=fid)  # Response as a template


# DONOR SHARE LOCATION TO DATABASE


@app.route("/c_dstorelocation")  # Url Decalaration
def c_d_store_location():  # Url Function
    try:
        fid = request.args.get("fid")  # Getting value from request object
        lat = request.args.get("lat")  # Getting value from request object
        lng = request.args.get("lng")  # Getting value from request object
        acc = request.args.get("acc")  # Getting value from request object
        print(fid, lat, lng)  # Print the statement
        con = getconnection()
        cur = con.cursor()
        cur.execute(
            "select * from foodtrack where food_id=%s", (fid,)
        )  # Query Execution
        flag = cur.fetchone()
        if flag is None:
            cur.execute(
                "INSERT INTO `foodtrack`(`food_id`, `longitude`, `latitude`,`accuracy`) VALUES (%s,%s,%s,%s)",
                (
                    fid,
                    lat,
                    lng,
                    acc,
                ),
            )  # Query Execution
            con.commit()  # Save the current connection data
        else:
            cur.execute(
                "UPDATE `foodtrack` SET `longitude`=%s,`latitude`=%s,`accuracy`=%s WHERE `food_id`=%s",
                (
                    lat,
                    lng,
                    acc,
                    fid,
                ),
            )  # Query Execution
            con.commit()  # Save the current connection data
        return make_response(
            jsonify({"success": True}), 200
        )  # Making response as a json object
    except Exception:
        traceback.print_exc()
        return make_response(
            jsonify({"success": False}), 500
        )  # Making response as a json object


# FOOD_TRACK2 PAGE


@app.route("/c_sharelocation1")  # Url Decalaration
def c_share_location1():  # Url Function
    fid = request.args.get("fid")  # Getting value from request object
    return render_template("cfood_track2.html", fid=fid)  # Response as a template


# RECEIVER FOOD TRACK LOCATION


@app.route("/c_rtracklocation")  # Url Decalaration
def c_r_track_location():  # Url Function
    try:
        fid = request.args.get("fid")  # Getting value from request object
        print(fid)  # Print the statement
        con = getconnection()
        cur = con.cursor()
        cur.execute(
            "select * from foodtrack where food_id=%s", (fid,)
        )  # Query Execution
        current_location = cur.fetchone()
        return make_response(
            jsonify({"current_location": current_location, "success": True}), 200
        )  # Making response as a json object
    except Exception:
        traceback.print_exc()  # Print the current exception
        return make_response(
            jsonify({"success": False}), 500
        )  # Making response as a json object


# REQUEST TO DONOR PAGE(ORDER PAGE)


@app.route("/order", methods=["Post", "Get"])  # Url Decalaration
def order():  # Url Function
    con = getconnection()
    cur = con.cursor()
    cur_fid = request.args.get("fid")  # Getting value from request object
    print(cur_fid, session["current_email"])  # Print the Statement
    cur.execute("select * from donor where fid=%s", [cur_fid])  # Query Execution
    result = cur.fetchone()
    print(result)  # Print the Statement
    cur.execute(
        "select * from signupentry where email=%s", (session["current_email"],)
    )  # Query Execution
    result1 = cur.fetchone()
    print(result1)  # Print the Statement
    cur.close()  # Close the cursor object
    return render_template(
        "order.html", d_uid=result[1], d_fid=result[0], r_uid=result1[0]
    )  # Response as a template


# REQUEST TO COMMUNTIY DONOR PAGE(ORDER PAGE)


@app.route("/corder", methods=["Post", "Get"])  # Url Decalaration
def community_order():  # Url Function
    con = getconnection()
    cur = con.cursor()
    cur_fid = request.args.get("cfid")  # Getting value from request object
    print(cur_fid, session["current_email"])  # Print the Statement
    cur.execute(
        "select * from communityentry where cfid=%s", [cur_fid]
    )  # Query Execution
    result = cur.fetchone()
    print(result)  # Print the Statement
    cur.execute(
        "select * from signupentry where email=%s", (session["current_email"],)
    )  # Query Execution
    result1 = cur.fetchone()
    print(result1)  # Print the Statement
    cur.close()  # Close the cursor object
    return render_template(
        "corder.html", cd_cuid=result[1], d_cfid=result[0], r_uid=result1[0]
    )
    # Response as a template


# USER MY FOOD ENTRY PAGE


@app.route("/myentry", methods=["Post", "Get"])  # Url Decalaration
def myentry():  # Url Function
    con = getconnection()
    cur = con.cursor()
    cur.execute(
        "select d.*,s.* from donor as d JOIN signupentry as s on s.uid = d.uid where d.email=%s",
        (session["current_email"],),
    )  # Query Execution
    result = cur.fetchall()
    print(result)  # Print the Statement
    cur.close()  # Close the cursor object
    return render_template("myentry.html", data1=result)  # Response as a template


# MY FOOD ENTRY PAGE


@app.route("/myentry1", methods=["Post", "Get"])  # Url Decalaration
def myentry1():  # Url Function
    con = getconnection()
    cur = con.cursor()
    cur.execute(
        "select ce.*,cs.* from communityentry as ce JOIN communitysignup as cs on cs.cuid = ce.cuid where ce.cemail=%s",
        (session["current_email"],),
    )  # Query Execution
    result = cur.fetchall()
    print(result)  # Print the Statement
    cur.close()  # Close the cursor object
    return render_template("myentry1.html", data1=result)  # Response as a template


if __name__ == "__main__":  # Main method initialization
    app.run(port=8000, debug=True)  # Server startup
