from typing import Protocol


class Retriever(Protocol):
    def retrieve(self, query: str) -> list[str]: ...


class Service:
    def __init__(self, retriever: Retriever):
        self.retriever = retriever

    def run(self, query: str) -> list[str]:
        return self.retriever.retrieve(query)
