import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📈 Profit Analyzer App")

st.write("Enter profits for 5 years:")

years = []
profits = []

# Input section
for i in range(5):
    year = st.text_input(f"Year {i+1}", key=f"year_{i}")
    profit = st.number_input(f"Profit in ₹ lakh for {year}", key=f"profit_{i}")
    if year:
        years.append(year)
        profits.append(profit)

# Processing and output
if len(profits) == 5 and all(years):
    avg_profit = sum(profits) / 5
    st.write(f"### 📊 Average Profit: ₹{avg_profit:.2f} lakh")

    # Display performance
    st.write("### Year-wise Performance:")
    for i in range(5):
        if profits[i] > avg_profit:
            st.success(f"{years[i]}: ₹{profits[i]} lakh (Above Average)")
        else:
            st.error(f"{years[i]}: ₹{profits[i]} lakh (Below Average)")

    # Create DataFrame
    df = pd.DataFrame({
        "Year": years,
        "Profit": profits
    })

    # ➕ Color column for bar chart
    df["Color"] = ["green" if p > avg_profit else "red" for p in df["Profit"]]

    # 📈 Line chart
    st.write("### 📉 Profit Over Time (Line Chart)")
    st.line_chart(df.set_index("Year")["Profit"])

    # 📊 Bar chart with colors
    st.write("### 📊 Profit Comparison (Bar Chart with Colors)")
    fig, ax = plt.subplots()
    ax.bar(df["Year"], df["Profit"], color=df["Color"])
    ax.set_ylabel("Profit (₹ lakh)")
    ax.set_title("Profit by Year")
    st.pyplot(fig)
