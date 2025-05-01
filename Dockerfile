# Step 1: Use an official lightweight Python image
FROM python:3.10-slim

# Step 2: Set working directory inside container
WORKDIR /app

# Step 3: Copy requirements and app files into container
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY random_forest_tuned_model.pkl random_forest_tuned_model.pkl
COPY scaler.pkl scaler.pkl
COPY templates/ ./templates/
# Step 4: Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Step 5: Expose the port Flask app will run on
EXPOSE 10000

# Step 6: Start the Flask app
CMD ["python", "app.py"]