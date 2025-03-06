from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model and scaler (make sure they are saved)
with open("cancer_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("scaler.pkl", "rb") as scaler_file:
    scaler = pickle.load(scaler_file)

# Homepage
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    feature_values = [float(request.form[f'feature{i}']) for i in range(30)]
    
    # Convert input to NumPy array and scale
    new_patient = np.array([feature_values])
    new_patient_scaled = scaler.transform(new_patient)

    # Make a prediction
    prediction = model.predict(new_patient_scaled)
    
    result = "Malignant (Cancerous)" if prediction[0] == 1 else "Benign (Non-Cancerous)"
    
    return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)