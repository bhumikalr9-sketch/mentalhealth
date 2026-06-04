# pages/3_Sleep_Analysis.py

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from utils.data_loader import load_data

# ---------------------------------------
# PAGE CONFIG
# ---------------------------------------

st.set_page_config(
    page_title="Sleep Analysis",
    page_icon="😴",
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

st.title("😴 Sleep Analysis Dashboard")

st.markdown("""
Analyze sleep patterns, sleep quality,
screen time habits, and their impact
on mental health.
""")

st.markdown("---")

# ---------------------------------------
# KPI SECTION
# ---------------------------------------

avg_sleep = round(
    df["sleep_hours"].mean(),
    2
)

max_sleep = round(
    df["sleep_hours"].max(),
    2
)

min_sleep = round(
    df["sleep_hours"].min(),
    2
)

poor_sleep_count = len(
    df[df["sleep_hours"] < 6]
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Avg Sleep",
    f"{avg_sleep} hrs"
)

col2.metric(
    "Max Sleep",
    f"{max_sleep} hrs"
)

col3.metric(
    "Min Sleep",
    f"{min_sleep} hrs"
)

col4.metric(
    "Poor Sleep Cases",
    poor_sleep_count
)

st.markdown("---")

# ---------------------------------------
# SLEEP DISTRIBUTION
# ---------------------------------------

st.subheader("📊 Sleep Hours Distribution")

fig = px.histogram(
    df,
    x="sleep_hours",
    nbins=20,
    title="Sleep Hours Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------
# SLEEP QUALITY
# ---------------------------------------

if "sleep_quality" in df.columns:

    st.subheader("🌙 Sleep Quality")

    sleep_quality = (
        df["sleep_quality"]
        .value_counts()
        .reset_index()
    )

    sleep_quality.columns = [
        "Quality",
        "Count"
    ]

    fig = px.pie(
        sleep_quality,
        names="Quality",
        values="Count",
        title="Sleep Quality Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ---------------------------------------
# SLEEP VS STRESS
# ---------------------------------------

st.subheader("😫 Sleep vs Stress")

fig = px.scatter(
    df,
    x="sleep_hours",
    y="stress_level",
    color="gender",
    title="Sleep Hours vs Stress Level"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------
# SLEEP VS ANXIETY
# ---------------------------------------

st.subheader("😟 Sleep vs Anxiety")

fig = px.scatter(
    df,
    x="sleep_hours",
    y="anxiety_level",
    color="gender",
    title="Sleep Hours vs Anxiety Level"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------
# SLEEP VS SOCIAL MEDIA
# ---------------------------------------

st.subheader("📱 Sleep vs Social Media")

fig = px.scatter(
    df,
    x="daily_social_media_hours",
    y="sleep_hours",
    color="gender",
    title="Social Media Usage vs Sleep Hours"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------
# SCREEN TIME BEFORE SLEEP
# ---------------------------------------

if "screen_time_before_sleep" in df.columns:

    st.subheader("📵 Screen Time Before Sleep")

    fig = px.histogram(
        df,
        x="screen_time_before_sleep",
        title="Screen Time Before Sleep"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ---------------------------------------
# SLEEP VS RISK SCORE
# ---------------------------------------

if "mental_health_risk_score" in df.columns:

    st.subheader("⚠ Sleep vs Mental Health Risk")

    fig = px.scatter(
        df,
        x="sleep_hours",
        y="mental_health_risk_score",
        color="gender",
        title="Sleep Hours vs Risk Score"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ---------------------------------------
# SLEEP VS DEPRESSION
# ---------------------------------------

if "depression_label" in df.columns:

    st.subheader("🧠 Sleep vs Depression")

    depression_sleep = (
        df.groupby("depression_label")
        ["sleep_hours"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        depression_sleep,
        x="depression_label",
        y="sleep_hours",
        title="Average Sleep Hours by Depression Status"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ---------------------------------------
# GENDER COMPARISON
# ---------------------------------------

st.subheader("👨‍🎓 Gender-wise Sleep Analysis")

fig = px.box(
    df,
    x="gender",
    y="sleep_hours",
    color="gender",
    title="Sleep Hours by Gender"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------
# AGE-WISE SLEEP ANALYSIS
# ---------------------------------------

st.subheader("🎂 Age-wise Sleep Patterns")

age_sleep = (
    df.groupby("age")
    ["sleep_hours"]
    .mean()
    .reset_index()
)

fig = px.line(
    age_sleep,
    x="age",
    y="sleep_hours",
    markers=True,
    title="Average Sleep Hours by Age"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------
# CORRELATION ANALYSIS
# ---------------------------------------

st.subheader("📈 Sleep Correlation Analysis")

corr_columns = [
    "sleep_hours",
    "daily_social_media_hours",
    "stress_level",
    "anxiety_level"
]

if "addiction_level" in df.columns:
    corr_columns.append(
        "addiction_level"
    )

if "mental_health_risk_score" in df.columns:
    corr_columns.append(
        "mental_health_risk_score"
    )

corr_matrix = df[corr_columns].corr()

fig = px.imshow(
    corr_matrix,
    text_auto=True,
    title="Sleep Related Correlations"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------
# EXECUTIVE INSIGHTS
# ---------------------------------------

st.markdown("---")

st.subheader("💡 Sleep Insights")

st.success(
    f"Average sleep duration is {avg_sleep} hours."
)

st.warning(
    f"{poor_sleep_count} students sleep less than 6 hours."
)

if "mental_health_risk_score" in df.columns:

    avg_risk = round(
        df["mental_health_risk_score"].mean(),
        2
    )

    st.error(
        f"Average Mental Health Risk Score: {avg_risk}"
    )

if "sleep_quality" in df.columns:

    most_common_quality = (
        df["sleep_quality"]
        .value_counts()
        .idxmax()
    )

    st.info(
        f"Most common sleep quality: {most_common_quality}"
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
    "Teen Mental Health Analytics Dashboard | Sleep Analysis"
)
