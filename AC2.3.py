# TASK 2 REFACTOR YOUR CODE 
# TASK 4 REQUIRES A MINOR CHANGE SUCH AS ADDING A COMMENT OR PRINT STATEMENT TO YOUR CODE.
# aAdding example code. 

n = input("Mani")
print("Welcome", n)
user_name = input("Enter your name: ")
print("Welcome, " + user_name + "!")

name =  input("Enter your name: ")
print("Welcome, " + name + "!")
name = input("Enter your name: ")
print("Welcome", name)
def welcome_user():
    name = input("Enter your name: ")
    print("Welcome", name)
welcome_user()
welcome_user()
age = int(input("Enter your age: "))
if age >= 18:
    can_vote = True
else:
    can_vote = False
can_vote = age >= 18
print("You can vote:", can_vote)


