# Module 11 example: protocol-based design
# This shows a flexible interface pattern without inheritance

from typing import Protocol


class RetrieverProtocol(Protocol):
    def retrieve(self, query: str) -> list[str]:
        ...


class SimpleRetriever:
    def retrieve(self, query: str) -> list[str]:
        return ["doc-1", "doc-2"]


class Service:
    def __init__(self, retriever: RetrieverProtocol):
        self.retriever = retriever

    def run(self, query: str):
        return self.retriever.retrieve(query)


print(Service(SimpleRetriever()).run("python"))
