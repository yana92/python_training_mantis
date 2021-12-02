from model.project import Project

def test_create_project(app, db, json_projects):
    old_projects = db.get_project_list()
    project = json_projects
    app.project.create_project(project)
    old_projects.append(project)
    new_projects = db.get_project_list()
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


