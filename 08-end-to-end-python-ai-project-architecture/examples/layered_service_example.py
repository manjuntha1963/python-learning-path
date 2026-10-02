# Module 08 example: a layered service design
# This demonstrates a practical software architecture pattern


class Retriever:
    def retrieve(self, query):
        return ["document-1", "document-2"]


class Service:
    def __init__(self, retriever):
        self.retriever = retriever

    def answer(self, question):
        docs = self.retriever.retrieve(question)
        return {"question": question, "documents": docs}


service = Service(Retriever())
print(service.answer("What is Python?"))
