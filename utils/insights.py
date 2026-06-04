import pandas as pd

# ---------------------------------------
# EXECUTIVE DASHBOARD INSIGHTS
# ---------------------------------------

def executive_insights(df):

    insights = {

        "total_students": len(df),

        "avg_sleep": round(
            df["sleep_hours"].mean(),
            2
        ),

        "avg_social_media": round(
            df["daily_social_media_hours"].mean(),
            2
        ),

        "avg_stress": round(
            df["stress_level"].mean(),
            2
        ),

        "avg_anxiety": round(
            df["anxiety_level"].mean(),
            2
        ),

        "avg_addiction": round(
            df["addiction_level"].mean(),
            2
        )
    }

    if "mental_health_risk_score" in df.columns:

        insights["avg_risk"] = round(
            df["mental_health_risk_score"].mean(),
            2
        )

    else:
        insights["avg_risk"] = 0

    return insights


# ---------------------------------------
# SOCIAL MEDIA INSIGHTS
# ---------------------------------------

def social_media_insights(df):

    result = {}

    result["avg_usage"] = round(
        df["daily_social_media_hours"].mean(),
        2
    )

    result["max_usage"] = round(
        df["daily_social_media_hours"].max(),
        2
    )

    result["heavy_users"] = len(
        df[
            df["daily_social_media_hours"] >= 6
        ]
    )

    if "primary_platform" in df.columns:

        result["most_popular_platform"] = (
            df["primary_platform"]
            .value_counts()
            .idxmax()
        )

    return result


# ---------------------------------------
# SLEEP INSIGHTS
# ---------------------------------------

def sleep_insights(df):

    result = {}

    result["avg_sleep"] = round(
        df["sleep_hours"].mean(),
        2
    )

    result["min_sleep"] = round(
        df["sleep_hours"].min(),
        2
    )

    result["max_sleep"] = round(
        df["sleep_hours"].max(),
        2
    )

    result["poor_sleep_count"] = len(
        df[
            df["sleep_hours"] < 6
        ]
    )

    result["good_sleep_count"] = len(
        df[
            df["sleep_hours"] >= 8
        ]
    )

    if "sleep_quality" in df.columns:

        result["most_common_quality"] = (
            df["sleep_quality"]
            .value_counts()
            .idxmax()
        )

    return result


# ---------------------------------------
# MENTAL HEALTH INSIGHTS
# ---------------------------------------

def mental_health_insights(df):

    result = {}

    result["avg_stress"] = round(
        df["stress_level"].mean(),
        2
    )

    result["avg_anxiety"] = round(
        df["anxiety_level"].mean(),
        2
    )

    result["avg_addiction"] = round(
        df["addiction_level"].mean(),
        2
    )

    if "mental_health_risk_score" in df.columns:

        result["avg_risk"] = round(
            df["mental_health_risk_score"].mean(),
            2
        )

        result["high_risk_students"] = len(
            df[
                df["mental_health_risk_score"] >= 75
            ]
        )

    return result


# ---------------------------------------
# DEPRESSION INSIGHTS
# ---------------------------------------

def depression_insights(df):

    result = {}

    if "depression_label" not in df.columns:

        result["depression_rate"] = 0
        return result

    total = len(df)

    depressed = len(
        df[
            df["depression_label"] == 1
        ]
    )

    result["depression_rate"] = round(
        (depressed / total) * 100,
        2
    )

    result["depressed_students"] = depressed

    result["healthy_students"] = (
        total - depressed
    )

    return result


# ---------------------------------------
# RISK SEGMENTATION
# ---------------------------------------

def risk_segmentation(df):

    if "mental_health_risk_score" not in df.columns:

        return {}

    low = len(
        df[
            df["mental_health_risk_score"] < 25
        ]
    )

    moderate = len(
        df[
            (df["mental_health_risk_score"] >= 25)
            &
            (df["mental_health_risk_score"] < 50)
        ]
    )

    high = len(
        df[
            (df["mental_health_risk_score"] >= 50)
            &
            (df["mental_health_risk_score"] < 75)
        ]
    )

    critical = len(
        df[
            df["mental_health_risk_score"] >= 75
        ]
    )

    return {

        "low": low,

        "moderate": moderate,

        "high": high,

        "critical": critical
    }


# ---------------------------------------
# CORRELATION INSIGHTS
# ---------------------------------------

def correlation_insights(df):

    numeric_df = df.select_dtypes(
        include=["int64", "float64"]
    )

    corr = numeric_df.corr()

    return corr


# ---------------------------------------
# AGE GROUP INSIGHTS
# ---------------------------------------

def age_group_insights(df):

    age_summary = (
        df.groupby("age")
        [
            "sleep_hours",
            "stress_level",
            "anxiety_level"
        ]
        .mean()
        .reset_index()
    )

    return age_summary


# ---------------------------------------
# GENDER INSIGHTS
# ---------------------------------------

def gender_insights(df):

    gender_summary = (
        df.groupby("gender")
        [
            "sleep_hours",
            "stress_level",
            "anxiety_level",
            "daily_social_media_hours"
        ]
        .mean()
        .reset_index()
    )

    return gender_summary


# ---------------------------------------
# GENERATE SUMMARY TEXT
# ---------------------------------------

def generate_summary(df):

    insights = executive_insights(df)

    summary = f"""
Total Students: {insights['total_students']}

Average Sleep Hours:
{insights['avg_sleep']}

Average Social Media Usage:
{insights['avg_social_media']} hours/day

Average Stress Level:
{insights['avg_stress']}

Average Anxiety Level:
{insights['avg_anxiety']}

Average Addiction Level:
{insights['avg_addiction']}

Average Risk Score:
{insights['avg_risk']}
"""

    return summary
