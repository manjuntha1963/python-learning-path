class AnswerService:
    def __init__(self, retriever):
        self.retriever = retriever

    def answer(self, question: str) -> dict:
        return {"question": question, "sources": self.retriever(question)}


service = AnswerService(lambda question: ["local-document-1"])
print(service.answer("What is Python?"))
