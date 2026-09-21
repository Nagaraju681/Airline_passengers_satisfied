
# ✈️ Airline Passenger Satisfaction Prediction

## 📌 Project Overview

Airline Passenger Satisfaction Prediction is a Machine Learning project that predicts whether an airline passenger is satisfied or dissatisfied based on their travel experience, service ratings, and personal information.

The project includes data preprocessing, Exploratory Data Analysis (EDA), Machine Learning model training, and a Streamlit web application for real-time passenger satisfaction prediction.

The main objective is to analyze passenger feedback and build a Machine Learning model that helps predict customer satisfaction.

---

## 🎯 Objectives

- Analyze airline passenger satisfaction data.
- Perform data cleaning and preprocessing.
- Conduct Exploratory Data Analysis (EDA).
- Identify factors affecting passenger satisfaction.
- Train a Machine Learning classification model.
- Evaluate model performance.
- Build a Streamlit application for predictions.

---

## 📊 Dataset

**Dataset:** Airline Passenger Satisfaction

The dataset contains passenger information, travel details, service ratings, and satisfaction labels.

### Important Features

- Gender
- Customer Type
- Age
- Type of Travel
- Class
- Flight Distance
- Inflight Wi-Fi Service
- Departure/Arrival Time Convenience
- Ease of Online Booking
- Food and Drink
- Online Boarding
- Seat Comfort
- Inflight Entertainment
- Baggage Handling
- Check-in Service
- Cleanliness
- Departure Delay
- Arrival Delay
- Satisfaction (Target)

The target variable is:

- `Satisfaction`: Satisfied or dissatisfied passenger.

---

## 🔄 Project Workflow

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Feature Selection
     ↓
Train-Test Split
     ↓
Data Preprocessing
     ↓
Machine Learning Model
     ↓
Model Evaluation
     ↓
Streamlit Deployment
     ↓
Passenger Satisfaction Prediction
```

---

## 🧹 Data Preprocessing

The following preprocessing techniques were applied as required by the dataset and model pipeline:

- Handling missing values
- Separating input features and target variable
- Encoding categorical features
- Preparing numerical features
- Train-test split
- Feature transformation
- Preparing data for Machine Learning

The project uses a saved transformer to preprocess input data before prediction.

---

## 🔍 Exploratory Data Analysis (EDA)

EDA was performed to understand passenger satisfaction patterns.

### Analysis Includes

- Passenger satisfaction distribution
- Customer type analysis
- Travel class comparison
- Flight distance analysis
- Service rating analysis
- Age distribution
- Departure and arrival delays
- Relationship between passenger features and satisfaction

EDA helps identify patterns in passenger experience and satisfaction.

---

## 🤖 Machine Learning

### Model Used

**Random Forest Classifier**

Random Forest is a supervised Machine Learning classification algorithm that combines multiple decision trees to make predictions.

The model is trained to classify passengers into:

- Satisfied
- Dissatisfied

### Model Files

- `rf_model_f.pkl` – Trained Machine Learning model
- `transformer.pkl` – Saved feature preprocessing transformer

> The model and transformer filenames correspond to the deployed project artifacts.

---

## 📈 Model Evaluation

The model can be evaluated using the following metrics:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

### Evaluation Results

Add your actual evaluation results below:

| Metric | Score |
|---|---|
| Accuracy | Add actual value |
| Precision | Add actual value |
| Recall | Add actual value |
| F1-Score | Add actual value |

> Replace the placeholder values with the results from your trained model. Do not add estimated metrics.

---

## 💻 Technologies Used

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

### Concepts

- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Categorical Encoding
- Machine Learning Classification
- Model Evaluation
- Model Deployment

---

## 📂 Project Structure

```text
Airline-Passenger-Satisfaction/
│
├── app.py
├── rf_model_f.pkl
├── transformer.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Nagaraju681/Airline-Passenger-Satisfaction.git
```

### 2. Navigate to the Project Directory

```bash
cd Airline-Passenger-Satisfaction
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application Locally

Run the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your browser.

Enter the required passenger details and click the prediction button to view the satisfaction prediction.

---

## 🔮 Example Prediction

### Input

Passenger details such as:

- Age
- Travel class
- Flight distance
- Service ratings
- Travel type

### Output

```text
Predicted Satisfaction: Satisfied
```

> The prediction depends on the input features and the trained model.

---

## 🚀 Deployment

The Machine Learning model is integrated into a Streamlit web application.

### Deployment Platform

- Streamlit Community Cloud

### Deployment Steps

1. Upload the project to GitHub.
2. Connect the GitHub repository to Streamlit Cloud.
3. Select `app.py` as the main file.
4. Install dependencies using `requirements.txt`.
5. Deploy the application.

### Live Demo

Add your Streamlit application URL here:

```text
Coming Soon
```

---

## 📌 Key Learnings

Through this project, I gained practical experience in:

- Python programming
- Data preprocessing
- Exploratory Data Analysis
- Handling categorical data
- Machine Learning classification
- Model evaluation
- Saving and loading ML models
- Streamlit application development
- Model deployment
- Building an end-to-end Machine Learning project

---

## 🚀 Future Improvements

- Improve model performance through hyperparameter tuning.
- Add more detailed EDA visualizations.
- Improve the Streamlit user interface.
- Add prediction probability.
- Monitor model performance.
- Explore additional Machine Learning algorithms.

---

## 👨‍💻 Author

**Nagaraju**

Aspiring Data Analyst | Data Scientist | Machine Learning Enthusiast

### 🔗 GitHub

https://github.com/Nagaraju681

---

## ⭐ Project Feedback

If you find this project useful, feel free to explore the repository and share feedback.
