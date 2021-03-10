def def_age(text, error_num):
    quest = input(text)
    while not quest.isnumeric():
        print(error_num)
        quest = input(text)
    return int(quest)

def find_by_name(data, name):
    for elem in data:
        if elem["name"] == name:
            return elem
        #elif elem["name"] != name:
           # print("Error")
           # true_elem = elem["name"] == name
            #try_again = input("Try again:")
           # if  try_again == true_elem:
                #return true_elem # !!!!!!!!!!!!!!!!
            #else:
                #return try_again
    return None