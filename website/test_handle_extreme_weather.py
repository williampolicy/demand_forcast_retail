import pandas as pd
import numpy as np

def handle_extreme_weather(special_dates_df, base_activity_level):
    # 获取极端天气日期
    extreme_weather_dates = special_dates_df[special_dates_df['type'] == 'extreme_weather']

    # 处理极端天气
    for _, row in extreme_weather_dates.iterrows():
        # 消费量前移
        base_activity_level[row['start_date'] - pd.Timedelta(days=2):row['start_date'] - pd.Timedelta(days=1)] *= 2
        # 极端天气期间消费量下降
        base_activity_level[row['start_date']:row['end_date']] *= 0.5
        # 恢复期消费量逐步恢复
        recovery_dates = pd.date_range(start=row['end_date'] + pd.Timedelta(days=1), periods=min(3, len(base_activity_level) - row['end_date'].dayofyear))
        for i, date in enumerate(recovery_dates):
            base_activity_level[date] *= (0.7 + 0.1 * (i + 1))
    
    return base_activity_level




# 读取特殊日期数据
special_dates_df = pd.read_csv('../special_dates.csv')
special_dates_df['start_date'] = pd.to_datetime(special_dates_df['start_date'])
special_dates_df['end_date'] = pd.to_datetime(special_dates_df['end_date'])

# 创建基础活动级别
dates = pd.date_range(start='2022-01-01', periods=365)
base_activity_level = pd.Series(np.random.uniform(low=0.2, high=0.2, size=365), index=dates)

# 处理极端天气
base_activity_level = handle_extreme_weather(special_dates_df, base_activity_level)

# 打印结果
print(base_activity_level)



import matplotlib.pyplot as plt

# 使用上面的代码处理极端天气
# ...

# 创建一个新的figure和axes
fig, ax = plt.subplots()

# 绘制活动级别
ax.plot(base_activity_level.index, base_activity_level.values, label='Activity Level')

# 添加标题和标签
ax.set_title('Activity Level Over Time')
ax.set_xlabel('Date')
ax.set_ylabel('Activity Level')

# 显示图例
ax.legend()
plt.show()




