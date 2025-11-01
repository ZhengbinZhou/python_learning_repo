# 对任何文件进行读写，通常都遵循四个核心步骤：
# 打开文件、读取或写入数据、关闭文件。
# 在Python中，使用 with语句可以优雅地管理文件资源，确保文件在使用后自动关闭，避免资源泄露

"""
读入csv文件

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
"""

######如果使用内含的csv库

#read all the data
import csv  # 导入内置csv模块

# 1. 打开文件（with语句自动关闭，encoding指定UTF-8避免中文乱码）
with open("student.csv", mode="r", encoding="UTF-8") as file:
    # 2. 创建读取对象（csv.reader按行读取，返回列表；csv.DictReader按字典读取，键为表头）
    # 方式A：用csv.reader（返回列表，需手动对应表头）
    reader = csv.reader(file)
    header = next(reader)  # 读取第一行（表头）
    print("表头：", header)  # 输出：表头： ['姓名', '年龄', '性别', '成绩']
    # 读取剩余数据
    for row in reader:
        print("行数据：", row)  # 输出：行数据： ['张三', '18', '男', '95'] 等

    # 方式B：用csv.DictReader（返回字典，键为表头，更直观）
    # reader = csv.DictReader(file)
    # for row in reader:
    #     print("姓名：", row["姓名"], "成绩：", row["成绩"])  # 输出：姓名： 张三 成绩： 95


#  write into csv data

import csv

# 1. 打开文件（mode="w"写入，newline=""避免空行，encoding="UTF-8"支持中文）
with open("new_student.csv", mode="w", newline="", encoding="UTF-8") as file:
    # 2. 定义表头和数据
    header = ["姓名", "年龄", "性别", "成绩"]
    data = [
        ["赵六", 20, "男", 85],
        ["孙七", 19, "女", 90],
        ["周八", 18, "男", 78]
    ]
    # 3. 创建写入对象，指定表头
    writer = csv.DictWriter(file, fieldnames=header)
    # 4. 写入表头和数据
    writer.writeheader()  # 写入表头
    writer.writerows(data)  # 批量写入数据（也可用writerow()单行写入）

print("CSV文件写入完成！")


# close csv
'''
若用 with 语句，文件会在代码块结束后自动关闭，无需手动调用 file.close()；
若未用 with，需在操作结束后手动关闭：file.close()。
'''

#####如果使用pandas库（推荐）
import pandas as pd

#read:

import pandas as pd

# 1. 打开+读取（read_csv()自动打开并读取，返回DataFrame（表格型数据结构））
df = pd.read_csv(
    "student.csv",  # 文件路径
    encoding="UTF-8",  # 编码
    dtype={"年龄": int, "成绩": int}  # 指定数据类型（避免年龄读成字符串）
)

# 2. 查看读取结果
print("数据预览：")
print(df.head(2))  # 查看前2行
print("数据形状：", df.shape)  # 输出：(3,4) 表示3行4列


#write into file
import pandas as pd

# 1. 准备数据（用字典创建DataFrame，键为表头，值为列数据）
data = {
    "姓名": ["赵六", "孙七", "周八"],
    "年龄": [20, 19, 18],
    "性别": ["男", "女", "男"],
    "成绩": [85, 90, 78]
}
df = pd.DataFrame(data)

# 2. 写入CSV（to_csv()自动打开+写入+关闭，index=False不保存行索引）
df.to_csv(
    "new_student_pd.csv",
    encoding="UTF-8",
    index=False  # 关键！避免生成多余的行号列
)

print("CSV文件写入完成！")