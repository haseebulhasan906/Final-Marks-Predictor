# app.py - UPDATED (White Theme + Local Directory Support)
import streamlit as st
import pandas as pd
import glob
import os

st.set_page_config(page_title="Abdullah & Haseeb", layout="wide")

# ============================
# WHITE THEME (Modern Look)
# ============================
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background-color: white !important;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #1e3a8a !important;
    }
    .stInfo, .stSuccess {
        opacity: 0.95;
    }
</style>
""", unsafe_allow_html=True)

# ============================
# TITLE
# ============================
st.markdown("<h1 style='text-align:center;'>Student Performance Prediction</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>CS4048 • Abdullah & Haseeb</h3>", unsafe_allow_html=True)
st.markdown("---")

# ============================
# SIDEBAR
# ============================
st.sidebar.image("https://img.icons8.com/fluency/100/robot.png")
st.sidebar.markdown("### Navigate")
section = st.sidebar.slider("Select Section", 1, 6, 1)

# ============================
# LOAD ALL FILES (LOCAL FOLDER)
# ============================

cleaned_data_file = "Cleaned_Dataset.csv"
final_results_file = "Final_Model_Performance_Summary.csv"

df = pd.read_csv(cleaned_data_file)
table = pd.read_csv(final_results_file)

# Get all png images in the same folder
plots = sorted(glob.glob("*.png"))

# Find workflow image
workflow_candidates = [
    "workflowpipeline image.png",
    "workflowpipeline image.jpg",
    "workflowpipeline image.jpeg",
    "WorkflowPipeline Image.png",
    "workflow_pipeline.png"
]

workflow_path = next((f for f in workflow_candidates if os.path.exists(f)), None)

# ============================
# SECTIONS
# ============================

if section == 1:
    st.header("1. Cleaned Dataset")
    st.success(f"Students: {len(df)} | Features: {df.shape[1]}")
    st.dataframe(df, use_container_width=True)

elif section == 2:
    st.header("2. Final Model Results")
    st.info("Lower Test MAE = Better Model")
    st.dataframe(table, use_container_width=True)

elif section == 3:
    st.header("3. All Result Plots")
    if not plots:
        st.warning("No .png plots found in this directory!")
    else:
        cols = st.columns(3)
        for i, p in enumerate(plots):
            with cols[i % 3]:
                name = os.path.basename(p).replace(".png", "").replace("_", " ").title()
                st.image(p, caption=name, use_container_width=True)

elif section == 4:
    st.header("4. Project Workflow Pipeline")

    if workflow_path:
        st.image(workflow_path, use_container_width=True)
        st.success("Workflow pipeline loaded successfully!")
    else:
        st.error("Workflow image not found! Place one of these in the same folder:")
        st.code("\n".join(workflow_candidates))

    st.markdown("""
    ### **Complete ML Pipeline**
    • Load & Merge Dataset  
    • Clean & Normalize Scores  
    • Visualizations + Correlation  
    • Train Simple + Multiple Regression  
    • Bootstrapping 95% CI  
    • Final Comparison Table  
    """)

elif section == 5:
    st.header("5. Key Findings")
    st.success("Multiple Regression using past exam scores gives BEST prediction accuracy.")
    st.info("Past performance is the strongest predictor of future results.")

elif section == 6:
    st.header("6. Project Complete!")
    st.balloons()
    st.markdown("<h1 style='text-align:center; color:#10b981;'>100% Done!</h1>", unsafe_allow_html=True)
