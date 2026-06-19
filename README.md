# Customer Churn Prediction API using FastAPI and SVM

## Overview

This project is a Machine Learning web application that predicts whether a customer is likely to churn based on their age and monthly charge. The model is built using the Support Vector Machine (SVM) algorithm and deployed using FastAPI. A simple HTML frontend is provided to interact with the API.

---

## Features

* Customer churn prediction using SVM
* REST API built with FastAPI
* Interactive HTML user interface
* JSON request and response handling
* CORS enabled for frontend integration

---

## Technologies Used

* Python
* FastAPI
* Scikit-learn
* NumPy
* Pandas
* HTML
* JavaScript

---

## Project Structure

```
customer_churn/
│
├── main.py
├── model.py
├── schema.py
├── index.html
├── requirements.txt
└── README.md
```

---

## Dataset

The model is trained on a sample dataset containing:

| Age | Monthly Charge | Churn |
| --- | -------------- | ----- |
| 25  | 50             | 0     |
| 30  | 60             | 0     |
| 35  | 70             | 1     |
| 40  | 80             | 1     |
| 45  | 90             | 1     |

Where:

* `0` = Customer is not likely to churn
* `1` = Customer is likely to churn

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/customer-churn-api.git
cd customer-churn-api
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux/Mac

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the FastAPI Server

```bash
python -m uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

API documentation:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoint

### Predict Customer Churn

**Endpoint**

```
POST /predict
```

**Request Body**

```json
{
  "age": 32,
  "monthly_charge": 65
}
```

**Response**

```json
{
  "prediction": 0,
  "message": "You are not likely to churn."
}
```

---

## Frontend

Open `index.html` in your browser and enter:

* Customer Age
* Monthly Charge

Click the **Predict** button to get the churn prediction result.

---

## Example Predictions

| Age | Monthly Charge | Prediction          |
| --- | -------------- | ------------------- |
| 28  | 55             | Not Likely to Churn |
| 42  | 85             | Likely to Churn     |

---

## Future Improvements

* Train on a larger real-world dataset
* Store the trained model using Pickle
* Improve UI using Bootstrap or React
* Deploy using Docker and Render
* Add model evaluation metrics and visualizations

---

## Author

**Aditya Kumar**

Machine Learning and Full Stack Developer

GitHub: https://github.com/aditya71007-web

