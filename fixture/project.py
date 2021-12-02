from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_manage_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_overview_page.php")):
            wd.find_element_by_link_text("Manage").click()

    def open_manage_projects_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php")):
            self.open_manage_page()
            wd.find_element_by_link_text("Manage Projects").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)

    def create_project(self, project):
        wd = self.app.wd
        self.open_manage_projects_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        #fill project form
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def delete_project_by_name(self, name):
        wd = self.app.wd
        self.open_manage_projects_page()
        self.select_project_by_name(name)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

    def select_project_by_name(self, name):
        wd = self.app.wd
        wd.find_element_by_link_text("%s" % name).click()