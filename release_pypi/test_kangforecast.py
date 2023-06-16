import kangforecast

import pandas as pd
from pkg_resources import resource_filename

print('---------print file kangforecast.__file__:\n')
print(kangforecast.__file__)

# Use resource_filename to get the path to your data file
print('---------\n')

datafile = resource_filename('kangforecast', 'data/special_dates.csv')

# 如果上述的所有方法都无法解决问题，那可能需要更深入的研究来找到解决办法。


data = pd.read_csv(datafile)
print(data)




# import pandas as pd
# data = pd.read_csv('kangforecast/data/special_dates.csv')

# print(data)

# # Replace with the actual parameters
# # result = kangforecast.prepare_data(param1, param2, param3)  



