import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_activity_weighted_sensitivity(sensitivity: list, weights: pd.DataFrame, activity_levels: pd.DataFrame, products: list) -> pd.DataFrame:
    sensitivity_df = pd.DataFrame({
        'product': products,
        'sensitivity': sensitivity
    })
    
    activity_weighted_sensitivity_df = pd.concat([sensitivity_df]*len(weights))

    activity_weighted_sensitivity_df.reset_index(drop=True, inplace=True)

    activity_weighted_sensitivity_df['weight'] = weights.values.flatten()
    activity_weighted_sensitivity_df['activity_level'] = activity_levels.values.flatten()

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

activity_levels = pd.DataFrame({
    'product1': np.random.uniform(low=0.2, high=1.0, size=365),
    'product2': np.random.uniform(low=0.2, high=1.0, size=365),
    'product3': np.random.uniform(low=0.2, high=1.0, size=365),
    'product4': np.random.uniform(low=0.2, high=1.0, size=365)
}, index=pd.date_range(start='2022-01-01', periods=365))

df = calculate_activity_weighted_sensitivity(sensitivity, weights, activity_levels, products)


# 打印结果
print(df)


# 重新设置索引为日期和产品
activity_weighted_sensitivity_df=df.set_index(['date', 'product'], inplace=True)
# 打印结果
print('activity_weighted_sensitivity_df:')
print(activity_weighted_sensitivity_df)


# 将长格式的数据转换为宽格式
activity_weighted_sensitivity_wide = activity_weighted_sensitivity_df['activity_weighted_sensitivity'].unstack()

# 打印结果
print(activity_weighted_sensitivity_wide)



# 打印结果
print('activity_weighted_sensitivity_df:')
print(activity_weighted_sensitivity_df)




# 打印结果
print(df)

# 以产品为单位进行可视化
for product in products:
    product_df = df[df['product'] == product]
    plt.plot(product_df['activity_weighted_sensitivity'], label=product)

plt.legend()
plt.show()
