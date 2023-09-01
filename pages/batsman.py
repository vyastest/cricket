import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(
    page_title="bastman App",
)



newdata=pd.read_csv('teststream.csv')
#striker innings count
strikerdata=newdata.groupby(['striker','match_id'])['start_date'].count().reset_index()
new_column_name = 'strikercount'
strikerdata.rename(columns={'start_date': new_column_name}, inplace=True)
strikerdata

#nonstrikerinningscount
nonstrikerdata=newdata.groupby(['non_striker','match_id'])['start_date'].count().reset_index()
nonstrikerdata
new_column_name = 'nonstrikercount'
nonstrikerdata.rename(columns={'start_date': new_column_name}, inplace=True)
nonstrikerdata

#merge the data
mergedstrikerdata=nonstrikerdata.merge(strikerdata,how='left',left_on=['non_striker','match_id'],right_on=['striker','match_id'])


# non striker innings count by players
mergedstrikerdata2=mergedstrikerdata[mergedstrikerdata['strikercount'].isna()]
mergedstrikerdata3=mergedstrikerdata2.groupby('non_striker')['match_id'].count().reset_index()
new_column_name = 'inningscount'
mergedstrikerdata3.rename(columns={'match_id': new_column_name}, inplace=True)


#combine data to get batting chart
batterdata=newdata.groupby('striker').agg({'runs_off_bat': 'sum', 'match_id': 'nunique', 'ball_count': 'sum', 'striker_out': 'sum','dotball': 'sum','boundary': 'sum'}).reset_index()
batterdata[batterdata['striker']=='V Kohli']
nonstrikeroutdata=newdata.groupby('non_striker')['non_striker_out'].sum()
batterdata2=batterdata.merge(nonstrikeroutdata,how='outer',left_on='striker',right_on='non_striker')
batterdata3=batterdata2.merge(mergedstrikerdata3,how='outer',left_on='striker',right_on='non_striker')
batterdata3['match_id']=np.where(pd.isna(batterdata3['match_id']),0,batterdata3['match_id'])
batterdata3['inningscount']=np.where(pd.isna(batterdata3['inningscount']),0,batterdata3['inningscount'])
batterdata3['total_innings']=batterdata3['match_id'] + batterdata3['inningscount']
#np.where(pd.isna(data), 0, 1)
batterdata3['total_out']=batterdata3['striker_out']+batterdata3['non_striker_out']


# Apply the conditions to create the new column
batterdata3['batsman'] = batterdata3.apply(lambda row: row['non_striker'] if pd.isna(row['striker']) else row['striker'], axis=1)


batterdata3['average']=batterdata3['runs_off_bat']/batterdata3['total_out']
batterdata3['strike_rate']=(batterdata3['runs_off_bat']/batterdata3['ball_count'])*100
batterdata3['dot_percent']=(batterdata3['dotball']/batterdata3['ball_count'])*100
batterdata3['bpb']=batterdata3['ball_count']/batterdata3['boundary']



# Specify the desired column order
desired_columns = ['batsman','total_innings', 'runs_off_bat', 'ball_count','total_out','average','strike_rate','dot_percent','bpb']

# Create a new DataFrame with the specified column order
batterdata3 = batterdata3[desired_columns]

#sample
#batterdata3[batterdata3['batsman']=='SPD Smith']
st.write(batterdata3[batterdata3['runs_off_bat']>50])

#batterdata3




#def main():
    #st.sidebar.title("Navigation")

    # New dataset filter
    #datasets = ["For 08-2019 to 06-2023", "For 01-2017 to 06-2019"]

    # Default to the first dataset ("For 08-2019 to 06-2023")
    #selected_dataset = st.sidebar.selectbox("Select Dataset", datasets, index=0)

    #pages = ["Sales Summary by Center and Date", "Sales Summary by Year"]
    #selected_page = st.sidebar.selectbox("Go to", pages)

    #if selected_page == "Sales Summary by Center and Date":
        #center_date_summary(selected_dataset)
    #elif selected_page == "Sales Summary by Year":
        #year_summary(selected_dataset)



#if __name__ == "__main__":
    #main()
