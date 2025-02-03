#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 01:03:21 2024

@author: weichunghsia
"""

import numpy as np
import matplotlib.pyplot as plt

# Data for EV registrations and charging stations for two periods
data_2018_2023 = {
    'Year': [2018, 2019, 2020, 2021, 2022, 2023],
    'EV Registrations': [572600, 783600, 1018900, 1454400, 2442300, 2577420],
    'Charging Stations': [3023, 3828, 7513, 17326, 12218, 18348]
}

data_2024_2027 = {
    'Year': [2024, 2025, 2026, 2027],
    'EV Registrations': [3018440, 3459460, 3900480, 4341500],
    'Charging Stations': [21536, 24725, 27914, 31103]
}

# Separate the data into two periods
period1_ev = np.array(data_2018_2023['EV Registrations'])
period1_cs = np.array(data_2018_2023['Charging Stations'])
period2_ev = np.array(data_2024_2027['EV Registrations'])
period2_cs = np.array(data_2024_2027['Charging Stations'])

# Perform linear regression for both periods to get slopes and intercepts
slope1, intercept1 = np.polyfit(period1_ev, period1_cs, 1)
slope2, intercept2 = np.polyfit(period2_ev, period2_cs, 1)

# Generate x and y values for the fit lines
fit_line1_x = np.linspace(period1_ev.min(), period1_ev.max(), 100)
fit_line1_y = slope1 * fit_line1_x + intercept1
fit_line2_x = np.linspace(period2_ev.min(), period2_ev.max(), 100)
fit_line2_y = slope2 * fit_line2_x + intercept2

# Create the scatter plot with separate fit lines for the two periods
plt.figure(figsize=(12, 6))
plt.scatter(period1_ev, period1_cs, color='blue', label='2018-2023 Data Points')
plt.plot(fit_line1_x, fit_line1_y, color='blue', label='2018-2023 Fit Line')
plt.scatter(period2_ev, period2_cs, color='green', label='2024-2027 Data Points')
plt.plot(fit_line2_x, fit_line2_y, color='green', label='2024-2027 Fit Line')

# Label the plot
plt.title('Relationship between EV Registrations and Charging Stations by Period')
plt.xlabel('EV Registrations')
plt.ylabel('Charging Stations')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()