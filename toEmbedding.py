from openai import OpenAI
import os
import openai
from tenacity import retry, wait_random_exponential, stop_after_attempt, retry_if_not_exception_type

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "your-api-key-here"))

EMBEDDING_MODEL = 'text-embedding-3-small'
EMBEDDING_CTX_LENGTH = 8191
EMBEDDING_ENCODING = 'cl100k_base'

# let's make sure to not retry on an invalid request, because that is what we want to demonstrate
@retry(wait=wait_random_exponential(min=1, max=20), stop=stop_after_attempt(6), retry=retry_if_not_exception_type(openai.BadRequestError))
def get_embedding(text_or_tokens, model=EMBEDDING_MODEL):
    return client.embeddings.create(input=text_or_tokens, model=model).data[0].embedding
res=get_embedding("Hello, world!")
print(res)