import pandas as pd
import joblib
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load model and scaler
model = joblib.load(os.path.join(BASE_DIR, "StressLevel.pkl"))

# Testing;
new_data = {
    "anxiety_level": 20,          # very high
    "self_esteem": 1,            # very low
    "mental_health_history": 1,  # history present
    "depression": 10,             # very high
    "headache": 0,
    "blood_pressure": 120,       # high
    "sleep_quality": 1,          # very poor
    "breathing_problem": 1,
    "noise_level": 20,
    "living_conditions": 2,
    "safety": 2,
    "basic_needs": 2,
    "academic_performance": 3,   # struggling
    "study_load": 2,             # overloaded
    "teacher_student_relationship": 2,
    "future_career_concerns": 9, # very worried
    "social_support": 1,
    "peer_pressure": 9,
    "extracurricular_activities": 1,
    "bullying": 1
}
def predict_std_stress_level(new_data):

    # Convert into DataFrame
    X_new = pd.DataFrame([new_data])

    # Ensure same column order as training
    X_new = X_new[model.feature_names_in_]

    # Predict
    pred_class = model.predict(X_new)[0]
    pred_prob  = model.predict_proba(X_new)[0]
    class_prob = pred_prob[pred_class] * 100
    # print("Predicted class:", pred_class)   # 0 = did not survive, 1 = survived
    # print("Predicted probabilities:", class_prob,"%")
    # If your model returns probabilities for multiple classes, check all
    pred_prob_all = model.predict_proba(X_new)[0]  # Get probabilities for all classes
    print(f"All class probabilities: {pred_prob_all}")
    return pred_class, class_prob

# print("Inside script")
# pred_class, class_prob = predict_std_stress_level(new_data)
# print(f"Predicted Standardized Stress Level: {pred_class} with probability {class_prob:.2f}%")

# print("Predicted Standardized Stress:", end=" ")
# print(predict_std_stress_level(new_data))
def get_model_performance():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(BASE_DIR, "metrics.json"), "r") as f:
        metrics = json.load(f)   # loads into a Python dict
    return metrics


# Example usage
# print("Model Performance Metrics:")
# print(get_model_performance()['accuracy'])
# print(get_model_performance()['precision'])
# print(get_model_performance()['recall'])
# print(get_model_performance()['f1'])

# This block will only run when executing this file directly (e.g. python titanic_predict.py)
if __name__ == "__main__":
    # test code (won’t run in Django)
    predict_std_stress_level(new_data)
    get_model_performance()