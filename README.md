# ⚡ Energy Load Forecasting

A machine learning project for **24-hour-ahead electricity load forecasting** using the PJM hourly energy consumption dataset.

The project covers the complete ML workflow, including exploratory data analysis, feature engineering, model development, evaluation, and deployment using Streamlit.

## 🎯 Project Overview

Electricity load forecasting is an important task in energy management, helping predict future electricity demand based on historical consumption patterns.

The objective of this project is to predict electricity consumption 24 hours ahead using historical load observations and calendar-based features.

| Property | Description |
|---|---|
| Dataset | PJM Hourly Energy Consumption |
| Target variable | `PJME_MW` |
| Task | Supervised Regression |
| Forecasting horizon | 24 hours ahead |
| Selected model | XGBoost |
| Deployment | Streamlit + Docker |

## 🔬 Methodology

### 1. Exploratory Data Analysis

The dataset was explored to understand electricity consumption patterns and identify relevant characteristics of the time series.

The analysis included:
- Time series visualization
- Distribution and outlier analysis
- Daily, weekly, and yearly seasonality
- Seasonal decomposition
- Autocorrelation (ACF) and partial autocorrelation (PACF)
- Augmented Dickey-Fuller (ADF) stationarity test

### 2. Feature Engineering

Seven features were selected for the final XGBoost model.

| Feature | Description |
|---|---|
| `hour` | Hour of the day |
| `dayofweek` | Day of the week |
| `month` | Month of the year |
| `lag_24` | Electricity load 24 hours earlier |
| `lag_48` | Electricity load 48 hours earlier |
| `lag_144` | Electricity load 144 hours earlier |
| `lag_168` | Electricity load 168 hours earlier |

Calendar features capture temporal patterns, while lag features provide historical electricity consumption information.

### 3. Model Development

Several approaches were evaluated and compared:

- Baseline models
- Linear Regression
- XGBoost
- CatBoost

XGBoost was selected for the deployment stage. CatBoost was used for experimentation and model comparison.

### 4. Model Evaluation

Model performance was evaluated using two regression metrics:

- **MAE (Mean Absolute Error)** — measures the average absolute difference between actual and predicted values.
- **RMSE (Root Mean Squared Error)** — measures prediction errors while penalizing larger errors more heavily.

## 🖥️ Streamlit Application

The project includes an interactive Streamlit application that loads the trained XGBoost model and generates electricity load predictions.

Users can manually enter:
- Calendar features: hour, day of the week, and month.
- Historical load values: 24, 48, 144, and 168 hours before the forecasted time.

The application uses these seven input features to generate a predicted electricity load in MW.

## 🚀 Getting Started

There are two ways to run the application.

### Option 1: Run Locally (Without Docker)

Make sure Python is installed.

Navigate to the application directory:

```bash
cd pjm
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

Open the application in your browser:

```text
http://localhost:8501
```

### Option 2: Run with Docker

Make sure Docker Desktop is installed and running.

Navigate to the application directory:

```bash
cd pjm
```

Build the Docker image:

```bash
docker build -t pjm-load-forecast .
```

Run the container:

```bash
docker run --rm -p 8501:8501 pjm-load-forecast
```

Open the application in your browser:

```text
http://localhost:8501
```

## 📁 Project Structure

```text
energy-load-forecasting/
│
├── notebook.ipynb          # EDA, feature engineering and model development
├── PJME_hourly.csv         # Original PJM hourly dataset
├── README.md               # Project documentation
├── .gitignore
│
└── pjm/
    ├── app.py              # Streamlit application
    ├── xgboost_model.bin   # Trained XGBoost model
    ├── requirements.txt    # Application dependencies
    └── Dockerfile          # Docker configuration
```

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn, XGBoost, CatBoost |
| Time Series Analysis | Statsmodels, Prophet |
| Application | Streamlit |
| Containerization | Docker |

## 🔮 Future Improvements

- Automate historical feature generation.
- Integrate regularly updated electricity load data.
- Implement automated model retraining.
- Explore additional forecasting models and feature engineering techniques.
- Improve the application interface and forecasting workflow.