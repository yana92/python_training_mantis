from model.project import Project
import random

def test_delete_project(app, db):
    if len(db.get_project_list()) == 0:
        app.project.create_project(Project(name="Test Project"))
    old_projects = db.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_name(project.name)
    old_projects.remove(project)
    new_projects = db.get_project_list()
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)