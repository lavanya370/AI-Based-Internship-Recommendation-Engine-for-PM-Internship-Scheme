from flask import Flask, render_template, request, redirect, session
import sqlite3
import joblib

app = Flask(__name__)
app.secret_key = "lavanya123"

# Load AI Model
try:
    model = joblib.load("model/recommendation_model.pkl")
except:
    model = None


# ---------------- HOME ---------------- #

@app.route('/')
def home():
    return render_template("index.html")


# ---------------- REGISTER ---------------- #

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        department = request.form['department']
        cgpa = request.form['cgpa']
        skills = request.form['skills']
        interest = request.form['interest']
        location = request.form['location']

        conn = sqlite3.connect("internship.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO student
        (name,email,password,department,cgpa,skills,interest,location)
        VALUES (?,?,?,?,?,?,?,?)
        """,(name,email,password,department,cgpa,skills,interest,location))

        conn.commit()
        conn.close()

        return redirect('/login')

    return render_template("register.html")


# ---------------- LOGIN ---------------- #

@app.route('/login', methods=['GET','POST'])
def login():

    if request.method == 'POST':

        email=request.form['email']
        password=request.form['password']

        conn=sqlite3.connect("internship.db")
        cursor=conn.cursor()

        cursor.execute("SELECT * FROM student WHERE email=? AND password=?",
                       (email,password))

        user=cursor.fetchone()

        conn.close()

        if user:

            session['name']=user[1]
            session['email']=user[2]
            session['department']=user[4]
            session['cgpa']=user[5]
            session['skills']=user[6]
            session['interest']=user[7]
            session['location']=user[8]

            return redirect('/dashboard')

        else:

            return "Invalid Email or Password"

    return render_template("login.html")


# ---------------- DASHBOARD ---------------- #

@app.route('/dashboard')
def dashboard():

    if 'name' not in session:
        return redirect('/login')

    return render_template(
        "dashboard.html",
        name=session['name'],
        department=session['department'],
        cgpa=session['cgpa'],
        skills=session['skills'],
        interest=session['interest'],
        location=session['location']
    )


# ---------------- AI RECOMMENDATION ---------------- #

@app.route('/recommendation')
def recommendation():

    if 'name' not in session:
        return redirect('/login')

    # Sample prediction (replace with your trained model input later)
    internship = "AI Intern"

    if model is not None:
        try:
            sample = [[8.5,0,1,0,1,0,1,0,0]]
            prediction = model.predict(sample)

            internship_list = [
                "AI Intern",
                "Data Science Intern",
                "Machine Learning Intern",
                "Python Developer Intern",
                "Web Development Intern",
                "Software Developer Intern"
            ]

            internship = internship_list[int(prediction[0])]

        except:
            internship = "AI Intern"

    return render_template(
        "recommendation.html",
        name=session['name'],
        department=session['department'],
        cgpa=session['cgpa'],
        skills=session['skills'],
        interest=session['interest'],
        location=session['location'],
        result=internship
    )


# ---------------- ADMIN ---------------- #

@app.route('/admin')
def admin():
    return render_template("admin_login.html")


@app.route('/admin_dashboard')
def admin_dashboard():
    return render_template("admin_dashboard.html")


# ---------------- LOGOUT ---------------- #

@app.route('/logout')
def logout():

    session.clear()

    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)