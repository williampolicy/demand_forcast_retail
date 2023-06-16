
import pandas as pd
import kanglib


def calculate_weighted_value(df: pd.DataFrame, columns: list, weights_column: str, result_column: str) -> pd.DataFrame:
    # 计算加权值
    df[result_column] = df[columns].prod(axis=1) * df[weights_column]
    return df



def calculate_weighted_value1(df: pd.DataFrame, columns: list, weights_column: str, result_column: str) -> pd.Series:
    # 计算加权乘积
    df[result_column] = df[columns].prod(axis=1) * df[weights_column]
    
    # 只返回计算结果
    return df[result_column]


def calculate_weighted_value2(df: pd.DataFrame, columns: list, weights_column: str, result_column: str) -> pd.Series:
	# 计算加权乘积
	df[result_column] = df[columns].prod(axis=1) * df[weights_column]

	# 只返回计算结果
	return df[[result_column]]


# 创建一个DataFrame以供测试
df = pd.DataFrame({
    'column1': [1, 2, 3],
    'column2': [4, 5, 6],
    'weights': [0.5, 0.6, 0.7]
})

# 使用calculate_weighted_value函数
df = calculate_weighted_value2(df, ['column2'], 'weights', 'result')
print(df)

