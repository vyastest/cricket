import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="Main App",
)



newdata=pd.read_csv('teststream.csv')

#data = pd.read_csv(filepath)
#data['Sale Date'] = pd.to_datetime(data['Sale Date'], errors='coerce')
#data[['Sales (Exc. Tax)', 'Tax', 'Sales(Inc. Tax)', 'Redeemed']] = data[['Sales (Exc. Tax)', 'Tax', 'Sales(Inc. Tax)', 'Redeemed']].replace(',', '', regex=True).astype(float)
#return data.dropna(subset=['Sale Date'])

#bowleraggregateddata
bowlerdata=newdata.groupby(['bowler']).agg({'bowler_conceded_runs': 'sum', 'match_id': 'nunique', 'ball_count': 'sum', 'bowler_out': 'sum','bowlerdotball': 'sum','boundary': 'sum','noballcount': 'sum'}).reset_index()
bowlerdata['total_balls']=bowlerdata['ball_count']-bowlerdata['noballcount']
bowlerdata['balls_per_over'] = 6
bowlerdata['overs'] = bowlerdata['total_balls'] // bowlerdata['balls_per_over']
bowlerdata['balls_in_last_over'] = bowlerdata['total_balls'] % bowlerdata['balls_per_over']
bowlerdata['final_overs'] = bowlerdata['overs'] + bowlerdata['balls_in_last_over'] / 10
bowlerdata[bowlerdata['bowler']=='JJ Bumrah']


bowlerdata['average']=bowlerdata['bowler_conceded_runs']/bowlerdata['bowler_out']
bowlerdata['economy']=(bowlerdata['bowler_conceded_runs']/bowlerdata['total_balls'])*6

bowlerdata['strike_rate']=bowlerdata['total_balls']/bowlerdata['bowler_out']
bowlerdata['dot_percent']=(bowlerdata['bowlerdotball']/bowlerdata['total_balls'])*100
bowlerdata['bpb']=bowlerdata['total_balls']/bowlerdata['boundary']
bowlerdata[bowlerdata['bowler']=='JJ Bumrah']


# Specify the desired column order
desired_columns = ['bowler','match_id','final_overs' ,'bowler_conceded_runs', 'bowler_out','average','economy','strike_rate','dot_percent','bpb']

# Create a new DataFrame with the specified column order
bowlerdata = bowlerdata[desired_columns]

#sample
#batterdata3[batterdata3['batsman']=='SPD Smith']
st.write(bowlerdata[bowlerdata['bowler']=='JJ Bumrah'])
#bowlerdata[bowlerdata['bowler_out']>100]
#bowlerdata



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



if __name__ == "__main__":
    main()
