from sentence_transformers import SentenceTransformer

# 加载预训练的Sentence Transformer模型
model = SentenceTransformer('D:/ai/all-MiniLM-L6-v2')

def get_sentence_transformer_embedding(text):
    embedding = model.encode(text)
    return embedding

# 示例文本
text = "OpenAI is creating advanced artificial intelligence."

# 获取嵌入向量
embedding = get_sentence_transformer_embedding(text)
print(embedding)
