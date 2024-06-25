from openai import OpenAI
import os
import openai
from tenacity import retry, wait_random_exponential, stop_after_attempt, retry_if_not_exception_type
import numpy as np
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "your_api_key_here"))

EMBEDDING_MODEL = 'text-embedding-3-small'
EMBEDDING_CTX_LENGTH = 8191
EMBEDDING_ENCODING = 'cl100k_base'

# let's make sure to not retry on an invalid request, because that is what we want to demonstrate
@retry(wait=wait_random_exponential(min=1, max=20), stop=stop_after_attempt(6), retry=retry_if_not_exception_type(openai.BadRequestError))
def get_embedding(text_or_tokens, model=EMBEDDING_MODEL):
    return client.embeddings.create(input=text_or_tokens, model=model).data[0].embedding

def read_file_and_get_embeddings(file_path):
    embeddings = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()  # 去掉每行的首尾空格
                if line:  # 确保不处理空行
                    embedding = get_embedding(line)
                    embeddings.append(embedding)
                    print(f"Embedding for '{line}'")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return embeddings

file_path = 'test.txt'
embeddings = read_file_and_get_embeddings(file_path)
save_embeddings = np.array(embeddings)
np.save('embeddings.npy', save_embeddings)
