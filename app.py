import streamlit as st
import numpy as np
from keras.models import load_model

# Load the trained model
model = load_model('C:/Users/ADMIN/Desktop/python jupyter/AI/project/medicine_model.keras')

# Define a list of all symptoms in the correct order of features
all_symptoms = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of_urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload.1', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze', 'Age_Group_Adult', 'Age_Group_Child', 'Age_Group_Elderly', 'Gender_Male', 'Gender_Female', 'Severity_Mild', 'Severity_Moderate', 'Severity_Severe']

# Define the medicines list
medicines = ['prognosis_(vertigo) Paroymsal  Positional Vertigo', 'prognosis_AIDS', 'prognosis_Acne', 'prognosis_Alcoholic hepatitis', 'prognosis_Allergy', 'prognosis_Arthritis', 'prognosis_Bronchial Asthma', 'prognosis_Cervical spondylosis', 'prognosis_Chicken pox', 'prognosis_Chronic cholestasis', 'prognosis_Common Cold', 'prognosis_Dengue', 'prognosis_Diabetes ', 'prognosis_Dimorphic hemmorhoids(piles)', 'prognosis_Drug Reaction', 'prognosis_Fungal infection', 'prognosis_GERD', 'prognosis_Gastroenteritis', 'prognosis_Heart attack', 'prognosis_Hepatitis B', 'prognosis_Hepatitis C', 'prognosis_Hepatitis D', 'prognosis_Hepatitis E', 'prognosis_Hypertension ', 'prognosis_Hyperthyroidism', 'prognosis_Hypoglycemia', 'prognosis_Hypothyroidism', 'prognosis_Impetigo', 'prognosis_Jaundice', 'prognosis_Malaria', 'prognosis_Migraine', 'prognosis_Osteoarthristis', 'prognosis_Paralysis (brain hemorrhage)', 'prognosis_Peptic ulcer diseae', 'prognosis_Pneumonia', 'prognosis_Psoriasis', 'prognosis_Tuberculosis', 'prognosis_Typhoid', 'prognosis_Urinary tract infection', 'prognosis_Varicose veins', 'prognosis_hepatitis A', 'Hydrocortisone cream', 'Atenolol', 'Orlistat', 'Supportive care', 'Balm', 'Hydrocortisone', 'Oral contraceptives', 'Vitamin B12 supplements', 'Latanoprost', 'Levocetirizine', 'NSAIDs', 'Biotin', 'Levothyroxine', 'PrEP', 'Artificial tears', 'Cyproheptadine', 'Lidocaine ointment', 'Thiamine', 'Lidocaine', 'N-acetylcysteine', 'Loperamide', 'Speech therapy', 'Dicyclomine', 'Beta-blockers', 'Magnesium supplements', 'Hepatitis B vaccination', 'Bilirubin', 'Nifedipine', 'Amoxicillin', 'Topical steroids', 'Polyethylene glycol', 'Ibuprofen', 'Vitamins', 'Fluoxetine', 'Metoclopramide', 'Clindamycin', 'Metformin', 'Diazepam', 'Ceftriaxone', 'Aspirin', 'Pseudoephedrine', 'Iron supplements', 'Antibiotics', 'Furosemide', 'Phenobarbital', 'Clopidogrel', 'Mesalamine', 'Physiotherapy', 'Antipsychotics', 'Vitamin C', 'Acetaminophen', 'Genetic counseling', 'Pantoprazole', 'Cetirizine', 'Naproxen', 'Alprazolam', 'Phenazopyridine', 'Moisturizers', 'Compression therapy', 'Guaifenesin', 'Paracetamol', 'Mirtazapine', 'Antihistamine eye drops', 'Antifungals', 'Antihistamines', 'Mupirocin', 'Simethicone', 'Modafinil', 'Oral Rehydration Salts', 'Protein Supplements', 'Albuterol', 'Eye drops', 'Kenalog', 'Coal tar', 'Laxatives', 'Parkinson medications', 'Dextromethorphan', 'Betahistine', 'Lozenges', 'Oxybutynin', 'Phenylephrine', 'Salicylic acid', 'Ondansetron', 'Corticosteroids', 'Atropine', 'Electrolytes', 'Vitamin B12', 'Ranitidine', 'Phentermine', 'Piracetam', 'Prednisolone', 'Nitrofurantoin', 'Clonazepam', 'Desmopressin', 'Multivitamins']

def encode_symptoms(input_symptoms, all_symptoms):
    encoded_symptoms = np.zeros(len(all_symptoms))
    for symptom in input_symptoms:
        if symptom in all_symptoms:
            index = all_symptoms.index(symptom)
            encoded_symptoms[index] = 1
    return encoded_symptoms.reshape(1, -1)

# Streamlit UI components
st.title("The Symptom Solver AI")
st.write("An AI-powered system for disease and medicine prediction based on symptoms.")

selected_symptoms = st.multiselect("Select Symptoms", options=all_symptoms)

# Prepare symptoms for encoding
input_symptoms = selected_symptoms

# Predict button
if st.button("Predict"):
    # Encode input symptoms
    symptom_input = encode_symptoms(input_symptoms, all_symptoms)

    # Predict using the model
    Y_pred = model.predict(symptom_input)

    # Process the output
    predicted_medicines = (Y_pred > 0.5).astype(int)
    predicted_medicine_labels = [medicines[i] for i, pred in enumerate(predicted_medicines[0]) if pred]

    # Separate disease name and recommended medicines
    disease_name = None
    recommended_medicines = []

    # Identify disease or prognosis label if it exists
    for label in predicted_medicine_labels:
        if label.lower().startswith("prognosis"):
            disease_name = label.split("_", 1)[-1]  # Extract actual disease name
        else:
            recommended_medicines.append(label)

    # If no specific disease found, assign "Unknown condition"
    if not disease_name:
        disease_name = "Unknown condition"

    # Output results
    st.subheader("Predicted Disease:")
    st.write(disease_name)

    st.subheader("Recommended Medicines:")
    if recommended_medicines:
        for medicine in recommended_medicines:
            st.write(medicine)
    else:
        st.write("No medicines recommended")
