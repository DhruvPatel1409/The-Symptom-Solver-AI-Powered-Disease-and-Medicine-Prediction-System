# The-Symptom-Solver-AI-Powered-Disease-and-Medicine-Prediction-System

## Project Overview
The **Symptom Solver** is an AI-powered disease prediction and medicine recommendation system based on user-entered symptoms. By leveraging machine learning models trained on medical datasets, the system predicts potential diseases and recommends appropriate medicines based on input symptoms, severity, age group, and gender. The project uses a user-friendly web application built with **Streamlit**.

## Features
- **Disease Prediction:** The system predicts a disease or health condition based on the symptoms provided by the user.
- **Medicine Recommendation:** Recommends relevant medicines based on the predicted disease or health condition.
- **Age and Gender Filtering:** Includes features to select the age group and gender for more accurate predictions.
- **Severity-based Input:** Allows the user to specify the severity of their symptoms (mild, moderate, severe) to enhance the prediction accuracy.
- **User-Friendly Interface:** Built using Streamlit, the system provides a simple and intuitive interface for users to interact with.

## Technologies Used
- **Python**: Core programming language used to build the model and the web app.
- **Keras**: Used for building and training the machine learning model.
- **TensorFlow**: Framework for implementing the deep learning model.
- **Streamlit**: Framework for creating the interactive web application.
- **NumPy**: Used for handling data processing and transformations.
- **Scikit-learn**: For various machine learning tasks like data preprocessing.
- **Pandas**: Used for data manipulation and analysis.

## Installation

### Prerequisites:
- Python 3.7 or higher
- TensorFlow and Keras
- Streamlit
- NumPy, Pandas, and other necessary libraries

Steps to Run the Project:
1) Clone the repository: 
git clone https://github.com/your-username/The-Symptom-Solver-AI-Powered-Disease-and-Medicine-Prediction-System.git
2) Install dependencies:
cd The-Symptom-Solver-AI-Powered-Disease-and-Medicine-Prediction-System
pip install -r requirements.txt
3) Run the Streamlit app:
streamlit run app.py
4) The application will open in your default browser. You can now input symptoms, select severity, age group, and gender, and receive disease predictions and medicine recommendations.

## Model Training

The model was trained on a dataset containing various symptoms and their corresponding diseases and medications. The training process involved several key steps, including data preprocessing, encoding symptoms, and training a deep neural network to make accurate predictions.

- **Neural Network Architecture**: A feed-forward neural network with multiple hidden layers was employed for both disease prediction and medicine recommendation. The architecture includes:
  - Input layer to handle the encoded symptom data.
  - Several hidden layers with activation functions like ReLU to capture complex patterns in the data.
  - Output layer with softmax activation to predict multiple classes for diseases and medicines.

- **Training Process**: The model was trained using **categorical cross-entropy loss** to handle multi-class classification tasks, and the **Adam optimizer** was used for efficient weight updates. The model was trained over multiple epochs with a focus on minimizing the loss function and improving prediction accuracy.

- **Model Evaluation**: After training, the model was evaluated on a validation set to assess its accuracy and make improvements. The trained model is capable of making real-time predictions on disease diagnosis and medicine recommendations based on user input.

## Usage

1. **Input Symptoms**: Select symptoms from the provided list of common health indicators. These symptoms will be used by the system to make predictions about potential diseases.
2. **Specify Severity**: Choose the severity of the symptoms (Mild, Moderate, Severe). This input helps the system refine the prediction based on how serious the symptoms are.
3. **Select Age and Gender**: Specify the age group (Child, Adult, Elderly) and gender (Male, Female, Other) for more accurate disease and medicine predictions. The system takes age and gender into account to provide tailored recommendations.
4. **Prediction**: After filling in the required information, click on the “Predict” button. The system will analyze the input and predict the most likely disease along with recommending appropriate medicines for the user.
   
Example Use Case :
Input: Symptoms like "fever", "headache", "fatigue".
Prediction: Disease: "Common Cold", Recommended Medicines: "Paracetamol", "Vitamin C".

Contributing :
We welcome contributions to enhance the functionality of this project. If you have an idea or improvement, feel free to fork the repository, create a branch, and submit a pull request. Please ensure all contributions follow the guidelines and maintain the project's integrity.

License : 
This project is licensed under the MIT License - see the LICENSE file for details.
