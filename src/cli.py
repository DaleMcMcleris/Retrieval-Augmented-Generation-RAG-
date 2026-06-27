from src.rag import ask

while True:

    question = input("\nAsk Econet > ")

    if question.lower() == "exit":
        break

    answer = ask(question)

    print("\nAnswer:\n")

    print(answer)