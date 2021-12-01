def greetings_func(name):
    print('welcome ' + name)


greetings_func('John')


def greetings_func(name, age):
    print(f'welcome {name} You are {str(age)} years old')


greetings_func('John', 27)

def salary(Name,Basic_Salary,sales):

    if sales>=1000000:
        commission=sales*0.2
    salary=Basic_Salary+commission
    print(f"{Name}'s salary:{salary}")
salary("Hitherto", 4000000,10000000)
