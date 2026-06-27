from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma

from sentence_transformers import SentenceTransformer

from langchain.embeddings.base import Embeddings

from utils import split_documents


class MiniLMEmbeddings(Embeddings):

    def __init__(self):
        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    def embed_documents(self, texts):
        return self.model.encode(texts).tolist()

    def embed_query(self, text):
        return self.model.encode(text).tolist()


loader = TextLoader("data/raw/econet_help.txt")

docs = loader.load()

chunks = split_documents(docs)

embedding = MiniLMEmbeddings()

db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding,
    persist_directory="data/chroma"
)

print("Knowledge base created!")