from flask import Flask, render_template, request, redirect, session, jsonify
import joblib
import random
import numpy as np

app = Flask(__name__)
app.secret_key = "traffic_secret"

model = joblib.load("kpa_congestion_model.pkl")

# ===== ROAD FEATURES =====
roads_features = {
    "Mombasa Road":[12,4,7,500,600,0.7,1,1,1,1],
    "Southern Bypass":[20,6,8,200,700,0.2,1,1,1,1],
    "Thika Road":[18,5,9,650,700,0.8,1,1,1,1],
    "Likoni Road":[10,2,5,450,500,0.6,1,0,1,0]
}

roads_coords = {
    "Mombasa Road":[-1.319,36.927],
    "Southern Bypass":[-1.334,36.763],
    "Thika Road":[-1.25,36.85],
    "Likoni Road":[-4.08,39.66]
}

# ===== LOGIN =====
@app.route("/")
def home():
    return redirect("/login")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        session["user"] = request.form["user"]
        return redirect("/dashboard")
    return render_template("login.html")

# ===== DASHBOARD =====
@app.route("/dashboard")
def dashboard():

    roads = {}
    ai_messages = []

    for road, features in roads_features.items():

        X = np.array(features).reshape(1,-1)
        pred = model.predict(X)[0]

        delay = random.randint(5,40)
        if pred == 1:
            delay += 10

        # 30-minute future prediction
        future_delay = delay + random.randint(-5,15)

        if delay < 15:
            color = "#00ffcc"
            status = "CLEAR"
        elif delay < 25:
            color = "#ffaa00"
            status = "MODERATE"
        else:
            color = "#ff3b3b"
            status = "CONGESTED"

        roads[road] = {
            "delay": delay,
            "future": future_delay,
            "color": color,
            "coords": roads_coords[road]
        }

        ai_messages.append(f"{road}: {status}")

    best_route = min(roads, key=lambda r: roads[r]["delay"])

    return render_template(
        "dashboard.html",
        roads=roads,
        best_route=best_route,
        ai_messages=ai_messages
    )

# ===== ROUTE API FOR LIVE UPDATE =====
@app.route("/api/routes")
def api_routes():

    data = {}
    for road in roads_features:

        delay = random.randint(5,40)
        data[road] = delay

    return jsonify(data)

# ===== ANALYTICS PAGE =====
@app.route("/analytics")
def analytics():

    stats = []
    for r in roads_features:
        stats.append({
            "road": r,
            "avg_delay": random.randint(10,35),
            "traffic": random.randint(200,900)
        })

    return render_template("analytics.html", stats=stats)

if __name__ == "__main__":
    app.run(debug=True)
