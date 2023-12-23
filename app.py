import streamlit as st
import pandas as pd
import pygwalker as pyg
import streamlit.components.v1 as components

# set page configurations
st.set_page_config(
    page_title="PygWalker - An intro",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load data
@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    return df

df = load_data("workspace/sleep_health_data.csv")

# Set title and subtitle
st.title("PygWalker - An intro")
st.subheader("A simple app to introduce PygWalker")

# Display PygWalker
def load_config(file_path):
    with open(file_path, "r") as f:
        config_str = f.read()
    return config_str

config = load_config('config.json')

# my df
st.write(config)


# The following took quite a bit of iteration
pyg_html = pyg.walk(df, spec=config, dark='dark', return_html=True)

components.html(pyg_html, height=1000, scrolling=True)
