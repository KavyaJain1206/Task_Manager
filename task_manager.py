import csv
from datetime import datetime

class Task:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.due_date = ""
        self.priority = ""
        self.status = "Not Started"

    def new_task(self):
        self.name = input("Enter task name: ")
        self.description = input("Description: ")
        self.due_date = input("Due Date (YYYY-MM-DD): ")
        self.priority = input("Priority (Low/Medium/High): ")

    def display_task(self):
        print(f"Task: {self.name}")
        print(f"Description: {self.description}")
        print(f"Due Date: {self.due_date}")
        print(f"Priority: {self.priority}")
        print(f"Status: {self.status}")

    def add_to_csv(self):
        with open('tasks.csv', 'a', newline='') as f:
            csvwriter = csv.writer(f)
            if f.tell() == 0:
                csvwriter.writerow(['Name', 'Description', 'Due Date', 'Priority', 'Status'])
            csvwriter.writerow([self.name, self.description, self.due_date, self.priority, self.status])

    @staticmethod
    def all_tasks():
        with open("tasks.csv", 'r') as f:
            csvreader = csv.reader(f)
            header = next(csvreader, None)
            tasks = [dict(zip(header, row)) for row in csvreader]

        if tasks:
            print(f"{'Name': <20} {'Description': <30} {'Due Date': <12} {'Priority': <10} {'Status': <15}")
            print('-' * 90)
            for task in tasks:
                print(f"{task['Name']: <20} {task['Description']: <30} {task['Due Date']: <12} {task['Priority']: <10} {task['Status']: <15}")
        else:
            print("No tasks found.")

    @staticmethod
    def delete_task(task_name):
        with open("tasks.csv", 'r') as f:
            rows = list(csv.reader(f))

        deleted = False
        with open("tasks.csv", 'w', newline='') as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(['Name', 'Description', 'Due Date', 'Priority', 'Status'])
            for row in rows:
                if row[0] != task_name:
                    csvwriter.writerow(row)
                else:
                    deleted = True
        if deleted:
            print(f'Task "{task_name}" deleted successfully.')
        else:
            print(f'Task "{task_name}" not found.')

    @staticmethod
    def edit_task(task_name):
        with open('tasks.csv', 'r') as file:
            rows = list(csv.reader(file))

        edited = False
        with open('tasks.csv', 'w', newline='') as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(['Name', 'Description', 'Due Date', 'Priority', 'Status'])
            for row in rows:
                if row[0] == task_name:
                    new_task_name = input(f'Enter new name for task "{task_name}": ')
                    new_description = input(f'Enter new description for task "{task_name}": ')
                    new_due_date = input(f'Enter new due date for task "{task_name}" (YYYY-MM-DD): ')
                    new_priority = input(f'Enter new priority for task "{task_name}" (Low/Medium/High): ')
                    row[0] = new_task_name
                    row[1] = new_description
                    row[2] = new_due_date
                    row[3] = new_priority
                    edited = True
                csvwriter.writerow(row)

        if edited:
            print(f'Task "{task_name}" edited successfully.')
        else:
            print(f'Task "{task_name}" not found.')

    @staticmethod
    def sort_by_priority():
        with open("tasks.csv", 'r') as f:
            csvreader = csv.reader(f)
            header = next(csvreader, None)
            tasks = [dict(zip(header, row)) for row in csvreader]

            sorted_tasks = sorted(tasks, key=lambda x: ['Low', 'Medium', 'High'].index(x['Priority']))

        print("Tasks Sorted by Priority:")
        if sorted_tasks:
            Task._display_sorted_tasks(sorted_tasks)
        else:
            print("No tasks found.")

    @staticmethod
    def sort_by_due_date():
        with open("tasks.csv", 'r') as f:
            csvreader = csv.reader(f)
            header = next(csvreader, None)
            tasks = [dict(zip(header, row)) for row in csvreader]

            sorted_tasks = sorted(tasks, key=lambda x: datetime.strptime(x['Due Date'], '%Y-%m-%d'))

        print("Tasks Sorted by Due Date:")
        if sorted_tasks:
            Task._display_sorted_tasks(sorted_tasks)
        else:
            print("No tasks found.")

    @staticmethod
    def _display_sorted_tasks(sorted_tasks):
        print(f"{'Name': <20} {'Description': <30} {'Due Date': <12} {'Priority': <10} {'Status': <15}")
        print('-' * 90)
        for task in sorted_tasks:
            print(f"{task['Name']: <20} {task['Description']: <30} {task['Due Date']: <12} {task['Priority']: <10} {task['Status']: <15}")


if __name__ == "__main__":
    task = Task()
    while True:
        print("Task Manager\n" + "1.Add Task\n2.Delete Task\n3.Edit Task\n4.Show All Tasks\n5.Sort by Priority\n6.Sort by Due Date\n7.Exit the task manager")
        try:
            user_input = int(input("Enter the option number: "))
            if user_input == 1:
                task.new_task()
                task.add_to_csv()
            elif user_input == 2:
                Task.delete_task(input("Enter the task name to be deleted: "))
            elif user_input == 3:
                Task.edit_task(input("Enter the Task Name To be Edited: "))
            elif user_input == 4:
                Task.all_tasks()
            elif user_input == 5:
                Task.sort_by_priority()
            elif user_input == 6:
                Task.sort_by_due_date()
            elif user_input == 7:
                print("Thank You for using the task manager!")
                break
            else:
                print("Not a Valid input!")
        except ValueError:
            print("Invalid input. Please enter a numeric option.")
