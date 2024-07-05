#from getEmbedding import get_embedding
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
           # embedding = get_embedding(sentence)
            embeddings.append(embedding)
            #print(f"Embedding for '{sentence}'")
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
search = get_sentence_transformer_embedding("我现在太后悔。我下岗10年，爷爷09年骑自行车洗澡去，那道上被人给撞着了，把股骨头摔坏了，摔坏之后，09年我要是出去打工去，我还能挣好多钱为我同事人家有干的人就请我那意思去需要我这个工种，因为爷爷摔坏了股骨头了，我就在家一直照顾爷爷没出去打工。")
search = np.array([search])
D, I = index.search(search, topK)
res=df['sentence'].iloc[I[0]]
print(res)
# save_embeddings = np.array(embeddings)
# np.save('embeddings.npy', save_embeddings)
