from datetime import datetime


def age_calculator():
    day = datetime.now()
    currentdate = day.strftime('%d-%m-%Y')
    userdate = input("Please input a date in the dd/mm/yyy format: ")
    age = int(currentdate[6:])-int(userdate[6:])
    if int(currentdate[3:5]) < int(userdate[3:5]):
        age -= 1
        return age
        print(age)
    elif int(currentdate[3:5]) == int(userdate[3:5]) and int(currentdate[0:2]) < int(userdate[0:2]):
        age -= 1
        return age
        print(age)
    else:
        return age
        print(age)


print(age_calculator())
