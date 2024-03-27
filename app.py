from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
connection = sqlite3.connect('trips.db')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/profile.html')
def index2():
    return render_template("profile.html")

@app.route('/contact.html')
def index3():
    return render_template("contact.html")

@app.route('/trip.html')
def index4():
    return render_template("trip.html")


c = connection.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS Trips( 
destination VARCHAR(30) PRIMARY KEY,
S_date DATE,
R_date DATE);""")
connection.commit()
connection.close()


@app.route('/index')
def trips():
    connection = sqlite3.connect('trips.db')
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM Trips")
    trip = crsr.fetchall()
    connection.close()
    return render_template('index', trips=trip)

@app.route('/add_trip', methods=['POST'])
def add_trip():
    destination = request.form['destination']
    S_date = request.form['S_date']
    R_date = request.form['R_date']
    
    conn = sqlite3.connect('trips.db')
    crsr = conn.cursor()
    crsr.execute("INSERT INTO Trips (destination,Start_date,Return_date) VALUES (?, ?, ?)",
                  (destination, S_date, R_date))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete_trip/<int:trip_id>', methods=['POST'])
def delete_trip(trip_id):
    conn = sqlite3.connect('trips.db')
    conn.execute('DELETE FROM Trips WHERE id = ?', (trip_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
