from datetime import datetime
class View:

    def show_tasks(self, tasks):
        print("Tasks:")
        for task in tasks:
            print(f"ID: {task[0]}, Title: {task[1]}, Description: {task[2]}")

    def show_tasks_tab1(self, tasks):
        print("Tasks in tablet USER:")
        for task in tasks:
            print(f"user_ID: {task[0]}, username: {task[1]}, EMAIL: {task[2]}")

    def show_tasks_tab2(self, tasks):
        print("Tasks in tablet Projects:")
        for task in tasks:
            print(f"user_ID: {task[1]}, project_id: {task[0]}, Date of publication: {task[2]}, Project name: {task[3]}")

    def show_tasks_tab3(self, tasks):
        print("Tasks in tablet Comments:")
        for task in tasks:
            print(f"user_ID: {task[2]}, project_id: {task[1]}, comment_id: {task[0]}, text: {task[3]}, Date of publication: {task[4]}")

    def get_task_input_full_tab1(self):
        userid = input("Enter user_id(only available): ")
        title = input("Enter username: ")
        description = input("Enter email: ")
        return userid, title, description

    def get_task_input_full_tab2(self):
        projectid = input("Enter user_id(only available): ")
        userid = input("Enter project_id(only available): ")
        title = input("Enter projectname: ")
        description = input("Enter date: ")
        return userid, projectid, title, description

    def get_task_input_full_tab3(self):
        commentid = input("Enter comment_id(only available): ")
        projectid = input("Enter project_id(only available): ")
        userid = input("Enter user_id(only available): ")
        title = input("Enter text: ")
        description = input("Enter date: ")
        return commentid, projectid, userid, title, description

    def get_task_input_tab1(self):
        title = input("Enter username: ")
        description = input("Enter email: ")
        return title, description

    def get_task_input_tab2(self):
        title = input("Enter project name: ")
        description = input("Enter date (YYYY-MM-DD): ")
        try:
            datetime.strptime(description, '%Y-%m-%d')
        except ValueError:
            print("Error: Date should be in YYYY-MM-DD format.(Will be returned default - 2000-01-01)")
            return title, '2000-01-01'
        return title, description


    def get_task_input_tab3(self):
        title = input("Enter text: ")
        description = input("Enter date (YYYY-MM-DD): ")
        try:
            datetime.strptime(description, '%Y-%m-%d')
        except ValueError:
            print("Error: Date should be in YYYY-MM-DD format.(Will be returned default - 2000-01-01)")
            return title, '2000-01-01'
        return title, description

    def get_task_id(self):
        while True:
            try:
                task_id = int(input("Enter ID: "))
                return task_id
            except ValueError:
                print("Error: Please enter a valid integer ID.")

    def get_task_id_minmax(self):
        while True:
            try:
                task_id_min = int(input("Enter min ID: "))
                task_id_max = int(input("Enter max ID: "))
                return task_id_min, task_id_max
            except ValueError:
                print("Error: Please enter a valid integer ID.")

    def get_task_input_text_dateminmax(self):
        title = input("Enter text: ")
        mintime = input("Enter min date (YYYY-MM-DD): ")
        maxtime = input("Enter max date (YYYY-MM-DD): ")
        try:
            datetime.strptime(mintime, '%Y-%m-%d')
            datetime.strptime(maxtime, '%Y-%m-%d')
        except ValueError:
            print("Error: Date should be in YYYY-MM-DD format.(Will be returned default: 2000-01-01 - 2099-12-31)")
            return title, '2000-01-01', '2099-12-31'
        return title, mintime, maxtime

    def get_amount(self):
        while True:
            try:
                task_id = int(input("Enter amount of random tasks: "))
                return task_id
            except ValueError:
                print("Error: Please enter a valid integer amount.")

    def show_message(self, message):
        print(message)