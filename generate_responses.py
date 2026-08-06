from clients import cached_ask
import json

with open("data/questions_en.json","r") as f:
    r= json.load(f)

models=["gemini-3.6-flash","gemma-4-26b-a4b-it"]
answers=[]
for model in models:
     for question in r:
        answer = (cached_ask(model,question["text"]))
        print(question["id"])
        print(model)
        print(answer)
        entry = {"id": question["id"], "model": model, "answer": answer}
        answers.append(entry)
        with open("data/responses.json", "w") as f:
            json.dump(answers, f, indent=2)