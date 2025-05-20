import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
@st.cache
def load_data():
    benin = pd.read_csv("../data/benin_clean.csv")
    sierra_leone = pd.read_csv("../data/sierraleone_clean.csv")
    togo = pd.read_csv("../data/togo_clean.csv")
    benin["Country"] = "Benin"
    sierra_leone["Country"] = "Sierra Leone"
    togo["Country"] = "Togo"
    return pd.concat([benin, sierra_leone, togo], ignore_index=True)

df = load_data()

# Sidebar
st.sidebar.title("Solar Potential Dashboard")
selected_country = st.sidebar.multiselect(
    "Select Country", options=df["Country"].unique(), default=df["Country"].unique()
)
selected_metric = st.sidebar.selectbox(
    "Select Metric", options=["GHI", "DNI", "DHI"]
)

# Filter data
filtered_data = df[df["Country"].isin(selected_country)]

# Main Dashboard
st.title("Solar Potential Dashboard")
st.markdown("### Visualizing Solar Potential Across Countries")

# Boxplot
st.markdown(f"#### {selected_metric} Comparison Across Countries")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=filtered_data, x="Country", y=selected_metric, palette="Set2", ax=ax)
ax.set_title(f"{selected_metric} Comparison Across Countries")
st.pyplot(fig)

# Top Regions Table
st.markdown("#### Top Regions by Average GHI")
top_regions = (
    df.groupby("Country")[["GHI"]]
    .mean()
    .sort_values(by="GHI", ascending=False)
    .reset_index()
)
st.table(top_regions)