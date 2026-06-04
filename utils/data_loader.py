import pandas as pd
import streamlit as st
from pathlib import Path

# -------------------------------------
# LOAD DATA
# -------------------------------------

@st.cache_data
def load_data(file_name="Teen_Mental_Health.csv"):
    """
    Load CSV dataset and cache it.
    """

    try:

        # Project root directory
        root_dir = Path(__file__).resolve().parent.parent

        # Dataset path
        file_path = root_dir / file_name

        # Check file exists
        if not file_path.exists():

            st.error(
                f"Dataset not found: {file_path}"
            )

            return pd.DataFrame()

        # Load CSV
        df = pd.read_csv(file_path)

        return df

    except Exception as e:

        st.error(
            f"Error loading dataset: {e}"
        )

        return pd.DataFrame()


# -------------------------------------
# DATA SUMMARY
# -------------------------------------

@st.cache_data
def get_dataset_summary(df):

    summary = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing_values": int(
            df.isnull().sum().sum()
        ),
        "duplicate_rows": int(
            df.duplicated().sum()
        )
    }

    return summary


# -------------------------------------
# NUMERIC COLUMNS
# -------------------------------------

@st.cache_data
def get_numeric_columns(df):

    return df.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()


# -------------------------------------
# CATEGORICAL COLUMNS
# -------------------------------------

@st.cache_data
def get_categorical_columns(df):

    return df.select_dtypes(
        include=["object"]
    ).columns.tolist()


# -------------------------------------
# CLEAN DATA
# -------------------------------------

@st.cache_data
def clean_data(df):

    df = df.copy()

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Fill numeric null values
    numeric_cols = df.select_dtypes(
        include=["int64", "float64"]
    ).columns

    for col in numeric_cols:

        df[col] = df[col].fillna(
            df[col].median()
        )

    # Fill categorical null values
    categorical_cols = df.select_dtypes(
        include=["object"]
    ).columns

    for col in categorical_cols:

        df[col] = df[col].fillna(
            df[col].mode()[0]
        )

    return df


# -------------------------------------
# FILTER DATA
# -------------------------------------

def filter_data(
    df,
    gender=None,
    age=None
):
    """
    Filter dataset based on user selections.
    """

    filtered_df = df.copy()

    if gender and gender != "All":

        filtered_df = filtered_df[
            filtered_df["gender"] == gender
        ]

    if age and age != "All":

        filtered_df = filtered_df[
            filtered_df["age"] == age
        ]

    return filtered_df


# -------------------------------------
# FEATURE LIST
# -------------------------------------

def get_feature_columns():
    """
    Features used in ML models.
    """

    return [
        "age",
        "sleep_hours",
        "daily_social_media_hours",
        "stress_level",
        "anxiety_level",
        "addiction_level"
    ]


# -------------------------------------
# TARGET COLUMNS
# -------------------------------------

def get_target_columns():

    return {
        "classification":
            "depression_label",

        "regression":
            "mental_health_risk_score"
    }
