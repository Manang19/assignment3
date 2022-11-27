def reverse (string):
    reversed_string = " "
    for i in string:
        reversed_string = i+reversed_string
    print("revesed string is:", reversed_string)
string = input(" enter the sentance:")
reverse (string)