
import streamlit as st
import pandas



#head to head
newdata=pd.read_csv('pages/teststream.csv')
#headtohead=newdata.groupby(['striker','bowler']).agg({'runs_off_bat': 'sum', 'match_id': 'nunique', 'ball_count': 'sum', 'bowler_out': 'sum','dotball': 'sum','boundary': 'sum'}).reset_index()
#headtohead[headtohead['striker']=='V Kohli']
#st.write(headtohead(x)

#with st.container():
st.title("WELCOME TO matchups")
    #st.sidebar.title("Navigation")
    #x = st.sidebar.selectbox("which city data do u want", headtohead['striker'].unique())
    #city_data = headtohead[headtohead['striker'] == x]
    #st.write(city_data)
