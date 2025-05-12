import streamlit as st


st.set_page_config(page_title="A Page  Demo", page_icon="📈")

st.sidebar.success("Sidebar")
st.sidebar.header("Plotting Demo")
st.markdown(
    """
  # TODO Liste
  
  ## Aktuelle Items:
"""
)
st.write("Hello Data Craft")