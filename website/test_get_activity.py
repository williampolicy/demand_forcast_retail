import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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


print(f'special_dates_df:\n',special_dates_df)
print(f'special_dates_df.iterrows()\n',special_dates_df.iterrows())

# 根据特殊日期增加活动级别
for _, row in special_dates_df.iterrows():
    base_activity_levels.loc[row['start_date']:row['end_date']] += activity_level_increments[row['type']]

# 确保活动级别在0和1之间
base_activity_levels = base_activity_levels.clip(0, 1)

# 打印活动级别
print(base_activity_levels)

# 可视化活动级别
base_activity_levels.plot()
plt.show()
