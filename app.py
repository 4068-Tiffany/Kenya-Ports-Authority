from flask import Flask, render_template, request, redirect, session
import joblib
import random
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "traffic_secret")

model = joblib.load("kpa_congestion_model.pkl")
# =========================
# ROAD COORDINATES
# =========================
roads_coords = {
    "Mombasa Road": [-1.319, 36.927],
    "Southern Bypass": [-1.334, 36.763],
    "Thika Road": [-1.25, 36.85],
    "Likoni Road": [-4.08, 39.66]
}

# =========================
# LIVE TRAFFIC GENERATOR
# =========================
def generate_live_data():
    roads = {}

    for road in roads_coords:
        delay = random.randint(5, 40)
        vehicles = random.randint(50, 500)

        if delay < 15:
            color = "green"
        elif delay < 25:
            color = "orange"
        else:
            color = "red"

        roads[road] = {
            "delay": delay,
            "vehicles": vehicles,
            "color": color,
            "coords": roads_coords[road]
        }

    return roads

# =========================
# LOGIN
# =========================
@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        session["user"] = request.form["user"]
        return redirect("/dashboard")
    return render_template("login.html")

# =========================
# DASHBOARD
# =========================
@app.route("/dashboard")
def dashboard():
    roads = generate_live_data()
    best_route = min(roads, key=lambda r: roads[r]["delay"])

    leaderboard = sorted(
        [{"route":r,"score":100-roads[r]["delay"]} for r in roads],
        key=lambda x: x["score"],
        reverse=True
    )

    return render_template(
        "dashboard.html",
        roads=roads,
        best_route=best_route,
        leaderboard=leaderboard
    )

# =========================
# PRESENTATION MODE
# =========================
@app.route("/presentation")
def presentation():
    roads = generate_live_data()
    best_route = min(roads, key=lambda r: roads[r]["delay"])

    return render_template(
        "presentation.html",
        roads=roads,
        best_route=best_route
    )

if __name__ == "__main__":
    app.run(debug=True)
