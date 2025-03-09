def classify_age(age):
    if age < 0:
        print("Invalid age!")
    elif age <= 12:
        print("Child")
    elif age <= 19:
        print("Teen")
    elif age <= 64:
        print("Adult")
    else:
        print("Senior")

while True:
    age = int(input("Enter age: "))
    classify_age(age)