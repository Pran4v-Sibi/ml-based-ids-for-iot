import joblib
import pandas as pd
import os
from flask import Flask, request, jsonify
import random
from flask import render_template
from datetime import datetime

app = Flask(__name__)

# Load model and scaler
model = joblib.load('random_forest_tuned_model.pkl')
scaler = joblib.load('scaler.pkl')

# Full features

full_model_features = [
    "Flow Duration", "Total Fwd Packets", "Total Backward Packets", 
    "Fwd Packets Length Total", "Bwd Packets Length Total", 
    "Fwd Packet Length Max", "Fwd Packet Length Mean", 
    "Fwd Packet Length Std", "Bwd Packet Length Max", "Bwd Packet Length Mean",
    "Bwd Packet Length Std", "Flow Bytes/s", "Flow Packets/s", 
    "Flow IAT Mean", "Flow IAT Std", "Flow IAT Max", "Flow IAT Min",
    "Fwd IAT Total", "Fwd IAT Mean", "Fwd IAT Std", "Fwd IAT Max", 
    "Fwd IAT Min", "Bwd IAT Total", "Bwd IAT Mean", "Bwd IAT Std",
    "Bwd IAT Max", "Bwd IAT Min", "Fwd PSH Flags", "Fwd Header Length",
    "Bwd Header Length", "Fwd Packets/s", "Bwd Packets/s", "Packet Length Max",
    "Packet Length Mean", "Packet Length Std", "Packet Length Variance",
    "SYN Flag Count", "URG Flag Count", "Avg Packet Size", 
    "Avg Fwd Segment Size", "Avg Bwd Segment Size", "Subflow Fwd Packets",
    "Subflow Fwd Bytes", "Subflow Bwd Packets", "Subflow Bwd Bytes",
    "Init Fwd Win Bytes", "Init Bwd Win Bytes", "Fwd Act Data Packets",
    "Fwd Seg Size Min", "Active Mean", "Active Std", "Active Max", 
    "Active Min", "Idle Mean", "Idle Std", "Idle Max", "Idle Min"
]

# Token
API_TOKEN = os.getenv("API_TOKEN")


def rebuild_full_features(input_data):
    input_df = pd.DataFrame([input_data])
    final_input = pd.DataFrame(columns=full_model_features)

    for col in input_df.columns:
        if col in final_input.columns:
            final_input[col] = input_df[col]

    final_input.fillna(0, inplace=True)
    scaled_data = scaler.transform(final_input)

    return scaled_data

@app.route('/')
def home():
    return '''
    <h2>🚀 IoT IDS API is Live!</h2>
    <p>This is the home page of the deployed IDS project.</p>
    <p><strong>POST</strong> /predict – Use this endpoint to send intrusion data (via Postman or frontend code).</p>
    <p><a href="/dashboard">📊 View Live Intrusion Dashboard</a></p>
    '''

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_json = request.get_json()

        token = request.headers.get('Authorization')
        if not token or token != API_TOKEN:
            return jsonify({
                "error": "Unauthorized: Missing or invalid token.",
                "status": "error"
            }), 401

        if not input_json:
            return jsonify({"error": "No input data provided."}), 400

        processed_data = rebuild_full_features(input_json)

        prediction = model.predict(processed_data)[0]
        proba = model.predict_proba(processed_data)[0]
        confidence = max(proba)

        return jsonify({
            "prediction": int(prediction),
            "confidence": round(float(confidence), 4),
            "status": "success"
        })

    except Exception as e:
        return jsonify({
            "error": f"Internal Server Error: {str(e)}",
            "status": "error"
        }), 500


# Simulated prediction feed
intrusion_feed = []

@app.route('/dashboard')
def dashboard():
    prediction = random.choice([0, 1])
    confidence = round(random.uniform(0.6, 0.99), 2)
    time = datetime.now().strftime("%H:%M:%S")

    intrusion_feed.insert(0, {
        "time": time,
        "prediction": prediction,
        "confidence": confidence
    })

    if len(intrusion_feed) > 10:
        intrusion_feed.pop()

    return render_template('dashboard.html', feed=intrusion_feed)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
