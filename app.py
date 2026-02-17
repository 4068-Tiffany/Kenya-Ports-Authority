from flask import Flask, render_template, request, redirect, session
import joblib
import random
import numpy as np

app = Flask(__name__)
app.secret_key = "traffic_secret"

# LOAD MODEL
model = joblib.load("kpa_congestion_model.pkl")

# ===== ROAD FEATURES (INPUT TO MODEL) =====
roads_features = {
    "Mombasa Road":  [12,4,7,500,600,0.7,1,1,1,1],
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

def generate_roads():
    roads = {}

    for road, feats in roads_features.items():
        X = np.array(feats).reshape(1,-1)

        # AI prediction
        pred = model.predict(X)[0]

        # fake delay for realism
        delay = random.randint(5,40)

        if delay < 15:
            color = "green"
        elif delay < 25:
            color = "orange"
        else:
            color = "red"

        roads[road] = {
            "delay": delay,
            "color": color,
            "coords": roads_coords[road],
            "ai": int(pred)
        }

    return roads

# ===== ROUTES =====

@app.route("/")
def home():
    return redirect("/login")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        session["user"] = request.form["user"]
        return redirect("/dashboard")
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    roads = generate_roads()
    best_route = min(roads, key=lambda r: roads[r]["delay"])

    return render_template(
        "dashboard.html",
        roads=roads,
        best_route=best_route
    )

if __name__ == "__main__":
    app.run(debug=True)
