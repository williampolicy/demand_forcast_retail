import pandas as pd
import numpy as np

# 假设有四种产品
products = ['product1', 'product2', 'product3', 'product4']

# 创建一个日期范围，从2022年的第一天开始，持续365天
dates = pd.date_range(start='2022-01-01', periods=365)

# 对于每一种产品，生成一组随机的活动水平数据
activity_levels = {product: np.random.uniform(low=0.2, high=1.0, size=365) for product in products}

# 将数据转换为DataFrame
activity_levels_df = pd.DataFrame(activity_levels, index=dates)

print(activity_levels_df)
