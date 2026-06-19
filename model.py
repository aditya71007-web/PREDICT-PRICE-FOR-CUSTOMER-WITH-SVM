import numpy as np
import pandas as pd
from sklearn.svm import SVC

# Training Data
data = {
    'age': [25, 30, 35, 40, 45],
    'monthly_charge': [50, 60, 70, 80, 90],
    'churn': [0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[['age', 'monthly_charge']]
y = df['churn']

# Train SVM Model
svc_model = SVC(kernel='linear', C=1.0)
svc_model.fit(X, y)


def predict_churn(age: int, monthly_charge: float):
    user_input = np.array([[age, monthly_charge]])

    prediction = svc_model.predict(user_input)[0]

    if prediction == 0:
        message = "You are not likely to churn."
    else:
        message = "You are likely to churn."

    return int(prediction), message