from flask import Flask, render_template, request, redirect, session, url_for
import random

app = Flask(__name__)
app.secret_key = "secret123"

# DEMO USERS
users = {
    "admin@mail.com": "1234",
    "operator@mail.com": "pass"
}

# ROAD DATA
roads_coords = {
    "Mombasa Road": [-1.319, 36.927],
    "Southern Bypass": [-1.334, 36.763],
    "Thika Road": [-1.25, 36.85],
    "Likoni Road": [-4.08, 39.66]
}

def generate_roads():
    roads = {}
    for road, coords in roads_coords.items():
        delay = random.randint(5, 40)

        if delay < 15:
            color = "green"
        elif delay < 25:
            color = "orange"
        else:
            color = "red"

        roads[road] = {
            "delay": delay,
            "color": color,
            "coords": coords
        }

    best = min(roads, key=lambda r: roads[r]["delay"])
    return roads, best

@app.route("/")
def landing():
    return render_template("landing.html")

@app.route("/login", methods=["GET","POST"])
def login():
    error = None

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email in users and users[email] == password:
            session["user"] = email
            return redirect("/dashboard")
        else:
            error = "Invalid login"

    return render_template("login.html", error=error)

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")

    roads, best = generate_roads()

    return render_template(
        "dashboard.html",
        roads=roads,
        best_route=best,
        user=session["user"]
    )

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
