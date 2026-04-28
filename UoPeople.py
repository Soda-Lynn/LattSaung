def creat_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = creat_name("john", "doe")
print(full_name)