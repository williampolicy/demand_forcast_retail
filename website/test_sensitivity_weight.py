

import pandas as pd
import numpy as np

def calculate_weighted_sensitivity(sensitivity: list, weight: list, products: list) -> pd.DataFrame:
    # 创建敏感度/偏好度的DataFrame
    sensitivity_df = pd.DataFrame({
        'product': products,
        'sensitivity': sensitivity
    })

    # 创建权重的DataFrame
    weight_df = pd.DataFrame({
        'product': products,
        'weight': weight
    })

    # 将两个DataFrame合并，基于产品列
    merged_df = pd.merge(sensitivity_df, weight_df, on='product')

    # 添加一个新的列来存储权重和敏感度的乘积
    merged_df['weighted_sensitivity'] = merged_df['sensitivity'] * merged_df['weight']

    return merged_df



products = ['product1', 'product2', 'product3', 'product4']
sensitivity = [0.2, 0.2, 0, 0.8]
weight = [1, 1, 1, 1.2]

df = calculate_weighted_sensitivity(sensitivity, weight, products)
print(df)


import matplotlib.pyplot as plt

# 打印结果
print(df)

# 以产品为单位进行可视化
for product in products:
    product_df = df[df['product'] == product]
    plt.plot(product_df['weighted_sensitivity'], label=product)

plt.legend()
plt.show()


