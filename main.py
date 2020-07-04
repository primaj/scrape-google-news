from pygooglenews import GoogleNews
import streamlit as st
import pandas as pd

gn = GoogleNews()

f'''
# Google News Feed Searcher
'''

search_term = st.text_input('Search Term:', 'Trump')
search_range = age = st.slider('Search Range (days):', 1, 365, 1)

search = gn.search(search_term, when=f'{search_range}d')

data = pd.DataFrame.from_dict(search['entries'])

# ['guidislink', 'id', 'link', 'links', 'published', 'published_parsed',
#  'source', 'sub_articles', 'summary', 'summary_detail', 'title',
#   'title_detail']

st.write(f"""
## {search_term} News Articles
Last *{search_range} day/s*
""")

# st.write(data['title'].tolist())

for row in range(1, data.shape[1]):

    st.write(f"### {data['published'].iloc[row]} - {data['title'].iloc[row]}")
    st.write(f"Link: {data['link'].iloc[row]}")
