from todolist import Todolist
from menu import Menu
from project import Project


"""
Classi da definire:
- menu
-project
- task
-tag
"""

# class Menu ():

#     def printMenu(self) ->None:
#         print(f"""
#         1. Add Project
#         2. Add Task
#         3. Add Tag
#         4. List Projects
#         5. List Task
#         6. List Tags
#         7. Exit
#     """)


# import uuid
# class Project:
#     def __init__(self, name: str):
#         self.id = uuid.uuid4()
#         self.name = name
#         self.task_list = []

#     def get_tasks_lenght(self)-> int:
#         return len(self.task_list)
    
#     def get_project_name(self)-> str:
#         return self.name
    
#     def set_project_name(self, new_name: str)-> None:
#         self.name = new_name
    

# class Todolist:
#     def __init__(self):
#         self.projects =[]
    
#     def add_project(self, project: Project)-> None:
#         self.projects.append(project)

#     def get_projects_lenght(self)-> int:
#         return len(self.projects)
    
#     def get_project(self)-> list[Project]:
#         for p in self.projects:
#             return f"{p.id}: {p.name}"


   


def main():
    todolist = Todolist()
    # print(todolist.projects)
    menu = Menu()
    menu.printMenu()


    i = input( "Seleziona operazione da eseguire: ")

    match i:
        case "1":
            print("Hai scento aggiungi Progetto")
            print('=' *20)
            project_name = input("Inserisci il nome del progetto: ")
            project = Project(project_name)
            todolist.add_project(project)
        case "2":
            print("Aggiungi Task")
        case "3":
            print("Aggiungi Tag")     
        case "4":
            print("Lista Progetti")
            
        case "5":
            print("Lista Task")
            
        case "6":
            print("Lista Tag")
    
        case "7":
            print("Esci")
            exit()
        case _:
            print("Inserisci il valore corretto")           




if __name__ == "__main__":
    main()# This is the main entry point of the application