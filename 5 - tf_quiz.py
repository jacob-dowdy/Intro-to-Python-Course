# true/false quiz

def tf_quiz(question, correct_ans):
    user_input = input("(T/F) " + question + ": ")
    if user_input.lower() == correct_ans.lower():
        return("correct")
    else:
        return("incorrect")
        
# quiz key for question and correct answer
quiz_eval = tf_quiz("Guitars have 6 strings","T")    
print("your answer is",quiz_eval)
