from flask import Flask, jsonify, request

app = Flask(_name_)

@app.route("/")
def home():
    return jsonify({
        "project": "SlopeWatch",
        "message": "Landslide Risk Monitoring System is running"
    })

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    rainfall = float(data.get("rainfall", 0))
    slope = float(data.get("slope", 0))

    # Prototype risk logic
    if rainfall >= 100 and slope >= 30:
        risk = "HIGH"
    elif rainfall >= 50 or slope >= 20:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return jsonify({
        "rainfall": rainfall,
        "slope": slope,
        "risk": risk
    })


if _name_ == "_main_":
    app.run(debug=True)
