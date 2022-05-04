import pandas as pd

input_file_path = "./data/电机辅料.xlsx"
output_file_path = "./output/test.xlsx"


# 把Excel文件中的数据读入pandas
df = pd.read_excel(input_file_path)

# print(df)

# # 读取excel的某一个sheet
# df = pd.read_excel(file_path, sheet_name='Sheet1')

# # 获取列标题
# print(df.columns)

# # 获取列行标题
# print(df.index)

# # 制定打印某一列
# print(df["工资水平"])

# # 描述数据
# print(df.describe())

# 获取所有套管的数据
taoguan_string_list = df["套管"]

# 使用+来split套管的值
taoguan_string_list_split = taoguan_string_list.str.split(pat="+")

# 测试split之后的输出
# print(taoguan_string_list_split)
# taoguan_string_list_split.to_excel(output_file_path)

print("没问题")