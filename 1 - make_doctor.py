# returns user's name with doctor in front of it
def make_doctor(name):
    return "Doctor " + name + " here"

full_name = input("Please write your full name: ")
print(make_doctor(full_name))
