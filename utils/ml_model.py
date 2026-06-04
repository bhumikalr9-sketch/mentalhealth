import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score, r2_score


# -----------------------------------
# DEPRESSION MODEL
# -----------------------------------

def train_depression_model(df):

    features = [
        "age",
        "sleep_hours",
        "daily_social_media_hours",
        "stress_level",
        "anxiety_level",
        "addiction_level"
    ]

    target = "depression_label"

    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    return model, accuracy


def predict_depression(
    model,
    age,
    sleep_hours,
    social_media_hours,
    stress_level,
    anxiety_level,
    addiction_level
):

    data = pd.DataFrame({
        "age": [age],
        "sleep_hours": [sleep_hours],
        "daily_social_media_hours": [social_media_hours],
        "stress_level": [stress_level],
        "anxiety_level": [anxiety_level],
        "addiction_level": [addiction_level]
    })

    prediction = model.predict(data)[0]

    return prediction


# -----------------------------------
# RISK MODEL
# -----------------------------------

def train_risk_model(df):

    features = [
        "age",
        "sleep_hours",
        "daily_social_media_hours",
        "stress_level",
        "anxiety_level",
        "addiction_level"
    ]

    target = "mental_health_risk_score"

    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    score = r2_score(
        y_test,
        predictions
    )

    return model, score


def predict_risk_score(
    model,
    age,
    sleep_hours,
    social_media_hours,
    stress_level,
    anxiety_level,
    addiction_level
):

    data = pd.DataFrame({
        "age": [age],
        "sleep_hours": [sleep_hours],
        "daily_social_media_hours": [social_media_hours],
        "stress_level": [stress_level],
        "anxiety_level": [anxiety_level],
        "addiction_level": [addiction_level]
    })

    prediction = model.predict(data)[0]

    return float(prediction)
