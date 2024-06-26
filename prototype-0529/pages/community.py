import streamlit as st
import pandas as pd
import pymysql
import datetime
from sqlalchemy import create_engine 

login_nickname = st.session_state.login_nickname

db_config = {
    'host': 'localhost',      
    'user': 'kivotos', 
    'password': 'kivotos2024!',  
    'database': 'project', 
    'port': 3306,             
    'charset': 'utf8mb4'      
}

st.title('Infographic Generator')
st.header('Infographic Generator Community', divider='rainbow')

db_url = f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}"
engine = create_engine(db_url)

def comment_view():
    try:
        query = "SELECT sequence,input_date,id,comment_title,user_comment FROM user_comment ORDER BY sequence DESC "

        df = pd.read_sql(query, engine)
        if df.empty:
            st.write('No Comment In Community')

        else:
            if "df" not in st.session_state:
                st.session_state.df = df
            
            column_config = {
                "sequence": 'Number', 
                "input_date": "Input Date",  
                "id": 'ID',  
                "comment_title": "Title",
                "user_comment" : None 
            }
            
            selected_data = st.dataframe(
                st.session_state.df,
                key="data",
                on_select="rerun",
                selection_mode=["single-row"],
                hide_index= True,
                column_config=column_config
            )

            selected_index = selected_data["selection"]["rows"]
            

            if selected_index:
                selected_row = st.session_state.df.iloc[selected_index[0]] 
                container = st.container(border=True) 
                container.write(f"Input Date: {selected_row['input_date']}")
                container.write(f"ID: {selected_row['id']}")
                container.write(f"Title: {selected_row['comment_title']}")
                container.write("User Comment")
                container.write(f"{selected_row['user_comment']}") 

            else:
                st.write("No Selected Data")


    except Exception as e:
        st.error(f"Error: {e}")    

tab1,tab2 = st.tabs(['Comment View','Comment Writing'])

with tab1:
    if login_nickname == 'Unknown':
        comment_view()
            
    else:
        st.write('Welcome! ' + login_nickname)
        comment_view()

with tab2:
    if login_nickname != 'Unknown':
        input_id = login_nickname
        input_comment_title = st.text_input('Commnent Title','', key='comment_title')
        input_comment = st.text_area('Your Comment','', key='comment')
        input_date = datetime.datetime.today()

        if st.button('Submit!'):
            try:
                connection = pymysql.connect(**db_config)
                cursor = connection.cursor()
                query = 'INSERT INTO user_comment(id, comment_title, user_comment, input_date) VALUES(%s, %s, %s, %s)'
                cursor.execute(query, (input_id, input_comment_title, input_comment, input_date))
                connection.commit()
                st.success('Successful Comment Submit!')
            except pymysql.Error as e:
                st.error(f'An error occurred: {e}')
            finally:
                if connection:
                    cursor.close()
                    connection.close()

    else:
        st.error('You have to login first!')