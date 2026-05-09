import streamlit as st
import pandas as pd
from db import get_sentiment, get_tag_and_cat, get_infkey
import plotly.express as px
from nlp import get_tfidf_keywords

data = get_sentiment()
ct_data = get_tag_and_cat()
k_data = get_infkey()
df = pd.DataFrame(data, columns=['sentiment', 'category', 'tag'])
df2 = pd.DataFrame(ct_data, columns=['tag', 'category'])
df3 = pd.DataFrame(k_data, columns=['tag', 'title', 'summary'])



group_sentiment = df.groupby(['tag', 'category'])['sentiment'].mean().reset_index()

cat_and_tag = df2.groupby(['category', 'tag']).size().reset_index().rename(columns={0: 'count'})

st.title('News Sentiment Analysis')

fig = px.bar(group_sentiment, x='category', y='sentiment', color='tag', barmode='group', color_discrete_map = {"west": "blue", "asia": "pink"})
st.plotly_chart(fig)

west = cat_and_tag[cat_and_tag['tag'] == 'west']
asia = cat_and_tag[cat_and_tag['tag'] == 'asia']

west_k = df3[df3['tag'] == 'west']
asia_k = df3[df3['tag'] == 'asia']



west_k_list = (west_k['title'] + ' ' + west_k['summary']).tolist()
asia_k_list = (asia_k['title'] + ' ' + asia_k['summary']).tolist()
west_keywords = get_tfidf_keywords(west_k_list)
asia_keywords = get_tfidf_keywords(asia_k_list)


fig2 = px.pie(west, values='count', names='category')
fig3 = px.pie(asia, values='count', names='category')

col1, col2 = st.columns(2)
with col1:
    st.header('West News Categories')
    st.plotly_chart(fig2)

with col2:
    st.header('Asia News Categories')
    st.plotly_chart(fig3)

col1, col2 = st.columns(2)
with col1:
    st.header('West News Keywords')
    st.write(west_keywords)
with col2:
    st.header('Asia News Keywords')
    st.write(asia_keywords)