from retrieval.search import DocumentSearcher
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch


class RAGPipeline:
    def __init__(self):
        self.searcher = DocumentSearcher()

        model_name = "google/flan-t5-base"

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def generate_answer(self, question):
        retrieved_chunks = self.searcher.search(question, top_k=3)

        context = "\n\n".join(retrieved_chunks)

        prompt = f"""
        Answer the question based only on the context below.

        Context:
        {context}

        Question:
        {question}
        """

        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1024)

        outputs = self.model.generate(
            **inputs,
            max_length=300,
            num_beams=4,
            early_stopping=True
        )

        answer = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        return answer


if __name__ == "__main__":
    rag = RAGPipeline()

    question = input("Ask your question: ")

    answer = rag.generate_answer(question)

    print("\nGenerated Answer:\n")
    print(answer)
