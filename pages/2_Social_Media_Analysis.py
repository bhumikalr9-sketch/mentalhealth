# pages/2_Social_Media_Analysis.py

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from utils.data_loader import load_data

# ---------------------------------------
# PAGE CONFIG
# ---------------------------------------

st.set_page_config(
    page_title="Social Media Analysis",
    page_icon="📱",
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

st.title("📱 Social Media Analysis")

st.markdown("""
Analyze social media habits, usage patterns,
platform popularity, and their relationship
with mental health indicators.
""")

st.markdown("---")

# ---------------------------------------
# KPI SECTION
# ---------------------------------------

avg_hours = round(
    df["daily_social_media_hours"].mean(),
    2
)

max_hours = round(
    df["daily_social_media_hours"].max(),
    2
)

min_hours = round(
    df["daily_social_media_hours"].min(),
    2
)

total_students = len(df)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Students",
    total_students
)

col2.metric(
    "Avg Usage",
    f"{avg_hours} hrs"
)

col3.metric(
    "Max Usage",
    f"{max_hours} hrs"
)

col4.metric(
    "Min Usage",
    f"{min_hours} hrs"
)

st.markdown("---")

# ---------------------------------------
# SOCIAL MEDIA HOURS DISTRIBUTION
# ---------------------------------------

st.subheader("📊 Daily Social Media Usage")

fig = px.histogram(
    df,
    x="daily_social_media_hours",
    nbins=20,
    title="Daily Social Media Hours Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------
# PLATFORM ANALYSIS
# ---------------------------------------

if "primary_platform" in df.columns:

    st.subheader("🌐 Platform Popularity")

    platform_df = (
        df["primary_platform"]
        .value_counts()
        .reset_index()
    )

    platform_df.columns = [
        "Platform",
        "Users"
    ]

    fig = px.bar(
        platform_df,
        x="Platform",
        y="Users",
        title="Most Popular Platforms"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ---------------------------------------
# SOCIAL MEDIA VS ANXIETY
# ---------------------------------------

st.subheader("😟 Social Media vs Anxiety")

fig = px.scatter(
    df,
    x="daily_social_media_hours",
    y="anxiety_level",
    color="gender",
    title="Social Media Usage vs Anxiety"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------
# SOCIAL MEDIA VS STRESS
# ---------------------------------------

st.subheader("😫 Social Media vs Stress")

fig = px.scatter(
    df,
    x="daily_social_media_hours",
    y="stress_level",
    color="gender",
    title="Social Media Usage vs Stress"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------
# SOCIAL MEDIA VS SLEEP
# ---------------------------------------

st.subheader("😴 Social Media vs Sleep")

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
# ADDICTION ANALYSIS
# ---------------------------------------

if "addiction_level" in df.columns:

    st.subheader("⚠ Addiction Analysis")

    fig = px.box(
        df,
        y="addiction_level",
        title="Addiction Level Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ---------------------------------------
# PLATFORM VS ANXIETY
# ---------------------------------------

if (
    "primary_platform" in df.columns and
    "anxiety_level" in df.columns
):

    st.subheader("📈 Platform vs Anxiety")

    anxiety_df = (
        df.groupby("primary_platform")
        ["anxiety_level"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        anxiety_df,
        x="primary_platform",
        y="anxiety_level",
        title="Average Anxiety by Platform"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ---------------------------------------
# PLATFORM VS STRESS
# ---------------------------------------

if (
    "primary_platform" in df.columns and
    "stress_level" in df.columns
):

    st.subheader("📈 Platform vs Stress")

    stress_df = (
        df.groupby("primary_platform")
        ["stress_level"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        stress_df,
        x="primary_platform",
        y="stress_level",
        title="Average Stress by Platform"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ---------------------------------------
# PLATFORM VS ADDICTION
# ---------------------------------------

if (
    "primary_platform" in df.columns and
    "addiction_level" in df.columns
):

    st.subheader("📈 Platform vs Addiction")

    addiction_df = (
        df.groupby("primary_platform")
        ["addiction_level"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        addiction_df,
        x="primary_platform",
        y="addiction_level",
        title="Average Addiction by Platform"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ---------------------------------------
# DEPRESSION ANALYSIS
# ---------------------------------------

if "depression_label" in df.columns:

    st.subheader("🧠 Social Media vs Depression")

    depression_df = (
        df.groupby("depression_label")
        ["daily_social_media_hours"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        depression_df,
        x="depression_label",
        y="daily_social_media_hours",
        title="Average Usage by Depression Status"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ---------------------------------------
# CORRELATION ANALYSIS
# ---------------------------------------

st.subheader("📌 Correlation with Social Media Usage")

corr_columns = [
    "daily_social_media_hours",
    "sleep_hours",
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

corr_df = df[corr_columns].corr()

fig = px.imshow(
    corr_df,
    text_auto=True,
    title="Correlation Heatmap"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------
# TOP INSIGHTS
# ---------------------------------------

st.markdown("---")

st.subheader("💡 Key Insights")

highest_platform = "N/A"

if "primary_platform" in df.columns:
    highest_platform = (
        df["primary_platform"]
        .value_counts()
        .idxmax()
    )

st.success(
    f"Most used platform: {highest_platform}"
)

st.success(
    f"Average daily usage: {avg_hours} hours"
)

if "sleep_hours" in df.columns:

    low_sleep = len(
        df[
            df["sleep_hours"] < 6
        ]
    )

    st.warning(
        f"{low_sleep} students sleep less than 6 hours."
    )

if (
    "mental_health_risk_score"
    in df.columns
):

    avg_risk = round(
        df["mental_health_risk_score"]
        .mean(),
        2
    )

    st.error(
        f"Average Risk Score: {avg_risk}"
    )

# ---------------------------------------
# DATA TABLE
# ---------------------------------------

st.markdown("---")

st.subheader("📄 Data Preview")

st.dataframe(
    df.head(20),
    use_container_width=True
)

# ---------------------------------------
# FOOTER
# ---------------------------------------

st.markdown("---")

st.caption(
    "Teen Mental Health Analytics Dashboard"
)
