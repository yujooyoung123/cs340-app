from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os
import database.db_connector as db

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_yujoo'
app.config['MYSQL_PASSWORD'] = '0574' #last 4 of onid
app.config['MYSQL_DB'] = 'cs340_yujoo'
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)

db_connection = db.connect_to_database()

# Routes

@app.route('/')
def root():
    return render_template("main.j2")

# Projects

@app.route('/projects', methods=["GET"])
def get_projects():
    query = "SELECT * FROM Projects"
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()

    return render_template("projects.j2", Data=data)

@app.route('/add-project', methods=["POST"])
def add_project():
    projectID = request.form["projectID"]
    platMap = request.form["platMap"]
    date_string = request.form["startingDate"]
    startingDate = date_string.replace("-", "")
    
    query = "INSERT INTO Projects (projectID, platMap, startingDate) VALUES (%s, %s, %s)"
    cur = mysql.connection.cursor()
    cur.execute(query, (projectID, platMap, startingDate))
    mysql.connection.commit()

    return redirect("/projects")

@app.route("/delete-project/<int:projectID>")
def delete_project(projectID):
        query = "DELETE FROM Projects WHERE projectID='%s';"  
        cur = mysql.connection.cursor()
        cur.execute(query, (projectID,))
        mysql.connection.commit()

        return redirect("/projects")

@app.route("/update-project/<int:projectID>", methods=["POST", "GET"])
def update_project(projectID):
    if request.method == "GET":
        query = "SELECT * FROM Projects WHERE projectID=%s;"
        cur = mysql.connection.cursor()
        cur.execute(query, (projectID,))
        project_data = cur.fetchone()

        return render_template("update-project.j2", Data=project_data)
    
    elif request.method == "POST":   
        platMap = request.form["platMap"]
        date_string = request.form["startingDate"]
        startingDate = date_string.replace("-", "")
        
        query = "UPDATE Projects SET platMap = %s, startingDate = %s WHERE projectID = %s"
        cur = mysql.connection.cursor()
        cur.execute(query, (platMap, startingDate, projectID))
        mysql.connection.commit()

        return redirect("/projects")
    
    return redirect("/projects")

# Municipalities

@app.route('/municipalities')
def get_municipalities():
    query = "SELECT * FROM Municipalities"
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()

    return render_template("municipalities.j2", Data=data)

@app.route('/add-municipality', methods=["POST"])
def add_municipality():
    municipalityID = request.form["municipalityID"]
    municipalityName = request.form["municipalityName"]
    website = request.form["website"]
    stateName = request.form["stateName"]
    fileLocation = request.form["fileLocation"]

    
    query = "INSERT INTO Municipalities (municipalityID, municipalityName, website, stateName, fileLocation) VALUES (%s, %s, %s, %s, %s)"
    cur = mysql.connection.cursor()
    cur.execute(query, (municipalityID, municipalityName, website, stateName, fileLocation))
    mysql.connection.commit()

    return redirect("/municipalities")

@app.route("/delete-municipality/<int:municipalityID>")
def delete_municipality(municipalityID):
        query = "DELETE FROM Municipalities WHERE municipalityID='%s';"  
        cur = mysql.connection.cursor()
        cur.execute(query, (municipalityID,))
        mysql.connection.commit()

        return redirect("/municipalities")

@app.route("/update-municipality/<int:municipalityID>", methods=["POST", "GET"])
def update_municipality(municipalityID):
    if request.method == "GET":
        query = "SELECT * FROM Municipalities WHERE municipalityID=%s;"
        cur = mysql.connection.cursor()
        cur.execute(query, (municipalityID,))
        project_data = cur.fetchone()

        return render_template("update-municipality.j2", Data=project_data)
    
    elif request.method == "POST":   
        municipalityID = request.form["municipalityID"]
        municipalityName = request.form["municipalityName"]
        website = request.form["website"]
        stateName = request.form["stateName"]
        fileLocation = request.form["fileLocation"]
        
        query = "UPDATE Municipalities SET municipalityName = %s, website = %s, stateName = %s, fileLocation = %s, WHERE municipalityID = %s"
        cur = mysql.connection.cursor()
        cur.execute(query, (municipalityName, website, stateName, fileLocation, municipalityID))
        mysql.connection.commit()

        return redirect("/municipalities")
    
    return redirect("/municipalities")

# Owners

@app.route('/owners')
def get_owners():
    query = "SELECT * FROM Owners"
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()

    return render_template("owners.j2", Data=data)

@app.route('/add-owner', methods=["POST"])
def add_owner():
    ownerID = request.form["ownerID"]
    ownerName = request.form["ownerName"]
    address = request.form["address"]
    phoneNumber = request.form["phoneNumber"]
    email = request.form["email"]
    projectID = request.form["projectID"]
    caseID = request.form["caseID"]

    
    query = "INSERT INTO Owners (ownerID, ownerName, address, phoneNumber, email, projectID, caseID) VALUES (%s, %s, %s, %s, %s, %s, %s);"
    cur = mysql.connection.cursor()
    cur.execute(query, (ownerID, ownerName, address, phoneNumber, email, projectID, caseID))
    mysql.connection.commit()

    return redirect("/owners")

@app.route("/delete-owner/<int:ownerID>")
def delete_owner(ownerID):
        query = "DELETE FROM Owners WHERE ownerID='%s';"  
        cur = mysql.connection.cursor()
        cur.execute(query, (ownerID,))
        mysql.connection.commit()

        return redirect("/owners")

