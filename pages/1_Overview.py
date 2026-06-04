# pages/1_Overview.py

import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_data

# ------------------------------------
# PAGE CONFIG
# ------------------------------------

st.set_page_config(
    page_title="Overview",
    page_icon="📊",
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
# TITLE
# ------------------------------------

st.title("📊 Dashboard Overview")

st.markdown(
    "Comprehensive overview of teen mental health indicators."
)

st.markdown("---")

# ------------------------------------
# KPIs
# ------------------------------------

total_students = len(df)

avg_sleep = round(
    df["sleep_hours"].mean(),
    2
)

avg_social = round(
    df["daily_social_media_hours"].mean(),
    2
)

avg_anxiety = round(
    df["anxiety_level"].mean(),
    2
)

avg_stress = round(
    df["stress_level"].mean(),
    2
)

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Students",
    total_students
)

col2.metric(
    "Avg Sleep",
    avg_sleep
)

col3.metric(
    "Social Media Hrs",
    avg_social
)

col4.metric(
    "Avg Anxiety",
    avg_anxiety
)

col5.metric(
    "Avg Stress",
    avg_stress
)

st.markdown("---")

# ------------------------------------
# AGE DISTRIBUTION
# ------------------------------------

col1, col2 = st.columns(2)

with col1:

    fig = px.histogram(
        df,
        x="age",
        title="Age Distribution",
        nbins=10
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    gender_counts = (
        df["gender"]
        .value_counts()
        .reset_index()
    )

    gender_counts.columns = [
        "Gender",
        "Count"
    ]

    fig = px.pie(
        gender_counts,
        names="Gender",
        values="Count",
        title="Gender Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ------------------------------------
# SOCIAL MEDIA ANALYSIS
# ------------------------------------

st.subheader("📱 Social Media Usage")

col1, col2 = st.columns(2)

with col1:

    fig = px.histogram(
        df,
        x="daily_social_media_hours",
        title="Daily Social Media Hours"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    if "primary_platform" in df.columns:

        platform_counts = (
            df["primary_platform"]
            .value_counts()
            .reset_index()
        )

        platform_counts.columns = [
            "Platform",
            "Users"
        ]

        fig = px.bar(
            platform_counts,
            x="Platform",
            y="Users",
            title="Most Used Platforms"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

st.markdown("---")

# ------------------------------------
# SLEEP ANALYSIS
# ------------------------------------

st.subheader("😴 Sleep Analysis")

col1, col2 = st.columns(2)

with col1:

    fig = px.histogram(
        df,
        x="sleep_hours",
        title="Sleep Hours Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    if "sleep_quality" in df.columns:

        quality = (
            df["sleep_quality"]
            .value_counts()
            .reset_index()
        )

        quality.columns = [
            "Quality",
            "Count"
        ]

        fig = px.pie(
            quality,
            names="Quality",
            values="Count",
            title="Sleep Quality"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

st.markdown("---")

# ------------------------------------
# STRESS & ANXIETY
# ------------------------------------

st.subheader("🧠 Mental Health Indicators")

col1, col2 = st.columns(2)

with col1:

    fig = px.box(
        df,
        y="stress_level",
        title="Stress Level Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    fig = px.box(
        df,
        y="anxiety_level",
        title="Anxiety Level Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.markdown("---")

# ------------------------------------
# RISK SCORE ANALYSIS
# ------------------------------------

if "mental_health_risk_score" in df.columns:

    st.subheader("⚠ Mental Health Risk")

    fig = px.histogram(
        df,
        x="mental_health_risk_score",
        color="gender",
        title="Risk Score Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.markdown("---")

# ------------------------------------
# CORRELATION MATRIX
# ------------------------------------

st.subheader("📈 Correlation Analysis")

numeric_cols = df.select_dtypes(
    include=["int64", "float64"]
)

corr = numeric_cols.corr()

fig = px.imshow(
    corr,
    text_auto=True,
    title="Correlation Heatmap"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# ------------------------------------
# EXECUTIVE INSIGHTS
# ------------------------------------

st.subheader("💡 Key Insights")

st.success(
    f"""
    Average social media usage is
    {avg_social} hours/day.
    """
)

st.success(
    f"""
    Students sleep an average of
    {avg_sleep} hours/day.
    """
)

st.success(
    f"""
    Average anxiety score is
    {avg_anxiety}.
    """
)

st.success(
    f"""
    Average stress score is
    {avg_stress}.
    """
)

# ------------------------------------
# DATA PREVIEW
# ------------------------------------

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
    "Teen Mental Health Analytics Dashboard"
)
