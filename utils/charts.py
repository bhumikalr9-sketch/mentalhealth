import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ------------------------------------
# AGE DISTRIBUTION
# ------------------------------------

def age_distribution(df):

    fig = px.histogram(
        df,
        x="age",
        nbins=10,
        title="Age Distribution"
    )

    return fig


# ------------------------------------
# GENDER DISTRIBUTION
# ------------------------------------

def gender_distribution(df):

    gender_df = (
        df["gender"]
        .value_counts()
        .reset_index()
    )

    gender_df.columns = [
        "Gender",
        "Count"
    ]

    fig = px.pie(
        gender_df,
        names="Gender",
        values="Count",
        title="Gender Distribution"
    )

    return fig


# ------------------------------------
# SOCIAL MEDIA HOURS
# ------------------------------------

def social_media_distribution(df):

    fig = px.histogram(
        df,
        x="daily_social_media_hours",
        nbins=20,
        title="Daily Social Media Usage"
    )

    return fig


# ------------------------------------
# PLATFORM ANALYSIS
# ------------------------------------

def platform_usage(df):

    if "primary_platform" not in df.columns:
        return None

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
        title="Platform Usage"
    )

    return fig


# ------------------------------------
# SLEEP DISTRIBUTION
# ------------------------------------

def sleep_distribution(df):

    fig = px.histogram(
        df,
        x="sleep_hours",
        nbins=20,
        title="Sleep Hours Distribution"
    )

    return fig


# ------------------------------------
# SLEEP QUALITY
# ------------------------------------

def sleep_quality_chart(df):

    if "sleep_quality" not in df.columns:
        return None

    quality_df = (
        df["sleep_quality"]
        .value_counts()
        .reset_index()
    )

    quality_df.columns = [
        "Quality",
        "Count"
    ]

    fig = px.pie(
        quality_df,
        names="Quality",
        values="Count",
        title="Sleep Quality"
    )

    return fig


# ------------------------------------
# SOCIAL MEDIA VS SLEEP
# ------------------------------------

def social_media_vs_sleep(df):

    fig = px.scatter(
        df,
        x="daily_social_media_hours",
        y="sleep_hours",
        color="gender",
        title="Social Media vs Sleep"
    )

    return fig


# ------------------------------------
# SOCIAL MEDIA VS ANXIETY
# ------------------------------------

def social_media_vs_anxiety(df):

    fig = px.scatter(
        df,
        x="daily_social_media_hours",
        y="anxiety_level",
        color="gender",
        title="Social Media vs Anxiety"
    )

    return fig


# ------------------------------------
# SOCIAL MEDIA VS STRESS
# ------------------------------------

def social_media_vs_stress(df):

    fig = px.scatter(
        df,
        x="daily_social_media_hours",
        y="stress_level",
        color="gender",
        title="Social Media vs Stress"
    )

    return fig


# ------------------------------------
# SLEEP VS STRESS
# ------------------------------------

def sleep_vs_stress(df):

    fig = px.scatter(
        df,
        x="sleep_hours",
        y="stress_level",
        color="gender",
        title="Sleep vs Stress"
    )

    return fig


# ------------------------------------
# SLEEP VS ANXIETY
# ------------------------------------

def sleep_vs_anxiety(df):

    fig = px.scatter(
        df,
        x="sleep_hours",
        y="anxiety_level",
        color="gender",
        title="Sleep vs Anxiety"
    )

    return fig


# ------------------------------------
# STRESS DISTRIBUTION
# ------------------------------------

def stress_distribution(df):

    fig = px.histogram(
        df,
        x="stress_level",
        nbins=15,
        title="Stress Distribution"
    )

    return fig


# ------------------------------------
# ANXIETY DISTRIBUTION
# ------------------------------------

def anxiety_distribution(df):

    fig = px.histogram(
        df,
        x="anxiety_level",
        nbins=15,
        title="Anxiety Distribution"
    )

    return fig


# ------------------------------------
# ADDICTION DISTRIBUTION
# ------------------------------------

def addiction_distribution(df):

    fig = px.histogram(
        df,
        x="addiction_level",
        nbins=15,
        title="Addiction Distribution"
    )

    return fig


# ------------------------------------
# RISK SCORE DISTRIBUTION
# ------------------------------------

def risk_score_distribution(df):

    if "mental_health_risk_score" not in df.columns:
        return None

    fig = px.histogram(
        df,
        x="mental_health_risk_score",
        nbins=20,
        title="Risk Score Distribution"
    )

    return fig


# ------------------------------------
# STRESS VS ANXIETY
# ------------------------------------

def stress_vs_anxiety(df):

    fig = px.scatter(
        df,
        x="stress_level",
        y="anxiety_level",
        color="gender",
        title="Stress vs Anxiety"
    )

    return fig


# ------------------------------------
# CORRELATION HEATMAP
# ------------------------------------

def correlation_heatmap(df):

    numeric_df = df.select_dtypes(
        include=["int64", "float64"]
    )

    corr = numeric_df.corr()

    fig = px.imshow(
        corr,
        text_auto=True,
        title="Correlation Heatmap"
    )

    return fig


# ------------------------------------
# DEPRESSION CHART
# ------------------------------------

def depression_chart(df):

    if "depression_label" not in df.columns:
        return None

    depression_df = (
        df["depression_label"]
        .value_counts()
        .reset_index()
    )

    depression_df.columns = [
        "Status",
        "Count"
    ]

    fig = px.pie(
        depression_df,
        names="Status",
        values="Count",
        title="Depression Distribution"
    )

    return fig


# ------------------------------------
# FEATURE IMPORTANCE
# ------------------------------------

def feature_importance_chart(
    features,
    importances
):

    imp_df = pd.DataFrame({
        "Feature": features,
        "Importance": importances
    })

    imp_df = imp_df.sort_values(
        by="Importance",
        ascending=False
    )

    fig = px.bar(
        imp_df,
        x="Importance",
        y="Feature",
        orientation="h",
        title="Feature Importance"
    )

    return fig


# ------------------------------------
# RADAR CHART
# ------------------------------------

def mental_health_radar(
    stress,
    anxiety,
    addiction,
    risk
):

    categories = [
        "Stress",
        "Anxiety",
        "Addiction",
        "Risk"
    ]

    values = [
        stress,
        anxiety,
        addiction,
        risk
    ]

    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=values,
            theta=categories,
            fill="toself",
            name="Metrics"
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

    return fig


# ------------------------------------
# AGE VS RISK
# ------------------------------------

def age_vs_risk(df):

    if "mental_health_risk_score" not in df.columns:
        return None

    age_df = (
        df.groupby("age")
        ["mental_health_risk_score"]
        .mean()
        .reset_index()
    )

    fig = px.line(
        age_df,
        x="age",
        y="mental_health_risk_score",
        markers=True,
        title="Age vs Risk Score"
    )

    return fig
