import pickle
from auxiliary import def_age , find_by_name

def add_employee(data):
    name = input("Enter name:\n")
    age = def_age("Enter age:", error_num="Age must = num")
    new_emp = {"name": name, "age": age}
    data.append(new_emp)
    return data


def del_employee(data):
    print("Del Employee :(")
    name = input("Enter name:\n")
    employee = find_by_name(data, name)
    data.remove(employee)
    return data


def edit_employee(data):
    name = input("Enter name:\n")
    employee = find_by_name(data, name)
    new_name = input("Enter new name:\n")
    new_age = def_age("Enter new age:", error_num="Age must = num")
    employee["name"] = new_name
    employee["age"] = new_age
    return data


def search_employee(data):
    choice = input("search by:\n1-full name\n2-start witn\n3-age\n")
    founded = []
    if choice == "1":
        name = input("Enter name for search:\n")
        employee = find_by_name(data, name)
    elif choice == "2":
        start = input("Stars with :\n")
        for elem in data:
            if elem["name"].startswith(start):
                founded.append(elem)
    elif choice == "3":
        age = def_age("Enter new age:", error_num="Age must = num")
        for elem in data:
            if elem["age"] == age :
                founded.append(elem)
    print_employee(founded)
    return


def print_employee(data):
    for elem in data:
        print(f'|{elem["name"]}||{elem["age"]}|')
    return data

def main():
    with open("data.picle", "rb") as read_f:
        data =  pickle.load(read_f)

data = [{"name": "Allen", "age": 35},
        {"name": "qwe", "age": 21}]

while True:
    print('-'* 26)
    choice = input("|1|Add employee\n|2|Del employee\n|3|Edit employee\n|4|Search for an employee\n|5|Print list of employees\n|0|Exit and Save" '\n--------------------------\n'"ENTER --> ")
    if choice == "1":
        data = add_employee(data)
    elif choice == "2":
        data = del_employee(data)
    elif choice == "3":
        data = edit_employee(data)
    elif choice == "4":
        data = search_employee(data)
    elif choice == "5":
        data = print_employee(data)
    elif choice == "6":
        with open("data.picle" , "wb" ) as save_f:
            pickle.dump(data , save_f)
    elif choice == "0":
        print("Exit")
        with open("data.picle" , "wb" ) as save_f:
            pickle.dump(data , save_f)
        break
    else:
        print("Error, try again:\n")

    # data = [{"name": "Allen", "age": 35},
    #         {"name": "Edward", "age": 21}]
main()