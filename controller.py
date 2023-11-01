from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        while True:
            choice = self.show_menu()
            if choice == '1':
                self.run_tablets_add()
            elif choice == '2':
                self.run_tablets()
            elif choice == '3':
                self.run_tablets_update()
            elif choice == '4':
                self.run_tablets_delete()
            elif choice == '5':
                self.run_tablets_random()
            elif choice == '6':
                self.run_tablets_search()
            elif choice == '7':
                break

    def run_tablets(self):
        while True:
            choice = self.show_menu_tablets()
            if choice == '1':
                self.view_tasks_tab1()
            elif choice == '2':
                self.view_tasks_tab2()
            elif choice == '3':
                self.view_tasks_tab3()
            elif choice == '4':
                break

    def run_tablets_update(self):
        while True:
            choice = self.show_menu_tablets()
            if choice == '1':
                self.update_task_tab1()
            elif choice == '2':
                self.update_task_tab2()
            elif choice == '3':
                self.update_task_tab3()
            elif choice == '4':
                break

    def run_tablets_add(self):
        while True:
            choice = self.show_menu_tablets()
            if choice == '1':
                self.add_task_tab1()
            elif choice == '2':
                self.add_task_tab2()
            elif choice == '3':
                self.add_task_tab3()
            elif choice == '4':
                break

    def run_tablets_delete(self):
        while True:
            choice = self.show_menu_tablets()
            if choice == '1':
                self.delete_task_tab1()
            elif choice == '2':
                self.delete_task_tab2()
            elif choice == '3':
                self.delete_task_tab3()
            elif choice == '4':
                break

    def run_tablets_random(self):
        while True:
            choice = self.show_menu_tablets()
            if choice == '1':
                self.random_task_tab1()
            elif choice == '2':
                self.random_task_tab2()
            elif choice == '3':
                self.random_task_tab3()
            elif choice == '4':
                break

    def run_tablets_search(self):
        while True:
            choice = self.show_menu_tablets()
            if choice == '1':
                self.search_task_tab1()
            elif choice == '2':
                self.search_task_tab2()
            elif choice == '3':
                self.search_task_tab3()
            elif choice == '4':
                break

    def show_menu(self):
        self.view.show_message("\nMenu:")
        self.view.show_message("1. Add Task")
        self.view.show_message("2. View Tasks")
        self.view.show_message("3. Update Task")
        self.view.show_message("4. Delete Task")
        self.view.show_message("5. Random Fill")
        self.view.show_message("6. Search")
        self.view.show_message("7. Quit")
        return input("Enter your choice: ")

    def show_menu_tablets(self):
        self.view.show_message("\nTablets:")
        self.view.show_message("1. USER")
        self.view.show_message("2. Projects")
        self.view.show_message("3. Comments")
        self.view.show_message("4. Quit")
        return input("Enter your choice: ")

    def add_task_tab1(self):
        userid, title, description = self.view.get_task_input_full_tab1()
        self.model.add_task_tab1(userid, title, description)

    def add_task_tab2(self):
        projectid, userid, title, description = self.view.get_task_input_full_tab2()
        self.model.add_task_tab2(projectid, userid, title, description)

    def add_task_tab3(self):
        commentid, projectid, userid, title, description = self.view.get_task_input_full_tab3()
        self.model.add_task_tab3(commentid, projectid, userid, title, description)

    def view_tasks_tab1(self):
        tasks = self.model.get_all_tasks_tab1()
        self.view.show_tasks_tab1(tasks)

    def view_tasks_tab2(self):
        tasks = self.model.get_all_tasks_tab2()
        self.view.show_tasks_tab2(tasks)

    def view_tasks_tab3(self):
        tasks = self.model.get_all_tasks_tab3()
        self.view.show_tasks_tab3(tasks)

    def update_task_tab1(self):
        task_id = self.view.get_task_id()
        title, description = self.view.get_task_input_tab1()
        self.model.update_task_tab1(task_id, title, description)

    def update_task_tab2(self):
        task_id = self.view.get_task_id()
        title, description = self.view.get_task_input_tab2()
        self.model.update_task_tab2(task_id, title, description)

    def update_task_tab3(self):
        task_id = self.view.get_task_id()
        title, description = self.view.get_task_input_tab3()
        self.model.update_task_tab3(task_id, title, description)


    def delete_task_tab1(self):
        task_id = self.view.get_task_id()
        self.model.delete_task_tab1(task_id)

    def delete_task_tab2(self):
        task_id = self.view.get_task_id()
        self.model.delete_task_tab2(task_id)

    def delete_task_tab3(self):
        task_id = self.view.get_task_id()
        self.model.delete_task_tab3(task_id)

    def random_task_tab1(self):
        amount = self.view.get_amount()
        self.model.random_add_task_tab1(amount)
        self.view.show_message("Random staff added successfully!")

    def random_task_tab2(self):
        amount = self.view.get_amount()
        self.model.random_add_task_tab2(amount)
        self.view.show_message("Random staff added successfully!")

    def random_task_tab3(self):
        amount = self.view.get_amount()
        self.model.random_add_task_tab3(amount)
        self.view.show_message("Random staff added successfully!")

    def search_task_tab1(self):
        min_id, max_id = self.view.get_task_id_minmax()
        title, description = self.view.get_task_input_tab1()
        self.model.search_tab1(min_id, max_id, title, description)

    def search_task_tab2(self):
        min_user_id, max_user_id = self.view.get_task_id_minmax()
        min_project_id, max_project_id = self.view.get_task_id_minmax()
        title, min_date, max_date = self.view.get_task_input_text_dateminmax()
        self.model.search_tab2(min_project_id, max_project_id, min_user_id, max_user_id, title, min_date, max_date)

    def search_task_tab3(self):
        min_user_id, max_user_id = self.view.get_task_id_minmax()
        min_project_id, max_project_id = self.view.get_task_id_minmax()
        min_comment_id, max_comment_id = self.view.get_task_id_minmax()
        title, min_date, max_date = self.view.get_task_input_text_dateminmax()
        self.model.search_tab3(min_comment_id, max_comment_id, min_project_id, max_project_id, min_user_id, max_user_id, title, min_date, max_date)