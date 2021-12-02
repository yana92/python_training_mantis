from model.project import Project
from generator.project import testdata
import pytest

@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_create_project(app, db, project):
    old_projects = db.get_project_list()
    app.project.create_project(project)
    old_projects.append(project)
    new_projects = db.get_project_list()
    assert len(old_projects) == len(new_projects)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


