import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 设置随机种子以获得可复现的结果
np.random.seed(0)

# 为每种商品创建一个空的DataFrame
df_dict = {}

# 商品名列表
product_names = ['Milk', 'Cheese', 'Yogurt', 'Butter', 'Cream', 'Eggs', 'IceCream', 'CottageCheese', 'SourCream', 'WhippedCream']

# 初始化日期范围
dates = pd.date_range(start='1/1/2023', end='12/31/2023')

for name in product_names:
    # 初始化需求和供应数据
    demand_data = np.random.uniform(low=50, high=100, size=len(dates))
    supply_data = np.random.uniform(low=50, high=100, size=len(dates))


    # 初始化节日列表
    holidays = ['2023-02-14', '2023-07-04', '2023-11-25', '2023-12-25']

    # # 在节日期间增加需求
    # demand_data[pd.to_datetime(holidays) == dates] *= 1.3  # increase demand by 30% on holidays

    # 在节日期间增加需求
    demand_data[dates.isin(pd.to_datetime(holidays))] *= 3  # increase demand by 30% on holidays


    # 在节日期间增加供应
    supply_data[dates.isin(pd.to_datetime(holidays))] *= 2.5  # increase supply by 250% on holidays

    # 对于特定的节日，如感恩节和圣诞节，我们可以更大幅度地增加供应
    thanksgiving = '2023-11-25'
    christmas = '2023-12-25'
    supply_data[dates == pd.to_datetime(thanksgiving)] *= 4  # quadruple supply on Thanksgiving
    supply_data[dates == pd.to_datetime(christmas)] *= 4 # quintuple supply on Christmas

       

    # 在暴风雪期间提前释放需求
    blizzard_date = '2023-12-20'
    pre_blizzard_date = '2023-12-19'
     # 在暴风雪期间提前释放需求
    demand_data[dates == pd.to_datetime(blizzard_date)] *= 2  # double the demand on blizzard date
    demand_data[dates == pd.to_datetime(pre_blizzard_date)] /= 2  # halve the demand on pre-blizzard date

    # demand_data[pd.to_datetime(blizzard_date) == dates] *= 2  # double the demand on blizzard date
    # demand_data[pd.to_datetime(pre_blizzard_date) == dates] /= 2  # halve the demand on pre-blizzard date
        # inventory_data = supply_data - demand_data
        # Calculate inventory
    inventory_data = supply_data - demand_data

    # Make sure inventory is not less than zero
    inventory_data = np.where(inventory_data < 0, 0, inventory_data)


    # 将需求，供应，库存数据放入DataFrame
    df = pd.DataFrame({
        'Date': dates,
        'Demand': demand_data,
        'Supply': supply_data,
        'Inventory': inventory_data
    })

    # 将DataFrame存入字典，键为商品名
    df_dict[name] = df

# # 输出Milk的库存图表
# plt.figure(figsize=(14, 8))
# plt.plot(df_dict['Milk']['Date'], df_dict['Milk']['Inventory'])
# plt.title('Inventory of Milk over Time')
# plt.xlabel('Date')
# plt.ylabel('Inventory')
# plt.grid(True)
# plt.show()



import matplotlib.pyplot as plt

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Plot data
ax.plot(dates, demand_data, label='Demand')
ax.plot(dates, supply_data, label='Supply')
ax.plot(dates, inventory_data, label='Inventory')

# Set labels and title
ax.set(xlabel='Date', ylabel='Quantity',
       title='Demand, Supply and Inventory over time')

# Enable legend
ax.legend()

# Show plot
plt.show()

