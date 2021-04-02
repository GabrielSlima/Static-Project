from template import hCSS as frontend_tamplate
import os
import json
import logging
from datetime import datetime


class Project:
    template = frontend_tamplate()
    BOOTSTRAP_PACKAGE_NAME = "bootstrap-4.1.2-dist.zip"
    BOOTSTRAP_ADDRESS = "https://github.com/twbs/bootstrap/releases/download/v4.1.2/{package_name}"

    def __init__(self, workspace_name):
        self.WORKSPACE =  os.path.dirname(workspace_name[0] + "/") 
        
        self.BOOTSTRAP_FOLDER = os.path.dirname(
            "{workspace}/bootstrap/".format(workspace=self.WORKSPACE)
        )
        
        self.CSS_FOLDER = os.path.dirname(
            "{workspace}/bootstrap/css/".format(workspace=self.WORKSPACE)
        )
        
        self.POSTS_FOLDER = os.path.dirname(
            "{workspace}/conteudo/".format(workspace=self.WORKSPACE)
        )
        
        self.BOOTSTRAP_ADDRESS = self.BOOTSTRAP_ADDRESS.format(
            package_name=self.BOOTSTRAP_PACKAGE_NAME
        )

        self.CORE_ELEMENTS = {
            "main_page": {
                "main_page": {
                    "name": "index.html",
                    "template": self.template.html,
                    "base_path": self.WORKSPACE
                },
                "main_page_javascript": {
                    "name": "java.js",
                    "template": self.template.javaS,
                    "base_path": self.WORKSPACE
                }
            },
            "posts": {
                "posts_javascript": {
                    "name": "js_post.js",
                    "template": self.template.javaS_post,
                    "base_path": self.POSTS_FOLDER
                },
                "categories_main_page_javascript": {
                    "name": "dir_list.js",
                    "template": self.template.diretorio_list_js,
                    "base_path": self.POSTS_FOLDER
                }
            },
            "global_usage": {
                "metadata": {
                    "name": "data.json",
                    "template": self.template.json,
                    "base_path": self.WORKSPACE
                },
                "css": {
                    "name": "estilo.css",
                    "template": self.template.estilo,
                    "base_path": self.CSS_FOLDER
                }
            }
        }

    def fetch_bootstrap(self):
        os.system(
            'cd {bootstrap_folder} && wget {bootstrap_address} && unzip {package_name}'.format(
                bootstrap_folder=self.BOOTSTRAP_FOLDER,
                bootstrap_address=self.BOOTSTRAP_ADDRESS,
                package_name=self.BOOTSTRAP_PACKAGE_NAME
            )
        )

    def process(self):
        if os.path.exists(self.WORKSPACE):
           logging.info("The project already exists, please try again with another name.")
           return

        os.makedirs(self.WORKSPACE)
        os.makedirs(self.POSTS_FOLDER)
        os.makedirs(self.BOOTSTRAP_FOLDER)
        os.makedirs(self.CSS_FOLDER)
        self.fetch_bootstrap()
            
        for core_elements_group in self.CORE_ELEMENTS.values():
            logging.info("Creating core elements...")
            for core_element in core_elements_group.values(): 
                element_path = "{base_path}/{name}".format(
                    base_path=core_element.get('base_path'),
                    name=core_element.get('name')
                )
                element = open(element_path, 'w+')
                element.write(core_element.get('template'))
                element.close()
        logging.info("The project was created at {}".format(os.path.realpath(self.WORKSPACE)))

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
        json_matadata[1]['posts'][self.name] = self.METADATA_TEMPLATE
        json.dump(json_matadata, metadata_file, indent=4)
        
        metadata_file.truncate()
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
        logging.info("A new template was created for {}".format(self.name))
