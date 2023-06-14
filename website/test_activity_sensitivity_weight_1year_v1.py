import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_activity_weighted_sensitivity(sensitivity: list, weights: pd.DataFrame, activity_levels: pd.DataFrame, products: list) -> pd.DataFrame:
    # 创建一个日期范围
    dates = pd.date_range(start='2022-01-01', periods=365)

    # 复制sensitivity和产品名称到新的DataFrame中
    activity_weighted_sensitivity_df = pd.DataFrame({
        'date': np.repeat(dates, len(products)),
        'product': products * len(dates),
        'sensitivity': sensitivity * len(dates)
    })

    # 为新的DataFrame添加权重和活动水平
    activity_weighted_sensitivity_df['weight'] = weights.values.flatten()
    activity_weighted_sensitivity_df['activity_level'] = activity_levels.values.flatten()

    # 计算活动加权敏感度
    activity_weighted_sensitivity_df['activity_weighted_sensitivity'] = activity_weighted_sensitivity_df['sensitivity'] * activity_weighted_sensitivity_df['weight'] * activity_weighted_sensitivity_df['activity_level']

    return activity_weighted_sensitivity_df

products = ['product1', 'product2', 'product3', 'product4']
sensitivity = [0.2, 0.3, 0.1, 0.8]

weights = pd.DataFrame({
    'product1': np.linspace(1, 1, 365),
    'product2': np.linspace(1, 1, 365),
    'product3': np.linspace(1, 1, 365),
    'product4': np.linspace(1, 1, 365)
}, index=pd.date_range(start='2022-01-01', periods=365))

print(f'weights:\n',weights)

activity_levels = pd.DataFrame({
    'product1': np.random.uniform(low=0.2, high=1.0, size=365),
    'product2': np.random.uniform(low=0.2, high=1.0, size=365),
    'product3': np.random.uniform(low=0.2, high=1.0, size=365),
    'product4': np.random.uniform(low=0.2, high=1.0, size=365)
}, index=pd.date_range(start='2022-01-01', periods=365))


print(f'activity_levels:\n',activity_levels)

df = calculate_activity_weighted_sensitivity(sensitivity, weights, activity_levels, products)



print('df = calculate_activity_weighted_sensitivity(sensitivity, weights, activity_levels, products):\n')
print(df)



# 重新设置索引为日期和产品
activity_weighted_sensitivity_df = df.copy()
activity_weighted_sensitivity_df.set_index(['date', 'product'], inplace=True)

# 打印结果
print('activity_weighted_sensitivity_df:')
print(activity_weighted_sensitivity_df)



# 将长格式的数据转换为宽格式
activity_weighted_sensitivity_wide = activity_weighted_sensitivity_df['activity_weighted_sensitivity'].unstack()

# 打印结果
print('activity_weighted_sensitivity_wide')
print(activity_weighted_sensitivity_wide)



# 以产品为单位进行可视化
for product in products:
    product_df = df[df['product'] == product]
    plt.plot(product_df['activity_weighted_sensitivity'], label=product)

plt.legend()
plt.show()
