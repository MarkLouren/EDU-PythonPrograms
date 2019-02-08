# * packing numbers n=[1,2,3,5] *n= 1,2,3,5
# packing is useful when you don't know how many arguments will be in a function
def add (*numbers):
    total=0
    for number in numbers:
        total=total+number
    print(total)
    return (total)
add(1,2,3,4,5,6,7)
# other example with packing * for arguments (1,2,3) ** for keys arguments ("name":"bob", "age":23)

def about (name, age, likes):
    sentence= "Meet {}! They are {} years old and they are like {}".format(name,age,likes)
    print(sentence)
    return sentence

dictionary = {"name": "Bob", "age":23, "likes":"Python"}
about (**dictionary)

#popular usage * => def foo(*args)  ** => def foo (**kwargs) [dictionaries] Сan add as many arguments as you wish
def foo(**kwargs):
    for key, value in kwargs.items():
        print ("{}:{}".format(key,value))

foo(name="me", age=15, loves="Python", drinks="Martiny")

# result:
# name:me
# age:15
# loves:Python
# drinks:Martiny
