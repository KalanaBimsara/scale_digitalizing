import streamlit as st
import json
from datetime import datetime

# Simulated incoming production order from SAP
order = {
    "order_id": "ord0001",
    "product_id": "pro0001",
    "date": str(datetime.now().date()),
    "minor_ingredients": [
        {"ingredient_id": "ing0001", "name": "MSG", "expected_quantity": "10g"},
        {"ingredient_id": "ing0002", "name": "Preservative-X", "expected_quantity": "5g"},
        {"ingredient_id": "ing0003", "name": "Enzyme-Z", "expected_quantity": "0.5g"}
    ]
}

st.set_page_config(page_title="Ingredient Scaler", layout="centered")
st.title("🧪 Minor Ingredient Scaling System")
st.markdown(f"**Production Order ID:** `{order['order_id']}`  \n**Product ID:** `{order['product_id']}`  \n**Date:** `{order['date']}`")

results = []

with st.form("scaling_form"):
    st.subheader("📥 Enter Measured Weights")

    for ing in order["minor_ingredients"]:
        st.markdown(f"**{ing['name']}** (Expected: `{ing['expected_quantity']}`)")
        ing["measured"] = st.number_input(
            label=f"Measured quantity for {ing['name']} (in grams):",
            min_value=0.0,
            step=0.01,
            key=ing["ingredient_id"]
        )
        st.markdown("---")

    submitted = st.form_submit_button("✅ Finalize and Export")

    if submitted:
        for ing in order["minor_ingredients"]:
            results.append({
                "ingredient_id": ing["ingredient_id"],
                "name": ing["name"],
                "expected_quantity": ing["expected_quantity"],
                "measured_quantity": f"{ing['measured']}g",
                "timestamp": datetime.now().isoformat()
            })

        final_output = {
            "order_id": order["order_id"],
            "product_id": order["product_id"],
            "date": order["date"],
            "minor_ingredients": results
        }

        filename = f"scaled_output_{order['product_id']}_{order['date']}.json"
        with open(filename, "w") as f:
            json.dump(final_output, f, indent=4)

        st.success(f"✅ All data recorded and saved as `{filename}`")
        st.download_button("⬇️ Download JSON", data=json.dumps(final_output, indent=4), file_name=filename, mime="application/json")
