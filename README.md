# Diabetes Prediction 🩺

A machine learning project for predicting the likelihood of diabetes based on patient health measurements. The project uses a diabetes dataset, standardizes the input features with `StandardScaler`, and trains a **Support Vector Machine (SVM)** classification model.

The repository also includes a simple Arabic web interface and a **FastAPI** backend for sending patient data and receiving prediction results.

> ⚠️ **Disclaimer:** This project is for educational purposes only and is not a medical diagnostic tool. Do not use its predictions as a substitute for professional medical advice or clinical testing.

## Features

- Exploratory data analysis using Python and Jupyter Notebook.
- Diabetes classification using an SVM model.
- Feature standardization with `StandardScaler`.
- FastAPI endpoint for making predictions through `/api/predict`.
- Simple web interface for entering patient data and displaying the result.
- Model and scaler loading using `joblib`.

## Project Structure

```text
Diabetes_Prediction/
├── Diabetes Prediction.ipynb   # Data analysis and model training
├── diabetes.csv                # Diabetes dataset
├── predictor.py                # Model loading and prediction logic
├── app.py                      # FastAPI application and API endpoint
├── index.html                  # Web user interface
├── .gitignore
└── README.md
```

## Dataset

The project uses the **Pima Indians Diabetes Dataset**, which contains 768 records, 8 input features, and one target column named `Outcome`.

### Input Features

| Feature | Description |
|---|---|
| `Pregnancies` | Number of pregnancies |
| `Glucose` | Plasma glucose concentration |
| `BloodPressure` | Diastolic blood pressure |
| `SkinThickness` | Triceps skin fold thickness |
| `Insulin` | 2-Hour serum insulin level |
| `BMI` | Body mass index |
| `DiabetesPedigreeFunction` | Diabetes pedigree function |
| `Age` | Age in years |
| `Outcome` | Target: `0` = non-diabetic, `1` = diabetic |

## Requirements

- Python 3.9 or later
- pip
- Jupyter Notebook (optional, for running the analysis notebook)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Ibraheem902/Diabetes_Prediction.git
cd Diabetes_Prediction
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment.

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

4. Install the required dependencies:

```bash
pip install fastapi uvicorn pandas numpy scikit-learn joblib jupyter
```

## Running the Notebook

Open the Jupyter Notebook:

```bash
jupyter notebook "Diabetes Prediction.ipynb"
```

The notebook covers the following steps:

1. Load the `diabetes.csv` dataset.
2. Explore and analyze the data.
3. Separate the features from the target labels.
4. Standardize the features using `StandardScaler`.
5. Split the data into training and testing sets using an 80/20 ratio.
6. Train an SVM model using `SVC(kernel="linear")`.
7. Evaluate the model using `accuracy_score`.

## Running the API

Before starting the API, make sure the following model files exist in the project root:

```text
diabetes_model.pkl
scaler.pkl
```

The `predictor.py` file loads these files when the application starts. Run the FastAPI server with:

```bash
uvicorn app:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## API Usage

### Endpoint

```http
POST /api/predict
```

### Example Request

```json
{
  "Pregnancies": 1,
  "Glucose": 120,
  "BloodPressure": 70,
  "SkinThickness": 20,
  "Insulin": 79,
  "BMI": 25.5,
  "DiabetesPedigreeFunction": 0.5,
  "Age": 30
}
```

### Example Response

```json
{
  "status": "success",
  "data": {
    "prediction": 0,
    "result": "Non-Diabetic"
  }
}
```

Possible prediction values:

- `prediction: 0` — Non-Diabetic
- `prediction: 1` — Diabetic

## Running the Web Interface

After starting the FastAPI server, open `index.html` in your browser. The web interface sends requests to:

```text
http://127.0.0.1:8000/api/predict
```

If you see a connection error, make sure the FastAPI server is running first.

## Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Scikit-learn
- FastAPI
- Uvicorn
- Joblib
- HTML and JavaScript

## Project Limitations

- Predictions are estimates based on a limited training dataset.
- Zero values in some medical features may represent missing values rather than actual measurements.
- The model should not be used to make medical decisions.
- The files `diabetes_model.pkl` and `scaler.pkl` must be available before running the API.

## Contributing

Contributions are welcome. To contribute:

1. Fork the repository.
2. Create a new branch for your changes.
3. Commit your changes with a clear message.
4. Open a Pull Request describing your contribution.

## License

No license has been specified for this project yet.

## Repository

[Diabetes Prediction on GitHub](https://github.com/Ibraheem902/Diabetes_Prediction)
