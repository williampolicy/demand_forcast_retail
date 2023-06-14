import numpy as np
import pandas as pd

# 我们设定一个基准活动水平为1
base_activity_level = 1

# 定义家庭类型
family_types = ['A', 'B', 'C']

# 创建一个空的DataFrame，将包含日期和每种类型家庭的活动水平
activity_df = pd.DataFrame()

# 添加日期信息，我们假设从1月1日开始
activity_df['Day'] = range(1, 366)

# 对于每一种家庭类型
for family_type in family_types:
    # 我们使用numpy的random函数生成一个365长度的随机数组，数值在-0.2到0.2之间，模拟活动水平的日常波动
    activity_fluctuation = np.random.uniform(-0.2, 0.2, 365)
    # 计算出每一天的活动水平
    activity_level = base_activity_level + activity_fluctuation
    # 将活动水平添加到DataFrame中
    activity_df['Activity_Level_' + family_type] = activity_level

# 保存到CSV文件
activity_df.to_csv('activity_level.csv', index=False)

print(activity_df)


# import numpy as np
# import pandas as pd

# # 我们设定一个基准活动水平为1
# base_activity_level = 1

# # 我们使用numpy的random函数生成一个365长度的随机数组，数值在-0.2到0.2之间，模拟活动水平的日常波动
# activity_fluctuation = np.random.uniform(-0.2, 0.2, 365)

# # 计算出每一天的活动水平
# activity_level = base_activity_level + activity_fluctuation

# # 将活动水平存储到一个DataFrame中
# activity_df = pd.DataFrame(activity_level, columns=['Activity_Level'])

# # 添加日期信息，我们假设从1月1日开始
# activity_df['Day'] = range(1, 366)

# # 保存到CSV文件
# activity_df.to_csv('activity_level.csv', index=False)

# print(activity_df)
