def lengthOfLastWord(s):
    s_list = s.split(" ")
    s_list = s_list[::-1]
    print(s_list)
    for a in s_list:
        print (a)
        if a != "":
            return (len(a))

s = "apple banana help"
print (lengthOfLastWord(s))
