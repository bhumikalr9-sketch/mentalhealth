import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_data
from utils.ml_model import (
    train_risk_model,
    predict_risk_score
)

# ------------------------------------
# PAGE CONFIG
# ------------------------------------

st.set_page_config(
    page_title="Risk Assessment",
    page_icon="⚠",
    layout="wide"
)

# ------------------------------------
# LOAD DATA
# ------------------------------------

@st.cache_data
def get_data():
    return load_data("Teen_Mental_Health.csv")

df = get_data()

# ------------------------------------
# TRAIN MODEL
# ------------------------------------

model, model_score = train_risk_model(df)

# ------------------------------------
# TITLE
# ------------------------------------

st.title("⚠ Mental Health Risk Assessment")

st.markdown("""
Predict overall mental health risk based on
sleep, social media usage, anxiety, stress,
and addiction indicators.
""")

st.markdown("---")

# ------------------------------------
# MODEL PERFORMANCE
# ------------------------------------

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Model Accuracy (R²)",
        f"{model_score:.2f}"
    )

with col2:
    st.metric(
        "Dataset Records",
        len(df)
    )

st.markdown("---")

# ------------------------------------
# USER INPUT
# ------------------------------------

st.subheader("📝 Enter Student Information")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=13,
        max_value=19,
        value=16
    )

    sleep_hours = st.slider(
        "Sleep Hours",
        3.0,
        12.0,
        7.0
    )

    social_media_hours = st.slider(
        "Daily Social Media Hours",
        0.0,
        15.0,
        5.0
    )

with col2:

    stress_level = st.slider(
        "Stress Level",
        1,
        10,
        5
    )

    anxiety_level = st.slider(
        "Anxiety Level",
        1,
        10,
        5
    )

    addiction_level = st.slider(
        "Addiction Level",
        1,
        10,
        5
    )

# ------------------------------------
# PREDICTION
# ------------------------------------

if st.button("🔍 Assess Risk"):

    risk_score = predict_risk_score(
        model,
        age,
        sleep_hours,
        social_media_hours,
        stress_level,
        anxiety_level,
        addiction_level
    )

    st.markdown("---")

    st.subheader("📊 Prediction Result")

    st.metric(
        "Predicted Risk Score",
        round(risk_score, 2)
    )

    # --------------------------------
    # RISK CATEGORY
    # --------------------------------

    if risk_score < 25:

        st.success(
            "🟢 Low Risk"
        )

        risk_level = "Low"

    elif risk_score < 50:

        st.warning(
            "🟡 Moderate Risk"
        )

        risk_level = "Moderate"

    elif risk_score < 75:

        st.error(
            "🟠 High Risk"
        )

        risk_level = "High"

    else:

        st.error(
            "🔴 Critical Risk"
        )

        risk_level = "Critical"

    # --------------------------------
    # GAUGE CHART
    # --------------------------------

    gauge_df = pd.DataFrame({
        "Category": ["Risk Score"],
        "Value": [risk_score]
    })

    fig = px.bar(
        gauge_df,
        x="Category",
        y="Value",
        title="Risk Score Visualization"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # --------------------------------
    # INSIGHTS
    # --------------------------------

    st.subheader("💡 Personalized Insights")

    if sleep_hours < 6:
        st.warning(
            "Low sleep duration may increase mental health risks."
        )

    if social_media_hours > 6:
        st.warning(
            "High social media usage detected."
        )

    if stress_level >= 7:
        st.error(
            "Stress level is significantly elevated."
        )

    if anxiety_level >= 7:
        st.error(
            "Anxiety level is significantly elevated."
        )

    if addiction_level >= 7:
        st.error(
            "Signs of social media addiction detected."
        )

    st.info(
        f"Overall Risk Category: {risk_level}"
    )

st.markdown("---")

# ------------------------------------
# FEATURE IMPORTANCE
# ------------------------------------

st.subheader("📈 Feature Importance")

try:

    feature_names = [
        "Age",
        "Sleep Hours",
        "Social Media Hours",
        "Stress Level",
        "Anxiety Level",
        "Addiction Level"
    ]

    importance_df = pd.DataFrame({
        "Feature": feature_names,
        "Importance": model.feature_importances_
    })

    importance_df = importance_df.sort_values(
        by="Importance",
        ascending=False
    )

    fig = px.bar(
        importance_df,
        x="Importance",
        y="Feature",
        orientation="h",
        title="Factors Influencing Risk Score"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

except:
    st.info(
        "Feature importance unavailable."
    )

# ------------------------------------
# RISK DISTRIBUTION
# ------------------------------------

if "mental_health_risk_score" in df.columns:

    st.markdown("---")

    st.subheader("📊 Dataset Risk Distribution")

    fig = px.histogram(
        df,
        x="mental_health_risk_score",
        nbins=20,
        title="Mental Health Risk Score Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ------------------------------------
# DATA PREVIEW
# ------------------------------------

st.markdown("---")

st.subheader("📄 Dataset Preview")

st.dataframe(
    df.head(20),
    use_container_width=True
)

# ------------------------------------
# FOOTER
# ------------------------------------

st.markdown("---")

st.caption(
    "Teen Mental Health Analytics Dashboard | Risk Assessment Module"
)
