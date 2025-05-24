import streamlit as st
from core import get_product_price
def main():
    st.set_page_config(page_title="Product Price Checker", layout="centered")

    st.title("🛒 Product Price Checker (US, USD)")
    product_input = st.text_input("Enter product name:", placeholder="e.g., iPhone 15")

    if st.button("Get Price"):
        if not product_input.strip():
            st.warning("Please enter a product name.")
        else:
            with st.spinner("Getting product price..."):
                result = get_product_price(product_input)
                if result["success"]:
                    st.success("Price fetched successfully!")
                    st.json(result["data"])
                else:
                    st.error("Failed to validate response.")
                    st.subheader("Raw Output")
                    st.code(result["raw_response"], language="json")
                    st.subheader("Error Details")
                    st.text(result["details"])

if __name__ == "__main__":
    main()
