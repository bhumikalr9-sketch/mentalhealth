import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_data
from utils.ml_model import (
    train_depression_model,
    predict_depression
)

# ----------------------------------
#
