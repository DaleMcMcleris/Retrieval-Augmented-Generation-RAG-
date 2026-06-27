# from transformers import pipeline

# from sentence_transformers import SentenceTransformer

# from langchain.embeddings.base import Embeddings

# from langchain_community.vectorstores import Chroma


# class MiniLMEmbeddings(Embeddings):

#     def __init__(self):
#         self.model = SentenceTransformer(
#             "sentence-transformers/all-MiniLM-L6-v2"
#         )

#     def embed_documents(self, texts):
#         return self.model.encode(texts).tolist()

#     def embed_query(self, text):
#         return self.model.encode(text).tolist()


# embedding = MiniLMEmbeddings()

# db = Chroma(
#     persist_directory="data/chroma",
#     embedding_function=embedding
# )

# generator = pipeline(
#     "text2text-generation",
#     model="google/flan-t5-small"
# )


# def ask(question):

#     docs = db.similarity_search(question, k=3)

#     context = "\n".join(
#         [doc.page_content for doc in docs]
#     )

#     prompt = f"""
# Answer the customer's question using only the information below.

# Context:

# {context}

# Question:

# {question}

# Answer:
# """

#     result = generator(
#         prompt,
#         max_new_tokens=80
#     )

#     return result[0]["generated_text"]


from transformers import pipeline
from sentence_transformers import SentenceTransformer
from langchain.embeddings.base import Embeddings
from langchain_community.vectorstores import Chroma


class MiniLMEmbeddings(Embeddings):

    def __init__(self):
        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    def embed_documents(self, texts):
        return self.model.encode(texts).tolist()

    def embed_query(self, text):
        return self.model.encode(text).tolist()


embedding = MiniLMEmbeddings()

db = Chroma(
    persist_directory="data/chroma",
    embedding_function=embedding
)

# ✅ FIXED PIPELINE (correct for your installed transformers version)
generator = pipeline(
    "text-generation",
    model="google/flan-t5-small"
)


def ask(question):

    docs = db.similarity_search(question, k=3)

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
Answer the question using ONLY the context below.

If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{question}

Answer:
"""

    result = generator(
        prompt,
        max_new_tokens=80,
        do_sample=False
    )

    return result[0]["generated_text"]