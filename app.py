import streamlit as st

st.set_page_config(
    page_title="Todo Liste",
    page_icon="👋",
)

st.sidebar.success("Select a demo above.")

st.markdown(
    """
  # TODO Liste
  
  ## Aktuelle Items:
"""
)

st.write("Hello Data Craft")