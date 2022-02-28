import os
import pandas as pd

# 合并csv文件
Folder_Path = r'C:\Users\admin\Desktop\全国空气\PM2.5-cy'  # 要拼接的文件夹及其完整路径，注意不要包含中文
SaveFile_Path = r'C:\Users\admin\Desktop\全国空气\PM2.5-cy'  # 拼接后要保存的文件路径
SaveFile_Name = r'all.csv'  # 合并后要保存的文件名

# 修改当前工作目录
os.chdir(Folder_Path)
# 将该文件夹下的所有文件名存入一个列表
file_list = os.listdir()

file = open(Folder_Path + '\\' + file_list[0], 'r', encoding="utf_8_sig")
# 读取第一个CSV文件并包含表头
df = pd.read_csv(file)  # 编码默认UTF-8，若乱码自行更改

# 将读取的第一个CSV文件写入合并后的文件保存
df.to_csv(SaveFile_Path + '\\' + SaveFile_Name, encoding="utf_8_sig", index=False)

# 循环遍历列表中各个CSV文件名，并追加到合并后的文件
for i in range(1, len(file_list)):
    rfile = open(Folder_Path + '\\' + file_list[i], 'r', encoding="utf_8_sig")
    df = pd.read_csv(rfile)
    df.to_csv(SaveFile_Path + '\\' + SaveFile_Name, encoding="utf_8_sig", index=False, header=False, mode='a+')
