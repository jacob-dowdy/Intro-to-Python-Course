# program that takes question and solution arguments for a quiz item.
def quiz_item(question,solution):
    while True:
        answer = input(question)
        if answer.lower() == solution.lower():
            print("That's correct!")
            return True

quiz_item("Who was the first avenger?: ", "Captain America")
