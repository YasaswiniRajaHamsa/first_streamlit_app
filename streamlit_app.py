import streamlit
streamlit.title('My parents new healthy diner')
streamlit.header(' 🥣 Breafast menu')
streamlit.text('🥑🍞Blueberry oatmeal')
streamlit.text('idly')
streamlit.text('dosa')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)
