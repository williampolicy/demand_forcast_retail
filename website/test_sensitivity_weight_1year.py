import pandas as pd

import numpy as np

def calculate_weighted_sensitivity(sensitivity: list, weights: pd.DataFrame, products: list) -> pd.DataFrame:
    sensitivity_df = pd.DataFrame({
        'product': products,
        'sensitivity': sensitivity
    })
    
    # 使用pd.concat将sensitivity_df复制每一天
    weighted_sensitivity_df = pd.concat([sensitivity_df]*len(weights))

    # 重设索引
    weighted_sensitivity_df.reset_index(drop=True, inplace=True)

    # 将weights的数据复制到新的列
    weighted_sensitivity_df['weight'] = weights.values.flatten()

    # 计算加权敏感度
    weighted_sensitivity_df['weighted_sensitivity'] = weighted_sensitivity_df['sensitivity'] * weighted_sensitivity_df['weight']

    return weighted_sensitivity_df




products = ['product1', 'product2', 'product3', 'product4']
sensitivity = [0.2, 0.3, 0.1, 0.8]

# 创建全年的权重数据
weights = pd.DataFrame({
    'product1': np.linspace(1, 1, 365),
    'product2': np.linspace(1, 1, 365),
    'product3': np.linspace(1, 1, 365),
    'product4': np.linspace(1, 1, 365)
})

df = calculate_weighted_sensitivity(sensitivity, weights, products)


import matplotlib.pyplot as plt

# 打印结果
print(df)

# 以产品为单位进行可视化
for product in products:
    product_df = df[df['product'] == product]
    plt.plot(product_df['weighted_sensitivity'], label=product)

plt.legend()
plt.show()

