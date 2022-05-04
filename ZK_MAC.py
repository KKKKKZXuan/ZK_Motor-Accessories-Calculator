import re
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
taoguan_string_list_split_org = taoguan_string_list.str.split(pat="+")
# 删除所有的空行
taoguan_string_list_split = [x for x in taoguan_string_list_split_org if x == x]

# 测试split之后的输出
# print(taoguan_string_list_split)
# taoguan_string_list_split.to_excel(output_file_path)

taoguan_list = []
last_taoguan = None


# 进循环对string逐一判断
for i in range(len(taoguan_string_list_split)):

    taoguan_list.append([])

    # 判断每一行的string
    for j in range(len(taoguan_string_list_split[i])):

        # 第一种情况：
        # 如果出现简写（例如：123A + B + C）
        # 判断出后面的BC是简写，自动判断添加前面的前缀
        # 如果前面的也是简写，继续向前判断
        # 特殊情况：
        # 不能是每一行的第一个位置出现简写
        # 自动向前寻找的个数不超过该行的个数总和
        if j > 0 and len(taoguan_string_list_split[i][j]) <= 1:
            
            k = 1
            while k < len(taoguan_string_list_split[i]):
                # print("i: {}".format(i))
                # print("j: {}".format(j))
                # print("k: {}".format(k))
                if len(taoguan_string_list_split[i][j - k]) <= 1:
                    k += 1
                else:
                    last_taoguan = taoguan_string_list_split[i][j - k]
                    break

            taoguan_list[i].append(last_taoguan[:-1] + taoguan_string_list_split[i][j])

        # 检查重复的次数
        # 以数量换*n
        elif len(taoguan_string_list_split[i][j]) > 1 and taoguan_string_list_split[i][j][-2] == "*":
            tgs = str.split(taoguan_string_list_split[i][j], "*")
            for k in range(int(tgs[1])):
                taoguan_list[i].append(tgs[0])

        # 如果没有问题
        # 直接存到新的list中
        else:
            taoguan_list[i].append(taoguan_string_list_split[i][j])
        
taoguan_pd_output = pd.DataFrame(taoguan_list)
taoguan_pd_output.to_excel(output_file_path)

print("没问题")