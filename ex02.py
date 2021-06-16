def trip(string):
    # for i in range(len(string)):
    #     if string[0] == " ":
    #         string = string[1:]
    #     else:
    #         break
    # for i in range(len(string)):
    #     if string[-1] == " ":
    #         string = string[:-1]
    #     else:
    #         break
    # return string
    # while string[0] == " ":
    #     string = string[1:]
    # while string[-1] == " ":
    #     string = string[:-1]
    # return string
    string = string.strip()
    return string


a = " s df   "
print(trip(a))

# 8：15-8：17
# 8：31-8：33
# 8：50-8：52
