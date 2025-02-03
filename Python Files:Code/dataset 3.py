#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 11:43:12 2024

@author: a613373464
"""
import pandas as pd
stations_data=pd.read_csv('/Users/a613373464/Downloads/alt_fuel_stations (Feb 27 2024)(1).csv')

##checking missing values
missing_values = stations_data.isnull().sum()
missing_values

stations_data.info()
stations_data.columns

new_df=stations_data[['Fuel Type Code','Station Name','Street Address', 'City','State','ZIP','Latitude','Longitude','Open Date','Country','EV Workplace Charging']]

##drop rows with missing values in those columns
##check new dataset missg value
new_df.isnull().sum()
new_stations_data= new_df.dropna()
new_stations_data.isnull().sum()
new_stations_data.shape


##filter rows where Fuel Type Code is 'ELEC'
filtered_data = new_stations_data[new_stations_data['Fuel Type Code'] == 'ELEC']

# Convert 'Open Date' to datetime format
filtered_data['Open Date'] = pd.to_datetime(filtered_data['Open Date'])
# Extract year from 'Open Date'
filtered_data['Year'] = filtered_data['Open Date'].dt.year
# Count the number of stations opened each year
stations_per_year = filtered_data.groupby('Year').size().reset_index(name='Number_of_Stations')
# Sort the grouped data by the number of stations in ascending order
stations_per_year_sorted = stations_per_year.sort_values(by='Year', ascending=True)



import matplotlib.pyplot as plt

stations_per_year.plot(kind='line', figsize=(10, 6), marker='o')  # 'marker' adds markers on data points for better visibility
plt.title('Number of Stations Opened per Year')
plt.xlabel('Year')
plt.ylabel('Number of Stations')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

















##not right
# Group the DataFrame by the 'State' column
grouped_by_state = new_stations_data.groupby('State')
# Calculate the number of stations in each state
stations_per_state = grouped_by_state.size().reset_index(name='Number_of_Stations')

# Sort the grouped data by the number of stations in ascending order
grouped_by_state_sorted = stations_per_state.sort_values(by='Number_of_Stations', ascending=False)




import matplotlib.pyplot as plt


# Plotting the number of charging stations per state
grouped_by_state_sorted.plot(kind='bar',x='State', y='Number_of_Stations', figsize=(12, 6))
plt.title('Number of Charging Stations per State')
plt.xlabel('State')
plt.ylabel('Number of Charging Stations')
plt.xticks(rotation=90)
plt.grid(axis='y')  # Add grid lines along the y-axis
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()
















