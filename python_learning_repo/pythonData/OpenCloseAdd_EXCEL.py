# 对任何文件进行读写，通常都遵循四个核心步骤：
# 打开文件、读取或写入数据、关闭文件。
# 在Python中，使用 with语句可以优雅地管理文件资源，确保文件在使用后自动关闭，避免资源泄露

'''
读入excel文件

首先是逻辑：
1.打开文件。
2.读取、写入数据
3.关闭文件
无论是csv和excel都一样

关键补充：文件打开模式（通用）
打开文件时需指定模式，避免误操作（如用w模式打开已有文件会直接清空内容）。常用模式如下：
r：只读模式（默认），文件不存在则报错。
w：写入模式，文件不存在则创建，存在则清空原有内容（危险！需谨慎）。
a：追加模式，文件不存在则创建，存在则在末尾追加内容（不覆盖原有数据）。
r+：读写模式，可同时读和写，但需注意指针位置（避免覆盖数据）。
b：二进制模式（如处理 Excel 二进制文件时需加，如rb、wb）。
'''

######使用pandas库（推荐）

#read
import pandas as pd

# 1. 读取Excel文件（read_excel()，指定工作表）
# 方式A：读取单个工作表
df1 = pd.read_excel(
    "student.xlsx",
    sheet_name="Sheet1",  # 指定工作表名称（或索引0）
    encoding="UTF-8",
    dtype={"年龄": int, "成绩": int}
)

# 方式B：读取多个工作表（返回字典，键为工作表名，值为DataFrame）
df_dict = pd.read_excel("student.xlsx", sheet_name=["Sheet1", "Sheet2"])
df2 = df_dict["Sheet2"]  # 获取Sheet2的数据

# 查看结果
print("Sheet1数据：")
print(df1)



#write into files


import pandas as pd

# 1. 准备两个DataFrame
df1 = pd.DataFrame({
    "姓名": ["张三", "李四", "王五"],
    "年龄": [18, 19, 18],
    "性别": ["男", "女", "男"],
    "成绩": [95, 88, 92]
})

df2 = pd.DataFrame({
    "姓名": ["张三", "王五", "李四"],
    "成绩": [95, 92, 88],
    "排名": [1, 2, 3]
})

# 2. 写入Excel（用ExcelWriter管理多个工作表，index=False不保存行索引）
with pd.ExcelWriter("new_student_pd.xlsx", engine="openpyxl") as writer:
    df1.to_excel(writer, sheet_name="学生信息", index=False)  # 写入第一个工作表
    df2.to_excel(writer, sheet_name="成绩排名", index=False)  # 写入第二个工作表

print("Excel文件写入完成！")


'''
五、关键注意事项（避坑指南）
文件路径问题：
相对路径：文件与代码在同一文件夹（如 student.csv），推荐使用。
绝对路径：完整路径（如 C:\Users\Admin\Desktop\student.csv，Windows 需用\\转义，或加r前缀：r"C:\Users\Admin\Desktop\student.csv"）。
编码格式问题：
中文文件优先用 encoding="UTF-8"；若仍乱码，尝试 encoding="GBK"（Windows 默认编码）。
写入文件时统一用 UTF-8，避免跨平台乱码。
资源释放问题：
必须关闭文件！推荐用 with 语句（csv、pandas、openpyxl均支持），自动释放资源。
数据类型问题：
读取时可能出现 “数字读成字符串”（如 CSV 的年龄为"18"），需用 dtype 参数指定类型（如 dtype={"年龄": int}）。
Excel 版本问题：
.xlsx 用 openpyxl 处理；.xls 需用旧版 xlrd（pip install xlrd==1.2.0，新版不支持.xls）。
通过以上内容，可掌握 CSV 和 Excel 文件的完整操作流程，根据实际需求选择工具库（简单场景用原生库，复杂场景用pandas），避免常见问题。'''
