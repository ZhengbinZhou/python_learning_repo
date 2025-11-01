import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import os
import nltk

nltk.download('punkt_tab')

# 下载停用词和分词器数据
nltk.download('stopwords')
nltk.download('punkt')

# 获取桌面路径
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
# 假设你的 Parquet 文件名为 _上市公司专利-2000-2023.parquet
file_path = os.path.join(desktop_path, '_上市公司专利-2000-2023.parquet')

try:
    # 从 Parquet 文件读取数据
    df = pd.read_parquet(file_path)
    # 检查数据中是否包含必要的列
    required_columns = ['摘要文本', 'IPC分类号']
    for col in required_columns:
        if col not in df.columns:
            raise KeyError(f"数据中缺少必要的列 '{col}'，请检查数据文件。")
except FileNotFoundError:
    print(f"未找到文件: {file_path}，请检查文件路径和文件名。")
    exit(1)
except KeyError as e:
    print(e)
    exit(1)


# 数据预处理函数
def preprocess_text(text):
    # 转换为小写
    text = str(text).lower()
    # 去除标点符号
    text = text.translate(str.maketrans('', '', string.punctuation))
    # 分词
    tokens = word_tokenize(text)
    # 去除停用词
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    return " ".join(tokens)


# 对专利文本进行预处理
df['processed_text'] = df['摘要文本'].apply(preprocess_text)

# IPC分类统计
ipc_counts = df['IPC分类号'].value_counts()
print("IPC分类统计：")
print(ipc_counts)

# 假设数据中已经有 is_exploratory 列，如果没有，使用简单规则自动标注
if 'is_exploratory' not in df.columns:
    print("数据中缺少 'is_exploratory' 列，使用简单规则自动标注。")
    explore_keywords = ["explore", "discover", "novel", "new concept"]


    def auto_label(text):
        for keyword in explore_keywords:
            if keyword in text:
                return 1
        return 0


    df['is_exploratory'] = df['processed_text'].apply(auto_label)

# 特征提取
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['processed_text'])
y = df['is_exploratory']

# 训练分类模型
model = LogisticRegression()
try:
    model.fit(X, y)
except Exception as e:
    print(f"模型训练出错: {e}，请检查数据格式和内容。")
    exit(1)

# 预测新专利的类型
new_text = "This patent explores new materials for energy storage."
new_processed_text = preprocess_text(new_text)
new_X = vectorizer.transform([new_processed_text])
try:
    prediction = model.predict(new_X)
    if prediction[0] == 1:
        print("该专利是探索性专利")
    else:
        print("该专利是开发性专利")
except Exception as e:
    print(f"预测出错: {e}，请检查数据格式和内容。")
