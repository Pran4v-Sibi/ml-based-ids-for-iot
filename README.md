# IoT Intrusion Detection System (IDS) using Machine Learning 🚀

This project implements a **Machine Learning-based Intrusion Detection System (IDS)** specifically designed for **IoT networks**. The model is built, containerized using Docker, and deployed to the cloud using Render.com for public access.

## 🚀 Project Overview

- **Model**: Random Forest Classifier
- **Framework**: Flask (for API development)
- **Containerization**: Docker
- **Version Control**: GitHub
- **Cloud Deployment**: Render Cloud Platform
- **Security**: Token-based API authentication

## 📚 Features

- Real-time prediction of network traffic as normal or attack.
- RESTful API with `/predict` endpoint.
- Token-based access control for secure API usage.
- Fully containerized using Docker.
- Publicly accessible through cloud hosting.

## 🛠️ Tech Stack

- Python 3.10
- Flask
- Scikit-learn
- Pandas
- Docker
- GitHub
- Render.com

## 🖥️ API Endpoints

| Method | Endpoint | Description |
|:-------|:---------|:------------|
| GET | `/` | Health check of API |
| POST | `/predict` | Send JSON input for intrusion detection prediction |

## 🔒 API Authentication

All `/predict` requests require an **Authorization token** to be passed in the header.

**Example Header:**

```plaintext
Authorization: YOUR_API_TOKEN

⚠️ Note: The API token is not shared publicly in this repository for security reasons.
If you require access for academic or demonstration purposes, please contact the project owner.

Requests without the correct token will receive a 401 Unauthorized response.

📦 Input JSON Example

{
  "Flow Duration": 123456,
  "Total Fwd Packets": 10,
  "Total Backward Packets": 12,
  "Fwd Packets Length Total": 600,
  "Bwd Packets Length Total": 800,
  "Fwd Packet Length Max": 60,
  "Fwd Packet Length Mean": 35,
  "Fwd Packet Length Std": 5,
  "Bwd Packet Length Max": 55,
  "Bwd Packet Length Mean": 30,
  "Bwd Packet Length Std": 4,
  "Flow Bytes/s": 1200,
  "Flow Packets/s": 20,
  "Flow IAT Mean": 1000,
  "Flow IAT Std": 100,
  "Flow IAT Max": 2000,
  "Flow IAT Min": 500,
  "Fwd IAT Total": 5000,
  "Fwd IAT Mean": 250,
  "Fwd IAT Std": 50,
  "Fwd IAT Max": 1000,
  "Fwd IAT Min": 200,
  "Bwd IAT Total": 6000,
  "Bwd IAT Mean": 300,
  "Bwd IAT Std": 60,
  "Bwd IAT Max": 1100,
  "Bwd IAT Min": 250,
  "Fwd PSH Flags": 0,
  "Fwd Header Length": 400,
  "Bwd Header Length": 420,
  "SYN Flag Count": 1,
  "URG Flag Count": 0,
  "Avg Packet Size": 45,
  "Avg Fwd Segment Size": 22,
  "Avg Bwd Segment Size": 25
}

🌍 Live API

You can access the live deployed API here:

🚀 Live URL: https://iot-ids-api.onrender.com

(Note: Authentication token required for POST requests.)

🧠 Future Improvements

Secure token management using environment variables.

Add user authentication and role-based access control.

Expand the model for multi-class classification (different types of attacks).

Set up logging and monitoring using cloud services.

📜 License

This project is for educational purposes and research only.