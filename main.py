import streamlit as st

def calculate(num1, num2, operation):
    """Perform the selected arithmetic operation."""
    operations = {
        "Addition (+)": (num1 + num2, "+"),
        "Subtraction (-)": (num1 - num2, "-"),
        "Multiplication (×)": (num1 * num2, "×"),
        "Division (÷)": (None if num2 == 0 else num1 / num2, "÷")
    }
    return operations[operation]

def main():
    # Page Configuration
    st.set_page_config(page_title="Simple Calculator", layout="centered")
    st.title("🔢 Simple Calculator")
    st.write("Enter two numbers and choose an operation to perform calculations.")
    
    # Input Fields
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number", value=0.0, format="%.4f")
    with col2:
        num2 = st.number_input("Enter second number", value=0.0, format="%.4f")
    
    # Operation Selection
    operation = st.selectbox("Choose operation", ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"])
    
    # Calculate Result
    if st.button("Calculate", use_container_width=True):
        result, symbol = calculate(num1, num2, operation)
        if result is None:
            st.error("❌ Error: Division by zero is not allowed!")
        else:
            st.success(f"✅ Result: {num1} {symbol} {num2} = {result:.4f}")
    
    # Footer Section
    st.markdown("""
    ---
    **Developed by [Azra Talib](https://github.com/AzraTalib123)**
    """)

if __name__ == "__main__":
    main()
