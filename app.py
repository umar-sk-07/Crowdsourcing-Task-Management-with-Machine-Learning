from flask import Flask, render_template, request
import pandas as pd
import pickle  # Or use joblib if you prefer for model loading

# Step 1: Create a Flask app
app = Flask(__name__)

# Step 2: Load your pre-trained models
# You can save the models after training in your Jupyter Notebook using joblib or pickle
# For this example, I'm assuming you saved your models as .pkl files.
# Adjust the paths to look inside the CrowdSourcing folder
with open('CrowdSourcing/decision_tree_model.pkl', 'rb') as f:
    dt_classifier = pickle.load(f)

with open('CrowdSourcing/linear_regression_model.pkl', 'rb') as f:
    lr_model = pickle.load(f)

with open('CrowdSourcing/logistic_regression_model.pkl', 'rb') as f:
    log_reg = pickle.load(f)

# Step 3: Define the route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Step 4: Define the route for predictions (to handle the form submission)
@app.route('/predict', methods=['POST'])
def predict():
    # Step 5: Get form data from the frontend
    task_difficulty = int(request.form['task_difficulty'])
    worker_skill = int(request.form['worker_skill'])
    performance_score = int(request.form.get('performance_score', 0))  # Only for quality control

    # Task Allocation Prediction
    predicted_worker = dt_classifier.predict([[task_difficulty, worker_skill]])[0]

    # Performance Analysis Prediction
    predicted_time = lr_model.predict([[task_difficulty, worker_skill]])[0]

    # Quality Control Prediction
    predicted_quality = log_reg.predict([[task_difficulty, worker_skill, performance_score]])[0]
    quality_label = "High Quality" if predicted_quality == 1 else "Low Quality"

    # Step 6: Send the results back to the frontend
    return render_template('index.html', predicted_worker=predicted_worker, 
                           predicted_time=f"{predicted_time:.2f}", 
                           quality_label=quality_label)

# Step 7: Run the app
if __name__ == '__main__':
    app.run(debug=True)
