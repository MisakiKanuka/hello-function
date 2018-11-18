def hello():
    print("Hello World")


hello()


def say_hello(name):
    print(f"Hi {name}!")


say_hello("Bob")
say_hello("Nana")


def double(number):
    return 2 * number


result_1 = double(3)

print(result_1)


# 1分課題
# str_conbine("Kazuma", "Takahashi") #Kazuma Takahashi を返す

def str_conbine(str1, str2):
    return str1 + str2


result = str_conbine("Kazuma", "Takahashi")
