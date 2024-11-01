import streamlit as st
import pandas as pd
import snowflake.connector
import streamlit_option_menu
from streamlit_option_menu import option_menu

# !pip install streamlit
# !pip install snowflake-connector-python
# !pip install streamlit_option_menu

# %%writefile app.py

from PIL import Image

st.write('Hello, *World!* :sunglasses:') # 해당 내용을 수정해서 사이트를 자유롭게 꾸밀 수 있다.

st.title('this is title')
st.header('this is header')
st.subheader('this is subheader')

# 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다.
tab1, tab2= st.tabs(['Tab A' , 'Tab B'])

with tab1:
  #tab A 를 누르면 표시될 내용
  st.write('hello')

with tab2:
  #tab B를 누르면 표시될 내용
  st.write('hi')

# 데이터 프레임
import pandas as pd
df = pd.DataFrame({
     '첫 번째 컬럼': [1, 2, 3, 4],
     '두 번째 컬럼': [10, 20, 30, 40]
     })
st.write(df)



import urllib
print("Password/Enpoint IP for localtunnel is:",urllib.request.urlopen('https://ipv4.icanhazip.com').read().decode('utf8').strip("\n"))

# !npm install localtunnel
# !streamlit run app.py &>/content/logs.txt &
# !npx localtunnel --port 8501
with st.sidebar:
  selected = option_menu(
    menu_title = "Main Menu",
    options = ["Home","Projects","Contact"],
    icons = ["house","book","envelope"],
    menu_icon = "cast",
    default_index = 0,

  )
  if selected == "Home":
    st.title(f"You Have selected {selected}")
    st.header('Snowflake Healthcare App')
    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    my_cur = my_cnx.cursor()
    # run a snowflake query and put it all in a var called my_catalog
    my_cur.execute("select * from SWEATSUITS")
    my_catalog = my_cur.fetchall()
    st.dataframe(my_catalog)
    q1 = st.text_input('Write your query','')
    st.button('Run Query')
    if not q1:
      st.error('Please write a query')
    else:
      my_cur.execute(q1)
      my_catalog = my_cur.fetchall()
      st.dataframe(my_catalog)
  if selected == "Projects":
    st.title(f"You Have selected {selected}")
  if selected == "Contact":
    st.title(f"You Have selected {selected}")
# %%
