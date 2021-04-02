from template import hCSS as frontend_tamplate
import os
import json
import logging
from datetime import datetime

class Project:
    BOOTSTRAP_PACKAGE_NAME = "bootstrap-4.1.2-dist.zip"
    BOOTSTRAP_ADDRESS = "https://github.com/twbs/bootstrap/releases/download/v4.1.2/{package_name}"
    
    def __init__(self, workspace_name):
        self.workspace_name = workspace_name[0]
        self.BOOTSTRAP_FOLDER = "{workspace}/bootstrap/".format(
            workspace=self.workspace_name
        )
        self.CSS_FOLDER = "{workspace}/bootstrap/css/".format(
            workspace=self.workspace_name
        )
        self.POSTS_FOLDER = "{workspace}/conteudo/".format(
            workspace=self.workspace_name
        )
        self.BOOTSTRAP_ADDRESS = self.BOOTSTRAP_ADDRESS.format(
            package_name=self.BOOTSTRAP_PACKAGE_NAME
        )

    def process(self):
        template = frontend_tamplate()
        project_workspace = os.path.dirname(self.workspace_name + "/")
        bootstrap_folder = os.path.dirname(self.BOOTSTRAP_FOLDER)
        css_folder = os.path.dirname(self.CSS_FOLDER)
        posts_folder = os.path.dirname(self.POSTS_FOLDER)

        core_elements = {
            "main_page": {
                "name": "index.html",
                "template": template.html
            },
            "main_page_javascript": {
                "name": "java.js",
                "template": template.javaS
            },
            "metadata": {
                "name": "data.json",
                "template": template.json
            }
        }

        if not os.path.exists(project_workspace):
            os.makedirs(project_workspace)
            for core_element in core_elements:
                logging.info("Creating core element {}".format(core_element))
                element_path = "{workspace}/{name}".format(
                    workspace=project_workspace,
                    name=core_elements.get(core_element['name'])
                )
                
                element = open(element_path, 'w+')
                element.write(core_elements.get(core_element['template']))
                element.close()
            
            if not os.path.exists(bootstrap_folder):
                os.makedirs(bootstrap_folder)
                os.system(
                    'cd {bootstrap_folder} && wget {bootstrap_address} && unzip {package_name}'.format(
                        bootstrap_folder=bootstrap_folder,
                        bootstrap_address=self.BOOTSTRAP_ADDRESS,
                        package_name=self.BOOTSTRAP_PACKAGE_NAME
                    )
                )
                main_page_css = open(css_folder + '/estilo.css', 'w+')
                main_page_css.write(template.estilo)

            if not os.path.exists(posts_folder):
                os.makedirs(posts_folder)

            posts_javascript = open(posts_folder + '/js_post.js', 'w+')
            posts_javascript.write(template.javaS_post)
            
            categories_main_page_javascript = open(posts_folder + '/dir_list.js', 'w+')
            categories_main_page_javascript.write(template.diretorio_list_js)

class Post:
    POSTS_CREATION_DATE_MASK = "%d/%m/%Y"
    def __init__(self, post_basic_information):
        self.name = post_basic_information[0]
        self.category = post_basic_information[1]
        self.workspace = post_basic_information[2]
        self.METADATA_TEMPLATE = {
            "title": "Title",
            "categoria": self.category,
            "Data": datetime.now().strftime(self.POSTS_CREATION_DATE_MASK), 
            "conteudo": "Content"
        }
    
    def update_posts_metadata(self):
        metadata_file = open(self.workspace + '/data.json', 'r+')
        metadata = metadata_file.read()
        metadata_file.seek(0)
        json_matadata = json.loads(metadata)
        json_matadata[1]['posts'][self.name] =  self.METADATA_TEMPLATE
        json.dump(json_matadata, metadata_file, indent = 4)
        metadata_file.close()
    
    def process(self):
        self.update_posts_metadata()
        template = frontend_tamplate()
        category_path = self.workspace + '/conteudo/' + self.category + '/'
        
        if not os.path.exists(category_path):
            os.makedirs(category_path)
           
            category_main_page = self.category + '.html'
            post_template = self.name + '.html'
           
            category_main_page = open(category_path + category_main_page, 'w+')
            category_main_page.write(template.diretorio_list_html)
            category_main_page.close()
        post = open(category_path + self.name + '.html', 'w+')
        post.write(template.post_html)
        post.close()
        
        
