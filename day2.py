# for i in range (1,10):
#     print(i)


# i=1
# while i<10:
#     print(i)
#     i+=1

    # def company(name):
#     print('welcome to',name)
# def greet(name):
#     print('hello',name)
#     company('TCS')

# greet('Dhanush')

students = []

permission = input('do you want to add student? (yes/no): ')
while permission.lower() == 'yes' or permission.lower() == 'y':
    name = input('enter student name: ')
    age = int(input('enter student age: '))
    students.append({'name': name, 'age': age})
    print(students)
    permission = input('do you want to add another student? (yes/no): ')