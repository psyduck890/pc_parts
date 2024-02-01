import streamlit as st
import pandas as pd

df = pd.read_csv('./all.csv')
st.title('AMD processors')
st.dataframe(df.set_index(df.columns[0]), column_config={"Product_url": st.column_config.LinkColumn()})