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
    st.header("Upcoming Codes Timeline")



    # Timeline data (keeping the same data from before)
    timeline_data = [
        {"year": "2024", "event": "2024 International Building Code (IBC)\nStricter safety requirements for glazing systems."},
        {"year": "2025", "event": "ASHRAE 90.1 (2025 Edition)\nStricter energy efficiency requirements for building envelopes, HVAC systems, and glazing."},
        {"year": "2025", "event": "California Energy Code (2025 Update)\nStricter energy performance standards for glazing and windows."},
        {"year": "2026", "event": "Energy Performance of Buildings Directive (EPBD)\nEU aiming for nearly zero-energy buildings."},
        {"year": "2026", "event": "United States Investment Tax Credit (ITC)\nExpansion of tax credits for high-performance glass."},
        {"year": "2030", "event": "2030 Climate Challenge (RIBA Standards)\nAmbitious goals for reducing carbon emissions and energy consumption."}
    ]

    # Convert the timeline data into a pandas DataFrame
    timeline_df = pd.DataFrame(timeline_data)
    timeline_df['year'] = pd.to_datetime(timeline_df['year'], format='%Y')  # Convert years to datetime for plotting

    # New Timeline Graph for the "Upcoming Codes Timeline" tab
    

    # Plot the timeline
    with plt.style.context("fivethirtyeight"):
        fig, ax = plt.subplots(figsize=(30, 18))
        fig.patch.set_alpha(0)  # Make the figure background transparent
        ax.patch.set_alpha(0)   # Make the axis background transparent

        # Plot the main line for the timeline
        ax.plot(timeline_df.year, [0] * len(timeline_df), "-o", color="black", markerfacecolor="white")

        # Set the x-ticks with the range of years, manually adjust limits
        ax.set_xticks(pd.date_range("2024-1-1", "2030-1-1", freq="YS"))
        ax.set_xlim(pd.to_datetime("2023-06-01"), pd.to_datetime("2031-01-01"))
        ax.set_ylim(-7, 6)

        # Annotate each event along the timeline
        for idx in range(len(timeline_df)):
            dt, event = timeline_df["year"][idx], timeline_df["event"][idx]
            level = 4 if idx % 2 == 0 else -4  # Alternate placing the event above and below the line

            ax.annotate(event, xy=(dt, 0.2 if level > 0 else -0.2), xytext=(dt, level),
                        arrowprops=dict(arrowstyle="-", color="red", linewidth=2),
                        ha="center", fontsize=20, bbox=dict(boxstyle="round,pad=0.3", edgecolor="white", facecolor="white"))

        # Remove unnecessary spines
        ax.spines[["left", "top", "right", "bottom"]].set_visible(False)
        ax.spines[["bottom"]].set_position(("axes", 0.5))

        # Hide the y-axis
        ax.yaxis.set_visible(False)

        # Set the title for the timeline
        ax.set_title(" ", pad=10, loc="left", fontsize=50, fontweight="bold")
        ax.grid(False)

        # Display the timeline in Streamlit
        st.pyplot(fig)
