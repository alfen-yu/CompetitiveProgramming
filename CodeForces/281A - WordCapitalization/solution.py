# manually give the input 

s = input()

def capitalize_first_word(s):
    lst = []
 
    for i in s:
        lst.append(i)
 
    if lst[0].isupper():
        print("".join(lst))
    else:
        lst[0] = chr(ord(lst[0]) - 32)
        print("".join(lst))
 
capitalize_first_word(s)