# import pandas as pd
# import numpy as np

# # 创建一个空的 DataFrame
# df = pd.DataFrame(columns=['ProductID', 'ProductName', 'Profit', 'InventoryLevel', 'SupplyChainFlexibility'])

# # 用于产品名称的列表
# product_names = ['Milk', 'Cheese', 'Yogurt', 'Butter', 'Cream', 'Eggs', 'IceCream', 'CottageCheese', 'SourCream', 'WhippedCream', 'LactoseFreeMilk', 'OrganicMilk', 'HalfAndHalf', 'Brie', 'Cheddar', 'Mozzarella', 'Parmesan', 'Swiss', 'Blue', 'Feta']

# # 填充 DataFrame
# for i in range(20):
#     df.loc[i] = [i, # ProductID
#                  product_names[i], # ProductName
#                  np.random.uniform(1, 10), # Profit
#                  np.random.randint(10, 100), # InventoryLevel
#                  np.random.randint(1, 6)] # SupplyChainFlexibility

# # 打印 DataFrame
# print(df)


# 导入所需的库
import pandas as pd
import numpy as np

# 创建一个空的 DataFrame
df = pd.DataFrame(columns=['ProductID', 'ProductName', 'Profit', 'InventoryLevel', 'SupplyChainFlexibility'])

# 用于产品名称的列表
product_names = ['Milk', 'Cheese', 'Yogurt', 'Butter', 'Cream', 'Eggs', 'IceCream', 'CottageCheese', 'SourCream', 'WhippedCream', 'LactoseFreeMilk', 'OrganicMilk', 'HalfAndHalf', 'Brie', 'Cheddar', 'Mozzarella', 'Parmesan', 'Swiss', 'Blue', 'Feta']

# 填充 DataFrame
for i in range(20):
    df.loc[i] = [i, # ProductID
                 product_names[i], # ProductName
                 np.random.uniform(1, 10), # Profit
                 np.random.randint(10, 100), # InventoryLevel
                 np.random.randint(1, 6)] # SupplyChainFlexibility

# 保存为 CSV 文件
df.to_csv('product_data.csv', index=False)
print(df)


# 打印统计信息
print(df[['Profit', 'InventoryLevel', 'SupplyChainFlexibility']].describe())
