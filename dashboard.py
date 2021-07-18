import streamlit as st
import pandas as pd
import numpy as np
from database_ops import db_execute_fetch

def main():
    st.title("TellCo Data Analytics Dashboard")

    st.sidebar.write("Navigation")
    app_mode = st.sidebar.selectbox("Choose Here", ("Home", "Univariate Analysis"))
    if app_mode == 'Home':
        st.write('''
        ## Introduction
        In this project, we are analyzing the customer information of a company called TellCo, an existing mobile service provider in the 
        Republic of Pefkakia. Our objective is to provide a report to analyze opportunities for growth and make a recommendation on whether 
        TellCo is worth buying or selling.
        ''')
        dataframe = db_execute_fetch("Select * from satisfaction_scores;", dbName = 'telecom_user_satisfaction')
        st.write('''
        ## Some overview of the data
        ''')
        st.table(dataframe.sample(5))

        st.write('''
            ## Some overview per user type
            ''')

        display_mode = st.selectbox("Choose the type of user", ("Type 0 users", "Type 1 users"))
        if display_mode == 'Type 0 users':
            st.write('''
            ## Some overview of Type 0 users
            ''')
            st.subheader('Sample type 0 users')
            st.table(dataframe[dataframe['Cluster'] == 0].sample(2))
            st.subheader('Statistics on attributes of type 0 users')
            st.table(dataframe[dataframe['Cluster'] == 0][['Engagement_Score', 'Experience_Score',	'Satisfaction_Score']].describe())

        elif display_mode == 'Type 1 users':
            st.write('''
            ## Some overview of Type 1 users
            ''')
            st.subheader('Sample type 1 users')
            st.table(dataframe[dataframe['Cluster'] == 1].sample(2))
            st.subheader('Statistics on attributes of type 1 users')
            st.table(dataframe[dataframe['Cluster'] == 1][['Engagement_Score', 'Experience_Score',	'Satisfaction_Score']].describe())

    elif app_mode == 'Univariate Analysis':
        st.write('''
        ## Here are a few plots of the variables
        ''')
        dataframe = db_execute_fetch("Select * from satisfaction_scores;", dbName = 'telecom_user_satisfaction')

        st.subheader('Engagement Score Plot')
        hist_values = np.histogram(dataframe['Engagement_Score'], bins=50)[0]
        st.bar_chart(hist_values)

        st.subheader('Experience Score Plot')
        hist_values = np.histogram(dataframe['Experience_Score'], bins=50)[0]
        st.bar_chart(hist_values)

        st.subheader('Satisfaction Score Plot')
        hist_values = np.histogram(dataframe['Satisfaction_Score'], bins=50)[0]
        st.bar_chart(hist_values)

        st.subheader('Cluster Plot')
        hist_values = np.histogram(dataframe['Cluster'], bins=2)[0]
        st.bar_chart(hist_values)
    
if __name__ == "__main__":
    main()