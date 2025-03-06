# Cancer Detection Web App

📌 Project Overview
    This is a **Machine Learning-based Cancer Detection Web App** built using Flask and Scikit-Learn. The model predicts whether a tumor is Malignant (cancerous) or Benign (non-cancerous) based on input features from the "Breast Cancer Wisconsin Dataset".

🚀 Features
    - User-friendly Web Interface (Bootstrap-based UI)
    - Flask Backend for ML model prediction
    - Trained ML Model using Logistic Regression, SVM, and Random Forest
    - Deployment on Render (Free cloud hosting)

🛠️ Technologies Used
    - Python 3
    - Flask (for Web Framework)
    - Scikit-Learn (Machine Learning Models)
    - Pandas & NumPy (Data Processing)
    - Bootstrap (UI Design)
    - HTML, CSS, JavaScript (Frontend)
  
📂 Project Structure
    ```
    CancerDetectionApp/
    │── app.py                 # Flask application
    │── requirements.txt       # Python dependencies
    │── cancer_model.pkl       # Trained ML model
    │── scaler.pkl             # Pre-trained scaler
    │── /templates             # HTML Templates
    │   ├── index.html         # Main Web Page
    │── /static                # Static Files (CSS, JS, Images)
    │   ├── style.css          # Custom Styling
    │── README.md              # Project Documentation
    ```

🔧 Installation & Setup
    1️⃣ Clone the Repository
      ```bash
      git clone https://github.com/your-username/cancer-detection-app.git
      cd cancer-detection-app
      ```
    
    2️⃣ Install Dependencies
      ```bash
      pip install -r requirements.txt
      ```
    
    3️⃣ Run the Application
      ```bash
      python app.py
      ```
Open the browser and go to:`http://127.0.0.1:5000/`

🧠 Machine Learning Models Implemented
1️⃣ Logistic Regression
2️⃣ Support Vector Machine (SVM)
3️⃣ Random Forest Classifier

The best model is selected based on Precision Score & Accuracy.

📊 How to Use the Web App
  1️⃣ Enter Feature Values (like `radius_mean`, `texture_mean`, etc.).  
  2️⃣ Click on 'Predict' to get the result.  
  3️⃣ The app will display Malignant (Cancerous) 🔴 or Benign (Non-Cancerous) 🟢.

📬 Contact
    For any issues or suggestions, feel free to reach out:
    📧 Email: `shivanisangwan0801@gmail.com`
    🔗 GitHub: https://github.com/Shivanii-Sangwan

