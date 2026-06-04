# pages/4_Mental_Health_Insights.py

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from utils.data_loader import load_data

# ---------------------------------------
# PAGE CONFIG
# ---------------------------------------

st.set_page_config(
    page_title="Mental Health Insights",
    page_icon="🧠",
    layout="wide"
)

# ---------------------------------------
# LOAD DATA
# ---------------------------------------

@st.cache_data
def get_data():
    return load_data("Teen_Mental_Health.csv")

df = get_data()

# ---------------------------------------
# TITLE
# ---------------------------------------

st.title("🧠 Mental Health Insights Dashboard")

st.markdown("""
Deep analysis of stress, anxiety,
depression risk, addiction behavior,
and overall mental wellbeing.
""")

st.markdown("---")

# ---------------------------------------
# KPI SECTION
# ---------------------------------------

avg_stress = round(
    df["stress_level"].mean(),
    2
)

avg_anxiety = round(
    df["anxiety_level"].mean(),
    2
)

avg_addiction = round(
    df["addiction_level"].mean(),
    2
)

avg_risk = round(
    df["mental_health_risk_score"].mean(),
    2
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Stress Level",
    avg_stress
)

col2.metric(
    "Anxiety Level",
    avg_anxiety
)

col3.metric(
    "Addiction Level",
    avg_addiction
)

col4.metric(
    "Risk Score",
    avg_risk
)

st.markdown("---")

# ---------------------------------------
# STRESS ANALYSIS
# ---------------------------------------

st.subheader("😫 Stress Analysis")

fig = px.histogram(
    df,
    x="stress_level",
    nbins=15,
    title="Stress Level Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------
# ANXIETY ANALYSIS
# ---------------------------------------

st.subheader("😟 Anxiety Analysis")

fig = px.histogram(
    df,
    x="anxiety_level",
    nbins=15,
    title="Anxiety Level Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------
# ADDICTION ANALYSIS
# ---------------------------------------

st.subheader("📱 Social Media Addiction")

fig = px.histogram(
    df,
    x="addiction_level",
    nbins=15,
    title="Addiction Level Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------
# RISK SCORE ANALYSIS
# ---------------------------------------

st.subheader("⚠ Mental Health Risk Score")

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

# ---------------------------------------
# STRESS VS ANXIETY
# ---------------------------------------

st.subheader("📈 Stress vs Anxiety")

fig = px.scatter(
    df,
    x="stress_level",
    y="anxiety_level",
    color="gender",
    title="Stress Level vs Anxiety Level"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------
# STRESS VS RISK SCORE
# ---------------------------------------

st.subheader("📊 Stress vs Risk Score")

fig = px.scatter(
    df,
    x="stress_level",
    y="mental_health_risk_score",
    color="gender",
    title="Stress Level vs Mental Health Risk"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------
# ANXIETY VS RISK SCORE
# ---------------------------------------

st.subheader("📊 Anxiety vs Risk Score")

fig = px.scatter(
    df,
    x="anxiety_level",
    y="mental_health_risk_score",
    color="gender",
    title="Anxiety Level vs Mental Health Risk"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------
# GENDER COMPARISON
# ---------------------------------------

st.subheader("👥 Gender Comparison")

col1, col2 = st.columns(2)

with col1:

    fig = px.box(
        df,
        x="gender",
        y="stress_level",
        color="gender",
        title="Stress by Gender"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    fig = px.box(
        df,
        x="gender",
        y="anxiety_level",
        color="gender",
        title="Anxiety by Gender"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ---------------------------------------
# AGE-WISE ANALYSIS
# ---------------------------------------

st.subheader("🎂 Age-wise Mental Health")

age_stats = (
    df.groupby("age")
    [
        "stress_level",
        "anxiety_level",
        "mental_health_risk_score"
    ]
    .mean()
    .reset_index()
)

fig = px.line(
    age_stats,
    x="age",
    y=[
        "stress_level",
        "anxiety_level",
        "mental_health_risk_score"
    ],
    markers=True,
    title="Mental Health Indicators by Age"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------
# DEPRESSION ANALYSIS
# ---------------------------------------

if "depression_label" in df.columns:

    st.subheader("🧠 Depression Analysis")

    depression_counts = (
        df["depression_label"]
        .value_counts()
        .reset_index()
    )

    depression_counts.columns = [
        "Status",
        "Count"
    ]

    fig = px.pie(
        depression_counts,
        names="Status",
        values="Count",
        title="Depression Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ---------------------------------------
# RADAR CHART
# ---------------------------------------

st.subheader("🎯 Mental Health Radar")

categories = [
    "Stress",
    "Anxiety",
    "Addiction",
    "Risk Score"
]

values = [
    avg_stress,
    avg_anxiety,
    avg_addiction,
    avg_risk
]

fig = go.Figure()

fig.add_trace(
    go.Scatterpolar(
        r=values,
        theta=categories,
        fill="toself",
        name="Average Metrics"
    )
)

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True
        )
    ),
    showlegend=False
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------
# CORRELATION HEATMAP
# ---------------------------------------

st.subheader("🔥 Correlation Heatmap")

corr_cols = [
    "daily_social_media_hours",
    "sleep_hours",
    "stress_level",
    "anxiety_level",
    "addiction_level",
    "mental_health_risk_score"
]

corr_matrix = df[corr_cols].corr()

fig = px.imshow(
    corr_matrix,
    text_auto=True,
    title="Mental Health Correlations"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------
# RISK SEGMENTATION
# ---------------------------------------

st.subheader("🚨 Risk Segmentation")

def risk_category(score):

    if score < 25:
        return "Low"

    elif score < 50:
        return "Moderate"

    elif score < 75:
        return "High"

    return "Critical"

risk_df = df.copy()

risk_df["Risk Category"] = (
    risk_df["mental_health_risk_score"]
    .apply(risk_category)
)

risk_counts = (
    risk_df["Risk Category"]
    .value_counts()
    .reset_index()
)

risk_counts.columns = [
    "Category",
    "Count"
]

fig = px.bar(
    risk_counts,
    x="Category",
    y="Count",
    title="Risk Categories"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------
# EXECUTIVE INSIGHTS
# ---------------------------------------

st.markdown("---")

st.subheader("💡 Executive Insights")

st.success(
    f"Average Stress Level: {avg_stress}"
)

st.success(
    f"Average Anxiety Level: {avg_anxiety}"
)

st.success(
    f"Average Addiction Level: {avg_addiction}"
)

st.warning(
    f"Average Mental Health Risk Score: {avg_risk}"
)

high_risk = len(
    df[
        df["mental_health_risk_score"] >= 75
    ]
)

st.error(
    f"High Risk Students: {high_risk}"
)

# ---------------------------------------
# DATA PREVIEW
# ---------------------------------------

st.markdown("---")

st.subheader("📄 Dataset Preview")

st.dataframe(
    df.head(20),
    use_container_width=True
)

# ---------------------------------------
# FOOTER
# ---------------------------------------

st.markdown("---")

st.caption(
    "Teen Mental Health Analytics Dashboard | Mental Health Insights"
)