@app.route("/update-owner/<int:ownerID>", methods=["POST", "GET"])
def update_owner(ownerID):
    if request.method == "GET":
        query = "SELECT * FROM Owners WHERE ownerID=%s;"
        cur = mysql.connection.cursor()
        cur.execute(query, (ownerID,))
        project_data = cur.fetchone()

        return render_template("update-owner.j2", Data=project_data)
    
    elif request.method == "POST":   
        ownerID = request.form["ownerID"]
        ownerName = request.form["ownerName"]
        address = request.form["address"]
        phoneNumber = request.form["phoneNumber"]
        email = request.form["email"]
        projectID = request.form["projectID"]
        caseID = request.form["caseID"]
        
        query = "UPDATE Owners SET ownerName = %s, address = %s, phoneNumber = %s, email = %s, projectID = %s, caseID = %s, WHERE ownerID = %s;"
        cur = mysql.connection.cursor()
        cur.execute(query, (ownerName, address, phoneNumber, email, projectID, caseID, ownerID))
        mysql.connection.commit()

        return redirect("/owners")
    
    return redirect("/owners")

# Cases

@app.route('/cases')
def get_cases():
    query = "SELECT * FROM Cases"
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()

    return render_template("cases.j2", Data=data)

@app.route('/add-case', methods=["POST"])
def add_case():
    caseID = request.form["caseID"]
    caseNumber = request.form["caseNumber"]
    deadlineDate = request.form["deadlineDate"]
    projectID = request.form["projectID"]
    lawyerID = request.form["lawyerID"]
    
    query = "INSERT INTO Cases (caseID, caseNumber, deadlineDate, projectID, lawyerID) VALUES (%s, %s, %s, %s, %s)"
    cur = mysql.connection.cursor()
    cur.execute(query, (caseID, caseNumber, deadlineDate, projectID, lawyerID))
    mysql.connection.commit()

    return redirect("/cases")

@app.route("/delete-case/<int:caseID>")
def delete_case(caseID):
        query = "DELETE FROM Cases WHERE caseID='%s';"  
        cur = mysql.connection.cursor()
        cur.execute(query, (caseID,))
        mysql.connection.commit()

        return redirect("/cases")

@app.route("/update-case/<int:caseID>", methods=["POST", "GET"])
def update_case(caseID):
    if request.method == "GET":
        query = "SELECT * FROM Cases WHERE casesID=%s;"
        cur = mysql.connection.cursor()
        cur.execute(query, (caseID,))
        project_data = cur.fetchone()

        return render_template("update-case.j2", Data=project_data)
    
    elif request.method == "POST":   
        caseID = request.form["caseID"]
        caseNumber = request.form["caseNumber"]
        deadlineDate = request.form["deadlineDate"]
        projectID = request.form["projectID"]
        lawyerID = request.form["lawyerID"]
        
        query = "UPDATE Cases SET caseNumber = %s, deadlineDate = %s, projectID = %s, lawyerID = %s WHERE caseID = %s"
        cur = mysql.connection.cursor()
        cur.execute(query, (caseNumber, deadlineDate, projectID, lawyerID, caseID))
        mysql.connection.commit()

        return redirect("/cases")
    
    return redirect("/cases")

# Lawyers

@app.route('/lawyers')
def lawyers():
    query = "SELECT * FROM Lawyers"
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()

    return render_template("lawyers.j2", Data=data)

@app.route('/add-lawyer', methods=["POST"])
def add_lawyer():
    lawyerID = request.form["lawyerID"]
    lawyerName = request.form["lawyerName"]
    stateLicensed = request.form["stateLicensed"]
    
    query = "INSERT INTO Lawyers (lawyerID, lawyerName, stateLicensed) VALUES (%s, %s, %s)"
    cur = mysql.connection.cursor()
    cur.execute(query, (lawyerID, lawyerName, stateLicensed))
    mysql.connection.commit()

    return redirect("/lawyers")

@app.route("/delete-lawyer/<int:lawyerID>")
def delete_lawyer(lawyerID):
        query = "DELETE FROM Lawyers WHERE lawyerID='%s';"  
        cur = mysql.connection.cursor()
        cur.execute(query, (lawyerID,))
        mysql.connection.commit()

        return redirect("/lawyers")

@app.route("/update-lawyer/<int:lawyerID>", methods=["POST", "GET"])
def update_lawyer(lawyerID):
    if request.method == "GET":
        query = "SELECT * FROM Lawyers WHERE lawyerID=%s;"
        cur = mysql.connection.cursor()
        cur.execute(query, (lawyerID,))
        project_data = cur.fetchone()

        return render_template("update-lawyer.j2", Data=project_data)
    
    elif request.method == "POST":
        lawyerID = request.form["lawyerID"]
        lawyerName = request.form["lawyerName"]
        stateLicensed = request.form["stateLicensed"]
        
        query = "UPDATE Lawyers SET lawyerName = %s, stateLicensed = %s, WHERE lawyerID = %s;"
        cur = mysql.connection.cursor()
        cur.execute(query, (lawyerName, stateLicensed, lawyerID))
        mysql.connection.commit()

        return redirect("/lawyers")
    
    return redirect("/lawyers")

# Listener
if __name__ == "__main__":
        #Start the app on port 3000, it will be different once hosted
    app.run(port=57305, debug=True)
    