import streamlit as st
import pandas as pd
from utils.data_loader import load_data
from utils.insights import executive_insights

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Teen Mental Health Analytics",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------
# LOAD CSS
# -----------------------------------

def load_css():
    try:
        with open("assets/styles.css") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )
    except:
        pass

load_css()

# -----------------------------------
# LOAD DATA
# -----------------------------------

@st.cache_data
def load_dataset():
    return load_data("Teen_Mental_Health.csv")

df = load_dataset()

# -----------------------------------
# SIDEBAR
# -----------------------------------

st.sidebar.title("🧠 Teen Mental Health")

st.sidebar.markdown("---")

st.sidebar.success(
    f"Records Loaded: {len(df)}"
)

st.sidebar.info(
    f"Features: {df.shape[1]}"
)

st.sidebar.markdown("---")

# -----------------------------------
# TITLE
# -----------------------------------

st.title("🧠 Teen Mental Health Analytics Dashboard")

st.markdown("""
Analyze social media habits, sleep quality,
stress levels, anxiety indicators and
mental health risk factors among teenagers.
""")

st.markdown("---")

# -----------------------------------
# FILTERS
# -----------------------------------

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Select Gender",
        ["All"] + sorted(df["gender"].unique().tolist())
    )

with col2:

    age = st.selectbox(
        "Select Age",
        ["All"] + sorted(df["age"].unique().tolist())
    )

filtered_df = df.copy()

if gender != "All":
    filtered_df = filtered_df[
        filtered_df["gender"] == gender
    ]

if age != "All":
    filtered_df = filtered_df[
        filtered_df["age"] == age
    ]

# -----------------------------------
# KPI SECTION
# -----------------------------------

stats = executive_insights(filtered_df)

st.subheader("📊 Key Metrics")

k1, k2, k3, k4, k5 = st.columns(5)

with k1:
    st.metric(
        "Students",
        stats["total_students"]
    )

with k2:
    st.metric(
        "Avg Sleep",
        f"{stats['avg_sleep']:.2f} hrs"
    )

with k3:
    st.metric(
        "Avg Risk",
        f"{stats['avg_risk']:.2f}"
    )

with k4:
    st.metric(
        "Avg Anxiety",
        f"{stats['avg_anxiety']:.2f}"
    )

with k5:
    st.metric(
        "Avg Stress",
        f"{stats['avg_stress']:.2f}"
    )

st.markdown("---")

# -----------------------------------
# DATA OVERVIEW
# -----------------------------------

st.subheader("📋 Dataset Overview")

st.dataframe(
    filtered_df.head(20),
    use_container_width=True
)

# -----------------------------------
# QUICK INSIGHTS
# -----------------------------------

st.subheader("💡 Executive Insights")

c1, c2 = st.columns(2)

with c1:

    st.info(
        f"""
        Average Social Media Usage:
        {filtered_df['daily_social_media_hours'].mean():.2f} hrs/day
        """
    )

    st.info(
        f"""
        Average Sleep Hours:
        {filtered_df['sleep_hours'].mean():.2f}
        """
    )

with c2:

    st.success(
        f"""
        Average Anxiety Level:
        {filtered_df['anxiety_level'].mean():.2f}
        """
    )

    st.success(
        f"""
        Average Addiction Level:
        {filtered_df['addiction_level'].mean():.2f}
        """
    )

st.markdown("---")

# -----------------------------------
# DEPRESSION STATS
# -----------------------------------

if "depression_label" in filtered_df.columns:

    depressed_pct = (
        filtered_df["depression_label"]
        .mean()
        * 100
    )

    st.subheader("⚠ Depression Risk")

    st.metric(
        "Depression Percentage",
        f"{depressed_pct:.1f}%"
    )

# -----------------------------------
# DOWNLOAD DATA
# -----------------------------------

st.subheader("📥 Download Dataset")

csv = filtered_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="filtered_teen_data.csv",
    mime="text/csv"
)

# -----------------------------------
# FOOTER
# -----------------------------------

st.markdown("---")

st.markdown(
    """
    <center>
    <h4>Teen Mental Health Analytics Dashboard</h4>
    <p>Built using Streamlit, Plotly and Machine Learning</p>
    </center>
    """,
    unsafe_allow_html=True
)
