the_string = input("String: ")
the_sub_string = input("Substring: ")

if the_sub_string in the_string :
    print("the string contains the substring")

    how_many = the_string.count(the_sub_string)
    print("It contains", how_many, "instance(s)")

    where = the_string.find(the_sub_string)
    print("The first occurrence starts at position", where)

    if the_string.startswith(the_sub_string) :
        print("The string starts with the substring")
    else :
        print("The string doesn't start with the substring")
    
    if the_string.endswith(the_sub_string) :
        print("The string ends with the substring")
    else :
        print("The string doesn't end with the substring")

else :
    print("the string doesn't contain the substring")