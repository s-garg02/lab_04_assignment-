class Employee:
    def __init__(self, id, name, age, salary):
        self.Id = id
        self.Name = name
        self.Age = age
        self.Salary = salary

# Create Employee objects
e1 = Employee("161E90", "Raman", 41, 56000)
e2 = Employee("161F91", "Himadri", 38, 67500)
e3 = Employee("161F99", "Jaya", 51, 82100)
e4 = Employee("171E20", "Tejas", 30, 55000)
e5 = Employee("171G30", "Ajay", 45, 44000)

# List of Employee objects
employee_list = [e1, e2, e3, e4, e5]

# Function to sort the list of Employee objects by a given attribute
def sort_employee_list(data_list, attribute):
    sorted_list = sorted(data_list, key=lambda employee: getattr(employee, attribute))
    return sorted_list

while True:
    print("Choose a sorting criterion:")
    print("1. Sort by Id")
    print("2. Sort by Name")
    print("3. Sort by Age")
    print("4. Sort by Salary")
    print("Enter your choice (1/2/3/4):")

    choice = input()
    
    if choice == '1':
        sorted_list = sort_employee_list(employee_list, "Id")
    elif choice == '2':
        sorted_list = sort_employee_list(employee_list, "Name")
    elif choice == '3':
        sorted_list = sort_employee_list(employee_list, "Age")
    elif choice == '4':
        sorted_list = sort_employee_list(employee_list, "Salary")
    else:
        print("Invalid choice")
        continue
    
    # Print the sorted list
    for employee in sorted_list:
        print(f"Id: {employee.Id}, Name: {employee.Name}, Age: {employee.Age}, Salary: {employee.Salary}")
