#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 00:53:39 2024

@author: weichunghsia
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


file_path = '/Users/weichunghsia/Downloads/Final_merged-dataset.xlsx'
all_sheets = pd.read_excel(file_path, sheet_name=None)


ev_registrations_data = all_sheets['EV Registrations']
state_wise_stations = all_sheets['State-wise Stations and Income']


all_years_merged = pd.merge(state_wise_stations[['Year', 'State', 'Number of Charging Stations']], 
                            ev_registrations_data[['Year', 'State', 'Number of Registrations']],
                            on=['Year', 'State'])


correlation_results = {}
for year in sorted(all_years_merged['Year'].unique()):
    year_data = all_years_merged[all_years_merged['Year'] == year]
    slope, intercept, r_value, p_value, std_err = linregress(year_data['Number of Registrations'], year_data['Number of Charging Stations'])
    correlation_results[year] = (r_value, p_value)


    plt.figure(figsize=(10, 6))
    plt.scatter(year_data['Number of Registrations'], year_data['Number of Charging Stations'], color='blue', alpha=0.5)
    x = np.linspace(year_data['Number of Registrations'].min(), year_data['Number of Registrations'].max(), 100)
    y = slope * x + intercept
    plt.plot(x, y, color='red', label=f'Linear Fit (r={r_value:.2f})')
    plt.title(f'{year} EV Registrations vs. Charging Stations')
    plt.xlabel('Number of EV Registrations')
    plt.ylabel('Number of Charging Stations')
    plt.legend()
    plt.grid(True)
    plt.show()


print("Yearly correlation results:")
for year, results in correlation_results.items():
    r_value, p_value = results
    print(f"Year {year}: Correlation coefficient = {r_value:.3f}, p-value = {p_value:.3e}")


for year, results in correlation_results.items():
    _, p_value = results
    if p_value < 0.05:
        print(f"Year {year}: Reject H0, significant positive correlation.")
    else:
        print(f"Year {year}: Fail to reject H0, no significant correlation.")
