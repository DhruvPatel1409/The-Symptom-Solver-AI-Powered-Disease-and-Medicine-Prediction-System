The-Symptom-Solver-AI-Powered-Disease-and-Medicine-Prediction-System

Overview :
"The Symptom Solver" is an AI-powered disease and medicine prediction system designed to help users identify potential health conditions based on their symptoms. Using machine learning algorithms, this system predicts diseases and recommends medicines by analyzing user inputs. The system also categorizes diseases based on severity and recommends effective treatments tailored to each condition.

Key Features:
Disease Prediction: The system predicts a disease or health condition based on the symptoms provided by the user.
Medicine Recommendation: Recommends relevant medicines based on the predicted disease or health condition.
Age and Gender Filtering: Includes features to select the age group and gender for more accurate predictions.
Severity-based Input: Allows the user to specify the severity of their symptoms (mild, moderate, severe) to enhance the prediction accuracy.
User-Friendly Interface: Built using Streamlit, the system provides a simple and intuitive interface for users to interact with.

Technologies Used:
Python: Core programming language used to build the model and the web app.
Keras: Used for building and training the machine learning model.
TensorFlow: Framework for implementing the deep learning model.
Streamlit: Framework for creating the interactive web application.
NumPy: Used for handling data processing and transformations.
Scikit-learn: For various machine learning tasks like data preprocessing.
Pandas: Used for data manipulation and analysis.

Installation
Prerequisites:
Python 3.7 or higher
TensorFlow and Keras
Streamlit
NumPy, Pandas, and other necessary libraries

Steps to Run the Project:
1) Clone the repository: 
git clone https://github.com/your-username/The-Symptom-Solver-AI-Powered-Disease-and-Medicine-Prediction-System.git
2) Install dependencies:
cd The-Symptom-Solver-AI-Powered-Disease-and-Medicine-Prediction-System
pip install -r requirements.txt
3) Run the Streamlit app:
streamlit run app.py
4) The application will open in your default browser. You can now input symptoms, select severity, age group, and gender, and receive disease predictions and medicine recommendations.

Model Training:
The model was trained on a dataset containing various symptoms and their corresponding diseases and medications. The training involved preprocessing the data, encoding symptoms, and using a deep neural network to make predictions.
Neural Network Architecture: A feed-forward neural network with multiple layers was used for disease and medicine prediction.
Training Process: The model was trained using categorical cross-entropy loss and the Adam optimizer.

Usage :
1) Input Symptoms: Select symptoms from the provided list.
2) Specify Severity: Choose the severity of the symptoms (Mild, Moderate, Severe).
3) Select Age and Gender: The system allows users to specify their age group (Child, Adult, Elderly) and gender for better prediction.
4) Prediction: Once you click on the “Predict” button, the system will predict the disease and recommend relevant medicines.

Example Use Case :
Input: Symptoms like "fever", "headache", "fatigue".
Prediction: Disease: "Common Cold", Recommended Medicines: "Paracetamol", "Vitamin C".

Contributing :
We welcome contributions to enhance the functionality of this project. If you have an idea or improvement, feel free to fork the repository, create a branch, and submit a pull request. Please ensure all contributions follow the guidelines and maintain the project's integrity.

License : 
This project is licensed under the MIT License - see the LICENSE file for details.
