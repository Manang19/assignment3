def count_upper_lower(string):
    upper_count = 0
    lower_count = 0 
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    print("Upper Case Count is %d Lower Case is %d " % (upper_count,lower_count))

sentance = input("enter a sentance : ")
count_upper_lower(sentance)
