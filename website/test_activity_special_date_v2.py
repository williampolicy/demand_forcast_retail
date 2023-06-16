import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def prepare_data():
    # Read special dates
    special_dates = pd.read_csv('../special_dates.csv')
    special_dates['start_date'] = pd.to_datetime(special_dates['start_date'])
    special_dates['end_date'] = pd.to_datetime(special_dates['end_date'])

    # Set different activity level increments for different types of special dates
    activity_increments = {
        'discount': 0.2,
        'holiday': 0.1,
        'extreme_weather': -0.1
    }

    # Create a date range
    dates = pd.date_range(start='2022-01-01', periods=365)

    # Create base activity levels
    demand = pd.DataFrame({
        'product1': np.random.uniform(low=0.2, high=0.2, size=365),
        'product2': np.random.uniform(low=0.3, high=0.3, size=365),
        'product3': np.random.uniform(low=0.4, high=0.4, size=365),
        'product4': np.random.uniform(low=0.8, high=0.8, size=365)
    }, index=dates)

    return special_dates, activity_increments, demand

def handle_special_dates(special_dates, demand, activity_increments):
    for _, row in special_dates.iterrows():
        if row['type'] in ['discount', 'holiday']:
            demand.loc[row['start_date']:row['end_date'], :] += activity_increments[row['type']]
    return demand

def handle_extreme_weather(special_dates, demand):
    extreme_weather_dates = special_dates[special_dates['type'] == 'extreme_weather']

    for _, row in extreme_weather_dates.iterrows():
        demand.loc[row['start_date'] - pd.Timedelta(days=2):row['start_date'] - pd.Timedelta(days=1), :] *= 2
        demand.loc[row['start_date']:row['end_date'], :] *= 0.5
        recovery_dates = pd.date_range(start=row['end_date'] + pd.Timedelta(days=1), periods=min(3, len(demand) - row['end_date'].dayofyear))
        for i, date in enumerate(recovery_dates):
            if date in demand.index:
                demand.loc[date, :] *= (0.7 + 0.1 * (i + 1))
    
    return demand

special_dates, activity_increments, demand = prepare_data()
demand = handle_special_dates(special_dates, demand, activity_increments)
demand = handle_extreme_weather(special_dates, demand)
demand = demand.clip(0, 1)
demand.plot()
plt.show()
