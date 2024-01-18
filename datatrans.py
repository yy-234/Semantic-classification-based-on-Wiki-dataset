import pandas as pd
from sklearn.model_selection import train_test_split
data_xlsx=['THUCNews/data/data_xlsx/wiki_0_0.xlsx',
           'THUCNews/data/data_xlsx/wiki_0_1.xlsx',
           'THUCNews/data/data_xlsx/wiki_0_2.xlsx',
           'THUCNews/data/data_xlsx/wiki_0_3.xlsx',
           'THUCNews/data/data_xlsx/wiki_0_4.xlsx'
           ]
# 读取所有Excel文件
dataframes = []
for file in data_xlsx:
    df = pd.read_excel(file)
    dataframes.append(df)

# 合并所有数据
merged_df = pd.concat(dataframes)

# 划分训练集、测试集和验证集
train_df, test_val_df = train_test_split(merged_df, test_size=0.4, random_state=42)
test_df, val_df = train_test_split(test_val_df, test_size=0.5, random_state=42)

# 显示各个数据集的大小
print("Training set size:", len(train_df))
print("Test set size:", len(test_df))
print("Validation set size:", len(val_df))

