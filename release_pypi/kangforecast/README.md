1. 该计算公式可以用以下的LaTeX数学表达式来表达：

   对于食物 $i$ 在某一日的总需求量，可以表示为：
   $$ D_i = \sum_{j}^{n} P_j \times N \times I_j \times C_{ji} $$

   其中：
   - $D_i$ 是食物 $i$ 的总需求量；
   - $P_j$ 是家庭类型 $j$ 的占比；
   - $N$ 是社区总家庭数；
   - $I_j$ 是家庭类型 $j$ 的可支配收入；
   - $C_{ji}$ 是家庭类型 $j$ 在该日对食物 $i$ 的消费概率；
   - $n$ 是家庭类型的数量。

2. 以下是一个Python程序来计算这个数值：

```python
import sqlite3
import pandas as pd

# 连接到SQLite数据库
conn = sqlite3.connect('festivals_food.db')

# 读取各表格
df_food = pd.read_sql_query("SELECT * from FestivalsFood", conn)
df_income = pd.read_sql_query("SELECT * from FamilyIncome", conn)
df_proportion = pd.read_sql_query("SELECT * from FamilyProportion", conn)

# 社区总家庭数
total_households = 100

# 不同日子
days = df_food['Festival'].unique()

# 不同食物
foods = df_food['Food'].unique()

# 需求计算
for day in days:
    for food in foods:
        demand = 0
        for i, row in df_proportion.iterrows():
            family_type = row['Family']
            proportion = row['Proportion']
            income = df_income.loc[df_income['Family'] == family_type, 'Income'].values[0]
            consumption_probability = df_food.loc[(df_food['Family'] == family_type) & (df_food['Festival'] == day) & (df_food['Food'] == food), 'Probability'].values[0]
            demand += proportion * total_households * income * consumption_probability
        print(f"The total demand for {food} on {day} is {demand}")

# 关闭连接
conn.close()
```

3. 该程序将输出不同日子中，每种食物的总需求量。

4. 输出报告可以采用一个Python的markdown库，如`markdown`库来生成，可以将计算结果格式化为markdown文本，然后写入到一个.md文件中。
