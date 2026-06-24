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
    while(list):
        for i in list:
            return list
print(list_str(list))