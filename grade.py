def grade(x: int) -> str:
    set_grade = "F"
    if (75 <= x <= 100):
        set_grade = "A"
    elif x >= 65:
        set_grade = "B"
    elif x >= 55:
        set_grade = "C"
    elif x >= 35:
        set_grade = "S"
    elif x < 35:
        return set_grade
    else:
        print("error")
    return set_grade


def start():
    subject = ["maths", "physics", "ICT", "english"]
    for i in subject:
        print(i)
        x = int(input("grade: "))
        print(grade(x))


start()
