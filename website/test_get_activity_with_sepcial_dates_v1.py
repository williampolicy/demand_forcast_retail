import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def handle_extreme_weather(special_dates_df, base_activity_levels):
    extreme_weather_dates = special_dates_df[special_dates_df['type'] == 'extreme_weather']

    for _, row in extreme_weather_dates.iterrows():
        base_activity_levels[row['start_date'] - pd.Timedelta(days=2):row['start_date'] - pd.Timedelta(days=1)] *= 2
        base_activity_levels[row['start_date']:row['end_date']] *= 0.5
        recovery_dates = pd.date_range(start=row['end_date'] + pd.Timedelta(days=1), periods=min(3, len(base_activity_levels) - row['end_date'].dayofyear))
        for i, date in enumerate(recovery_dates):
            base_activity_levels[date] *= (0.7 + 0.1 * (i + 1))
    
    return base_activity_levels


# 读取特殊日期
special_dates_df = pd.read_csv('../special_dates.csv')
special_dates_df['start_date'] = pd.to_datetime(special_dates_df['start_date'])
special_dates_df['end_date'] = pd.to_datetime(special_dates_df['end_date'])

# 为不同的特殊日期类型设置不同的活动级别增量
activity_level_increments = {
    'discount': 0.2,
    'holiday': 0.1,
    'extreme_weather': -0.1
}

# 创建一个日期范围
dates = pd.date_range(start='2022-01-01', periods=365)

# 创建基础活动级别
base_activity_levels = pd.DataFrame({
    'product1': np.random.uniform(low=0.2, high=0.2, size=365),
    'product2': np.random.uniform(low=0.3, high=0.3, size=365),
    'product3': np.random.uniform(low=0.4, high=0.4, size=365),
    'product4': np.random.uniform(low=0.8, high=0.8, size=365)
}, index=dates)

# 根据特殊日期增加活动级别
for _, row in special_dates_df.iterrows():
    if row['type'] != 'extreme_weather':
        base_activity_levels.loc[row['start_date']:row['end_date']] += activity_level_increments[row['type']]
    else:
        base_activity_levels = handle_extreme_weather(special_dates_df, base_activity_levels)

# 确保活动级别在0和1之间
base_activity_levels = base_activity_levels.clip(0, 1)

# 可视化活动级别
base_activity_levels.plot()
plt.show()
