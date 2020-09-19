def encode(message):
    result = ""
    pre_char = message[0]
    character = ""
    count = 0
    i = 0

    while (i != len(message)):
        character = message[i]

        if (pre_char == character):
            count += 1
        else:
            result += str(count) + pre_char
            count = 1

        pre_char = character
        i = i + 1

    return result + str(count) + pre_char


    #Remove pass and write your logic here

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)