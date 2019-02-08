from random import choice #get the random.choice function


questions = ["Why is the sky blue?","Where are the dinosaurs?","Why is there a face on the moon?"]

question = choice(questions)

answer = input(question + ": ").strip().lower()

while answer != "just because":
    answer = input("But why????: ").strip().lower()

print("That makes sense!")
print("test")
