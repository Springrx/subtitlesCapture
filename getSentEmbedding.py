import os
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
from sentence_transformers import SentenceTransformer

# 加载预训练的Sentence Transformer模型
#model = SentenceTransformer('/home/kc/all-MiniLM-L6-v2')
model = SentenceTransformer('lier007/xiaobu-embedding-v2')
def get_sentence_transformer_embedding(text):
    embedding = model.encode(text, normalize_embeddings=True)
    return embedding

# 示例文本
#text = "OpenAI is creating advanced artificial intelligence."

# 获取嵌入向量
#embedding = get_sentence_transformer_embedding(text)
#print(embedding)
