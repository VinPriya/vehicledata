import sqlite3
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_result',methods=["GET"])
def display_result():
     
    v_id=request.args.get("v_id")
        # open the connection to the database
    conn = sqlite3.connect('elecVehicle.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(f"select * from VehicleRegistration JOIN VehicleAddress ON VehicleRegistration.Vehicle_ID=VehicleAddress.Vehicle_ID WHERE VehicleRegistration.Vehicle_ID='{v_id}'")
    rows = cur.fetchall()
    conn.close()
    return render_template('output.html', rows=rows)