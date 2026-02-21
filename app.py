from flask import Flask, render_template, request, redirect, session, url_for
import random

app = Flask(__name__)
app.secret_key = "secret123"

users = {
    "admin@mail.com": "1234",
    "operator@mail.com": "pass"
}

roads_coords = {
    "Mombasa Road": [-1.319, 36.927],
    "Southern Bypass": [-1.334, 36.763],
    "Thika Road": [-1.25, 36.85],
    "Likoni Road": [-4.08, 39.66]
}

def generate_directions(road):
    directions_data = {
        "Mombasa Road": ["Start at KPA Gate", "Head north", "Arrive at destination"],
        "Southern Bypass": ["Merge onto bypass", "Continue for 8 km", "Arrive"],
        "Thika Road": ["Head north", "Take exit 7", "Arrive"],
        "Likoni Road": ["Head to ferry crossing", "Turn left", "Arrive"]
    }
    return directions_data.get(road, [])

def generate_roads():
    roads = {}
    for road, coords in roads_coords.items():
        delay = random.randint(5, 45)
        accidents = random.randint(0, 2)
        construction = random.choice([True, False])
        
        # Scoring logic (lower is better)
        score = delay + (accidents * 10) + (8 if construction else 0)
        
        color = "green" if delay < 15 else "orange" if delay < 25 else "red"
        
        roads[road] = {
            "delay": delay, "color": color, "coords": coords,
            "accidents": accidents, "construction": construction,
            "score": score, "directions": generate_directions(road)
        }
    best = min(roads, key=lambda r: roads[r]["score"])
    return roads, best


@app.route("/")
def landing():
    # This shows the "Traffic AI" entry screen first
    return render_template("landing.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if email in users and users[email] == password:
            session["user"] = email
            return redirect(url_for("dashboard"))
    # Shows the login screen after they click "Enter Control Room"
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    roads, best = generate_roads()
    return render_template("dashboard.html", roads=roads, best_route=best, user=session["user"])


if __name__ == "__main__":
    app.run(debug=True)