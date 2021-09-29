from time import sleep


def demo_input_output():
    name = input("Enter name: ")
    print(f"Hello, {name}")


def demo_variables():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    if x < y:
        print("x is less than y")
    elif x > y:
        print("x is greater than y")
    else:
        print("x and y are equal")


def demo_while():
    i = 3
    while i > 0:
        print("Hello, World")
        i -= 1


def demo_for():
    for i in range(2, 10, 2):
        print(i, end=" ")


def main():
    for i in range(3):
        say_hello()


def say_hello():
    print("Well hello there" * 10)


def test_size_of_int():
    start = 10
    while True:
        sleep(1)
        start *= 10
        print(start)


def test_lists():
    scores = []
    scores.append(72)
    scores.append(73)
    scores.append(33)

    print(f"Average: {sum(scores)/len(scores)}")


def case_converter():
    name = input("Enter your name: ")
    for c in name:
        print(c.capitalize(), end="")


case_converter()
#main()

#say_hello()
#test_size_of_int()
#test_lists()




# demo_input_output()
# demo_variables()
#demo_while()
#demo_for()