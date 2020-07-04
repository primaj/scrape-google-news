from pygooglenews import GoogleNews
import streamlit as st
import pandas as pd

f'''
-----------------------------------

# Google News Feed Searcher

-----------------------------------
'''

gn = GoogleNews()

search_term = st.text_input('Search Term:', 'Trump')
search_range = st.slider('Search Range (days):', 1, 365, 1)

search = gn.search(search_term, when=f'{search_range}d')

data = pd.DataFrame.from_dict(search['entries'])

f'''
# {search_term} News Articles
Last *{search_range} day/s*

------------------------------------------- 
'''


for row in range(1, data.shape[1]):

    f'''
    ## {data['published'].iloc[row]}
    ### {data['title'].iloc[row]}
    Link: {data['link'].iloc[row]}
    
    ------------------------------------------- 
    '''



