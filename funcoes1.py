from tkinter.filedialog import test


def line(n):
    for i in range(n):
        print("_", end=" ")
        i = i + 1
    print(" ")


test = int(input("Insert an interger: "))
x = 0
while x <= test:
    line(x)
    x += 1
print(" ")
