from getEmbedding import get_embedding
from getSentEmbedding import get_sentence_transformer_embedding
from tenacity import retry, wait_random_exponential, stop_after_attempt, retry_if_not_exception_type
import numpy as np
import pandas as pd
import faiss
def get_sentences_embeddings(sentences):
    embeddings = []
    try:       
        for sentence in sentences:
            embedding = get_sentence_transformer_embedding(sentence)
            embeddings.append(embedding)
            print(f"Embedding for '{sentence}'")
    except Exception as e:
        print(f"An error occurred: {e}")   
    return embeddings

file_path = 'test.txt'
df = pd.read_csv(file_path, sep="#", header=None, names=["sentence"])
sentences = df['sentence'].tolist()
embeddings = get_sentences_embeddings(sentences)
sentence_embeddings=np.array(embeddings)
dimension = sentence_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(sentence_embeddings)
topK = 5
search = get_sentence_transformer_embedding("大姐一直16岁到了北京，到现在还在北京了")
search = np.array([search])
D, I = index.search(search, topK)
res=df['sentence'].iloc[I[0]]
print(res)
# save_embeddings = np.array(embeddings)
# np.save('embeddings.npy', save_embeddings)
