# The match statement is introduced in Python 3.10 as a pattern matching feature. It works like switch-case in other languages but more powerful.

# # 1 creating matches
# value = 2

# match value:
#     case 1:
#         print("One")
#     case 2:
#         print("Two")
#     case 3:
#         print("Three")
#     case _:
#         print("Default case")  # Like 'else'

# # 2🔹 With Strings

# command = "start"

# match command:
#     case "start":
#         print("Engine started")
#     case "stop":
#         print("Engine stopped")
#     case _:
#         print("Unknown command")


# # 3🔹 Matching Multiple Values
# fruit = "mango"

# match fruit:
#     case "apple" | "mango":
#         print("It's a tropical fruit")
#     case "banana":
#         print("It's a banana")
#     case _:
#         print("Unknown fruit")

# 🔹 Matching with Conditions (if guards)
# age = 18

# match age:
#     case age if age < 18:
#         print("Minor")
#     case age if age >= 18 and age < 60:
#         print("Adult")
#     case _:
#         print("Senior")


#🔹 Matching Tuples

point = (0, 1)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y-axis at y = {y}")
    case (x, 0):
        print(f"X-axis at x = {x}")
    case (x, y):
        print(f"Point at x = {x}, y = {y}")















