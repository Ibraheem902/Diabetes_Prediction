import joblib
import pandas as pd

class DiabetesPredictor:
    def __init__(self, model_path='diabetes_model.pkl', scaler_path='scaler.pkl'):
        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path)

        self.feature_names = [
            'Pregnancies', 'Glucose', 'BloodPressure', 
            'SkinThickness', 'Insulin', 'BMI', 
            'DiabetesPedigreeFunction', 'Age'
        ]
    
    def predict(self, input_data):
        df = pd.DataFrame([input_data], columns=self.feature_names)
        std_data = self.scaler.transform(df)
        print("\n--- DEBUG INFO ---")
        print("Raw Features Input:", input_data)
        print("Scaled Data:", std_data)
        prediction = self.model.predict(std_data)
        
        return{
            'prediction': int(prediction[0]),
            'result': 'Diabetic' if prediction[0] == 1 else 'Non-Diabetic'
        }