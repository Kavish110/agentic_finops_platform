from sqlalchemy import Index

Index(
    "ix_policy_embedding",
    PolicyDocument.embedding,
    postgresql_using="ivfflat",
    postgresql_with={"lists": 100},
    postgresql_ops={"embedding": "vector_cosine_ops"},
)