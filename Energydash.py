import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

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
        "2022 Building Energy Efficiency Standards", "2021 IECC and 90.1-2019",
        "2021 IECC and 90.1-2019", "2018 IECC and 90.1-2016", "90.1-2013",
        "2021 IECC and 90.1-2019", "2015 IECC and 90.1-2013", "2018 IECC and 90.1-2016",
        "2018 IECC and 90.1-2016", "2021 IECC and 90.1-2019", "90.1-2007", 
        "2012 IECC and 90.1-2010", "Home rule", "2012 IECC and 90.1-2010", 
        "2021 IECC and 90.1-2019", "2015 IECC and 90.1-2013", "2021 IECC and 90.1-2019",
        "2018 IECC and 90.1-2016", "2015 IECC and 90.1-2013", "90.1-2019", 
        "None statewide", "Home rule", "2021 IECC and 90.1-2019", 
        "2018 IECC and 90.1-2016", "2018 IECC and 90.1-2016", "2018 IECC and 90.1-2016", 
        "90.1-2019", "2021 IECC and 90.1-2019", "2018 IECC and 90.1-2016", 
        "2015 IECC and 90.1-2013", "2021 IECC and 90.1-2019", 
        "2006 IECC and 90.1-2004", "90.1-2019", "2018 IECC and 90.1-2016", 
        "2018 IECC and 90.1-2016", "2009 IECC and 90.1-2007", "Home rule", 
        "2012 IECC and 90.1-2010", "2015 IECC and 90.1-2013", 
        "2021 IECC and 90.1-2019", "2018 IECC and 90.1-2016", "2021 IECC and 90.1-2019", 
        "2018 Washington State Energy Code", "90.1-2013", "2015 IECC and 90.1-2013", 
        "Home rule"
    ]
}

# Create dataframes
province_df = pd.DataFrame(province_data)
us_state_df = pd.DataFrame(us_state_data)

# Group the Canadian province dataframe by 'Code' and combine provinces with the same code into a single row
province_df_grouped = province_df.groupby('Code').agg({
    'Province/Territory': ', '.join,
    
}).reset_index()

# Group the US state dataframe by 'Code' and combine states with the same code into a single row
us_state_df_grouped = us_state_df.groupby('Code').agg({
    'State': ', '.join
}).reset_index()

# Handle navigation between tabs using session state
if 'tab' not in st.session_state:
    st.session_state.tab = "Canada"

# Sidebar with clickable text for tabs
st.sidebar.markdown("## Energy Codes")
if st.sidebar.button("Canada"):
    st.session_state.tab = "Canada"
if st.sidebar.button("US"):
    st.session_state.tab = "US"

if st.sidebar.button("Upcoming Codes Timeline"):
    st.session_state.tab = "Timeline"

# Display content based on the selected tab
if st.session_state.tab == "Canada":
    st.header("Canadian Provinces Grouped by Code")
    for _, row in province_df_grouped.iterrows():
        st.markdown(f"**{row['Code']}**: {row['Province/Territory']}")
        # Adding link to PDF file hosted in GitHub repository
    st.sidebar.markdown("### Additional Resources:")
    st.sidebar.markdown("[Canadian Codes Details](https://github.com/Moe-obe/Energydash/blob/main/Energy%20Efficiency%20Codes%20Canada%20-%20Summary.pdf)")

elif st.session_state.tab == "US":
    st.header("US States Grouped by Code")
    for _, row in us_state_df_grouped.iterrows():
        st.markdown(f"**{row['Code']}**: {row['State']}")

    # Add two separate links for IECC and ASHRAE codes on the left side
    st.sidebar.markdown("### Additional Resources:")
    st.sidebar.markdown("[IECC Codes](https://codes.iccsafe.org/codes/i-codes)")
    st.sidebar.markdown("[ASHRAE Code](https://www.ashrae.org/technical-resources/standards-and-guidelines/read-only-versions-of-ashrae-standards)")


elif st.session_state.tab == "Timeline":
    st.header("Upcoming Important Dates")



    # Link to the raw image hosted on GitHub
    image_url = "https://raw.githubusercontent.com/Moe-obe/Energydash/5c38f8a9bb003891c73fae11dd29e53c0c36e4d9/Screenshot%202024-09-27%20184704.png"

# Display the image in Streamlit
    st.image(image_url, caption="Upcoming Codes Timeline", width=1300)
    # Add descriptions and hyperlinks under the timeline image
    st.markdown("""
    ### Related References:
    - [**ASHRAE/IES 90.1-2022 Becomes New National Energy Reference Standard**](https://lightingcontrolsassociation.org/2024/06/20/ddd/#:~:text=ASHRAE%2FIES%2090.1%2D2022%20Becomes%20New%20National%20Energy%20Reference%20Standard,-06%2F20%2F2024&text=In%20March%202024%2C%20the%20U.S.,energy%20over%20the%202019%20version.)
    - [**2024 International Building Code (IBC)**](https://www.structuremag.org/article/2024-ibc-significant-structural-changes-glass-and-glazing-ibc-chapter-24/)
    - [**ASHRAE 90.1 (2025 Edition)**](https://github.com/Moe-obe/Energydash/blob/main/2025code.png)
    - [**California Energy Code (2025 Update)**](https://www.renewableenergymagazine.com/energy_saving/california-adopts-updated-building-standards-expanding-energy-20240912)
    - [**United States Investment Tax Credit (ITC) for High-Performance Glass**](https://www.glass.org/news/2024/defending-and-promoting-glass-industry)
    - [**Climate Challenge (RIBA Standards)**](https://www.guardianglass.com/gb/en/insights/a-window-on-the-future-changes-to-part-l-building-regs)
    """)
