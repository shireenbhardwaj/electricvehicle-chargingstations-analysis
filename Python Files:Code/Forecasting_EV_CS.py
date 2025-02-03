#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 17:56:32 2024

@author: shireenbhardwaj
"""

'''Forecasting Overall US EV Registrations Data'''

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Cleaning up the extracted data and preparing it for the regression model
data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Number of EV Registrations': [572600, 783600, 1018900, 1454400, 2442300]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert 'Year' to a numerical feature for regression
df['Year'] = pd.to_numeric(df['Year'])

# Prepare the features and target variable for the regression model
X = df[['Year']]  # Features (2D array for sklearn)
y = df['Number of EV Registrations']  # Target variable

# Initialize and fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Forecasting for the next 5 years
forecast_years = np.array([[year] for year in range(2023, 2028)])
forecast_ev_registrations = model.predict(forecast_years)

# Creating a DataFrame for the forecasted values
forecast_df = pd.DataFrame({
    'Year': range(2023, 2028),
    'Forecasted EV Registrations': forecast_ev_registrations.astype(int)
})

forecast_df


'''Forecasting State-wise EV Registrations Data'''

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Load your DataFrame with data
df = pd.read_excel('EV_registrations.xlsx', sheet_name='Ratios')  # Update 'your_data.csv' with your file path

# Convert 'Year' to a numerical feature for regression
df['Year'] = pd.to_numeric(df['Year'])

# Define a function for forecasting EV registrations for each state
def forecast_for_state(state_df):
    X = state_df[['Year']]  # Features (2D array for sklearn)
    y = state_df['Number of Registrations']  # Target variable

    # Initialize and fit the linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Forecasting for the next 5 years
    forecast_years = np.array([[year] for year in range(2023, 2028)])
    forecast_ev_registrations = model.predict(forecast_years)

    # Creating a DataFrame for the forecasted values
    forecast_df = pd.DataFrame({
        'Year': range(2023, 2028),
        'Forecasted EV Registrations': forecast_ev_registrations.astype(int)
    })

    return forecast_df

# Initialize an empty DataFrame to store forecast results for all states
all_forecasts = pd.DataFrame()

# Iterate over unique states and perform forecasting for each state
for state_name in df['State'].unique():
    state_df = df[df['State'] == state_name]
    state_forecast = forecast_for_state(state_df)
    state_forecast['State'] = state_name
    all_forecasts = pd.concat([all_forecasts, state_forecast])

# Reset index for the final DataFrame
all_forecasts.reset_index(drop=True, inplace=True)

# Display the forecast DataFrame
print(all_forecasts)

# Save the forecast DataFrame to an Excel file
all_forecasts.to_excel('forecast_results.xlsx', index=False)


'''Forecasting Overall US Charging Stations Data'''

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Cleaning up the extracted data and preparing it for the regression model
data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Number of Charging Stations': [3023, 3828, 7513, 17326, 12218]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert 'Year' to a numerical feature for regression
df['Year'] = pd.to_numeric(df['Year'])

# Prepare the features and target variable for the regression model
X = df[['Year']]  # Features (2D array for sklearn)
y = df['Number of Charging Stations']  # Target variable

# Initialize and fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Forecasting for the next 5 years
forecast_years = np.array([[year] for year in range(2023, 2028)])
forecast_charging_stations = model.predict(forecast_years)

# Creating a DataFrame for the forecasted values
forecast_df = pd.DataFrame({
    'Year': range(2023, 2028),
    'Forecasted Charging Stations': forecast_charging_stations.astype(int)
})

forecast_df

'''Forecasting State-wise Charging Stations Data'''

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Load your DataFrame with data
df = pd.read_excel('EV_registrations.xlsx', sheet_name='Ratios')

# Convert 'Year' to a numerical feature for regression
df['Year'] = pd.to_numeric(df['Year'])

# Define a function for forecasting charging stations for each state
def forecast_for_state(state_df):
    X = state_df[['Year']]  # Features (2D array for sklearn)
    y = state_df['Number of Charging Stations']  # Target variable

    # Initialize and fit the linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Forecasting for the next 5 years
    forecast_years = np.array([[year] for year in range(2023, 2028)])
    forecast_charging_stations = model.predict(forecast_years)

    # Creating a DataFrame for the forecasted values
    forecast_df = pd.DataFrame({
        'Year': range(2023, 2028),
        'Forecasted Charging Stations': forecast_charging_stations.astype(int)
    })

    return forecast_df

# Initialize an empty DataFrame to store forecast results for all states
all_forecasts = pd.DataFrame()

print(df.columns)

# Iterate over unique states and perform forecasting for each state
for state_name in df['State'].unique():
    state_df = df[df['State'] == state_name]
    state_forecast = forecast_for_state(state_df)
    state_forecast['State'] = state_name
    all_forecasts = pd.concat([all_forecasts, state_forecast])

# Reset index for the final DataFrame
all_forecasts.reset_index(drop=True, inplace=True)

# Display the forecast DataFrame
print(all_forecasts)

# Save the forecast DataFrame to an Excel file
all_forecasts.to_excel('charging_station_forecast_results.xlsx', index=False)
