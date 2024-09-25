import streamlit as st
import pandas as pd


# Data for Canadian provinces and US states with codes
province_data = {
    "Province/Territory": [
        "British Columbia", "Alberta", "Saskatchewan", "Manitoba", 
        "Ontario", "Quebec", "New Brunswick", "Nova Scotia",
        "Prince Edward Island", "Newfoundland & Labrador", "Yukon", 
        "Nunavut", "Northwest Territories"
    ],
    "Code": [
        "Energy Step Code / Zero Carbon Step Code", "NECB 2020 (Tier 1)",
        "NECB 2020 (Tier 1)", "NECB 2020 (Tier 1)", "Supplementary Standard SB10",
        "NECB 2015 (amended)", "NECB 2011", "NECB 2017", 
        "NECB 2020 (Tier 1)", "none", "none", "none", "none"
    ],
    "Link": [
        "https://example.com/bc", "https://example.com/alberta", "https://example.com/saskatchewan", 
        "https://example.com/manitoba", "https://example.com/ontario", 
        "https://example.com/quebec", "https://example.com/new-brunswick", 
        "https://example.com/nova-scotia", "https://example.com/prince-edward-island", 
        "https://example.com/newfoundland", "https://example.com/yukon", 
        "https://example.com/nunavut", "https://example.com/northwest-territories"
    ]
}

us_state_data = {
    "State": [
        "Alabama", "Alaska", "Arizona", "Arkansas", "California", 
        "Colorado", "Connecticut", "Delaware", "District of Columbia", 
        "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", 
        "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", 
        "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", 
        "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", 
        "New Hampshire", "New Jersey", "New Mexico", "New York", 
        "North Carolina", "North Dakota", "Oklahoma", "Oregon", 
        "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", 
        "Tennessee", "Texas", "Utah", "Vermont", "Virginia", 
        "Washington", "West Virginia", "Wisconsin", "Wyoming"
    ],
    "Code": [
        "90.1-2013", "None statewide", "Home rule", "2009 IECC and 90.1-2007", 
        "2022 Building Energy Efficiency Standards", "2021-IECC and 90.1-2019",
        "2021 IECC and 90.1-2019", "2018 IECC and 90.1-2016", "90.1-2013",
        "2021 IECC and 90.1-2019", "2015 IECC and 90.1-2013", "2018 IECC and 90.1-2016",
        "2018 IECC and 90.1-2016", "2021 IECC and 90.1-2019", "90.1-2007", 
        "2012 IECC and 90.1-2010", "Home rule", "2012 IECC and 90.1-2010", 
        "2021-IECC and 90.1-2019", "2015 IECC and 90.1-2013", "2021 IECC and 90.1-2019",
        "2018 IECC and 90.1-2016", "2015 IECC and 90.1-2013", "90.1-2019", 
        "None statewide", "Home rule", "2021 IECC and 90.1-2019", 
        "2018 IECC and 90.1-2016", "2018 IECC and 90.1-2016", "2018 IECC and 90.1-2016", 
        "90.1-2019", "2021 IECC and 90.1-2019", "2018 IECC and 90.1-2016", 
        "2015 IECC and 90.1-2013", "2021 IECC and 90.1-2019", 
        "2006 IECC and 90.1-2004", "90.1-2019", "2018 IECC and 90.1-2016", 
        "2018 IECC and 90.1-2016", "2009 IECC and 90.1-2007", "Home rule", 
        "2012 IECC and 90.1-2010", "2015 IECC and 90.1-2013", 
        "2021-IECC and 90.1-2019", "2018 IECC and 90.1-2016", "2021 IECC and 90.1-2019", 
        "2018 Washington State Energy Code", "90.1-2013", "2015 IECC and 90.1-2013", 
        "Home rule"
    ],
    "Link": [
        "https://example.com/alabama", "https://example.com/alaska", "https://example.com/arizona", 
        "https://example.com/arkansas", "https://example.com/california", "https://example.com/colorado", 
        "https://example.com/connecticut", "https://example.com/delaware", 
        "https://example.com/district-of-columbia", "https://example.com/florida", 
        "https://example.com/georgia", "https://example.com/hawaii", 
        "https://example.com/idaho", "https://example.com/illinois", 
        "https://example.com/indiana", "https://example.com/iowa", 
        "https://example.com/kansas", "https://example.com/kentucky", 
        "https://example.com/louisiana", "https://example.com/maine", 
        "https://example.com/maryland", "https://example.com/massachusetts", 
        "https://example.com/michigan", "https://example.com/minnesota", 
        "https://example.com/mississippi", "https://example.com/missouri", 
        "https://example.com/montana", "https://example.com/nebraska", 
        "https://example.com/nevada", "https://example.com/new-hampshire", 
        "https://example.com/new-jersey", "https://example.com/new-mexico", 
        "https://example.com/new-york", "https://example.com/north-carolina", 
        "https://example.com/north-dakota", "https://example.com/oklahoma", 
        "https://example.com/oregon", "https://example.com/pennsylvania", 
        "https://example.com/rhode-island", "https://example.com/south-carolina", 
        "https://example.com/south-dakota", "https://example.com/tennessee", 
        "https://example.com/texas", "https://example.com/utah", 
        "https://example.com/vermont", "https://example.com/virginia", 
        "https://example.com/washington", "https://example.com/west-virginia", 
        "https://example.com/wisconsin", "https://example.com/wyoming"
    ]
}

# Create dataframes
province_df = pd.DataFrame(province_data)
us_state_df = pd.DataFrame(us_state_data)

# Group the Canadian province dataframe by 'Code' and combine provinces with the same code into a single row
province_df_grouped = province_df.groupby('Code').agg({
    'Province/Territory': ', '.join,
    'Link': 'first'  # Keep the first link, since all grouped entries will have the same code
}).reset_index()

# Group the US state dataframe by 'Code' and combine states with the same code into a single row
us_state_df_grouped = us_state_df.groupby('Code').agg({
    'State': ', '.join,
    'Link': 'first'  # Keep the first link, similar logic as with provinces
}).reset_index()

# Tabs to switch between Canada and US data
tabs = st.tabs(["Canada", "US"])

# Canada tab
with tabs[0]:
    st.header("Canadian Provinces Grouped by Code")
    for _, row in province_df_grouped.iterrows():
        st.markdown(f"**{row['Code']}**: {row['Province/Territory']} [Link]({row['Link']})")

# US tab
with tabs[1]:
    st.header("US States Grouped by Code")
    for _, row in us_state_df_grouped.iterrows():
        st.markdown(f"**{row['Code']}**: {row['State']} [Link]({row['Link']})")
