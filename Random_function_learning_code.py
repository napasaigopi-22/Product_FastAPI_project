def printing_dogs_name(first_name, last_name):
    print_sentence= first_name + ":" + last_name
    return print_sentence
print(printing_dogs_name("My pet name is","Daschund"))


# with the help of FASTAPI
def printing_dogs_names(firstname: str, lastname: str):
    print_dogs_sentence = firstname.title() +":" + lastname.upper()
    return print_dogs_sentence

print(printing_dogs_names("My pet name is","Daschund"))


def list_str(list: list[str]):
    list = ["gopi", "sai", "napa", "nadh"]
    lst = "  "
    for i in list:
        lst = i +" "+ lst
    return lst
print(list_str(list))



items = str(input("Enter Your Name: "))
def python_code_with_union(items:str | None= None):
    if items is not None:
        return(f"Hey! { items}")
    else:
        return(f"Hey! you enter {items} a invalid name")

print(python_code_with_union(items))



#Using lambda function: a small ananymous function that can have any number of arguments but only having one expression. 
lambda_method = lambda x,y: x*y
print(lambda_method(3,4))

f = lambda: "Hello"
print(f())

l = [1,2,3,4]
mul = list(map(lambda x: x*2 , l))
print(mul)

l = [1,2,3,4]
mul = list(filter(lambda x: x%2==0 , l))
print(mul)

from functools import reduce
l = [1,2,3,4]
mul = reduce(lambda x,y: x*y , l)
print(mul)