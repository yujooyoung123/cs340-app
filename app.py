from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os
# import database.db_connector as db

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_yujoo'
app.config['MYSQL_PASSWORD'] = '0574' #last 4 of onid
app.config['MYSQL_DB'] = 'cs340_yujoo'
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)

# db_connection = db.connect_to_database()

# Routes
@app.route('/')
def root():
    return render_template("main.j2")

@app.route('/projects')
def get_proj():
    return render_template("projects.j2")

@app.route('/municipalities')
def get_municipalities():
    return render_template("municipalities.j2")

@app.route('/owners')
def get_owners():
    return render_template("owners.j2")

@app.route('/cases')
def get_cases():
    return render_template("cases.j2")

@app.route('/lawyers')
def get_lawyers():
    return render_template("lawyers.j2")

# @app.route('/test-query')
# def get_db():
#     query = "SELECT * FROM Projects"
#     cursor = db.execute_query(db_connection=db_connection, query=query)
#     results = json.dumps(cursor.fetchall())
#     return results

# Listener
if __name__ == "__main__":
        #Start the app on port 3000, it will be different once hosted
    app.run(port=57300, debug=True)
    