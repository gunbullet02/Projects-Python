def reverse(str):
    if len(str) == 0:
        return str
    else:
        return reverse(str[1:])+str[0]

mystr = "jo"
print(reverse(mystr))