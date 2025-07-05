import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Page config
st.set_page_config(page_title="Streamlit Showcase App", layout="wide")

# Title and Intro
st.title("✨ Streamlit Deployment Showcase")
st.subheader("Test your Streamlit deployment with a stylish sample app.")
st.markdown("Made with ❤️ using `Streamlit`, `Matplotlib`, and `Pandas`")

st.divider()

# Sidebar Navigation
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Go to", ["📋 Overview", "📊 Data & Charts", "📝 Feedback Form"])

# Section 1 - Overview
if page == "📋 Overview":
    st.header("📋 Overview")
    st.write("""
    This app demonstrates:
    - Interactive widgets
    - Random data generation
    - Matplotlib charts
    - User feedback form
    - Responsive layout
    """)

    st.success("You're viewing the overview section!")

# Section 2 - Data & Chart
elif page == "📊 Data & Charts":
    st.header("📊 Data Visualization")
    st.markdown("Here's some randomly generated data to show off visualizations:")

    # Create random data
    data = pd.DataFrame({
        'Date': pd.date_range(start='2025-01-01', periods=30),
        'Sales': np.random.randint(100, 500, size=30)
    })

    st.dataframe(data)

    # Chart
    fig, ax = plt.subplots()
    ax.plot(data['Date'], data['Sales'], marker='o', color='skyblue', linewidth=2)
    ax.set_title("📈 Sales Over Time", fontsize=16)
    ax.set_xlabel("Date")
    ax.set_ylabel("Sales")
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Section 3 - Feedback
elif page == "📝 Feedback Form":
    st.header("📝 Feedback Form")
    name = st.text_input("Your Name")
    feedback = st.text_area("What do you think about this demo app?")
    mood = st.radio("How do you feel about Streamlit?", ["😍 Love it", "🙂 It's good", "😐 Neutral", "😕 Not sure"])

    if st.button("Submit Feedback"):
        if name and feedback:
            st.success(f"Thanks for your feedback, {name}!")
        else:
            st.warning("Please fill in both name and feedback.")

    st.markdown("You selected: **{}**".format(mood))

# Footer
st.divider()
st.caption("© 2025 | Built for testing Streamlit deployment.")
