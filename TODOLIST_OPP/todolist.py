
from project import Project


class Todolist:
    def __init__(self):
        self.projects: list[Project] = []

    """Add a single project to a list of projects"""
    def add_project(self, project: Project)-> None:
        self.projects.append(project)

    """Return the number of projects inside the project list"""
    def get_projects_lenght(self)-> int:
        return len(self.projects)
    
    
    def get_project(self)-> list[Project]:
        for p in self.projects:
            return f"{p.id}: {p.name}"