from template import hCSS as frontend_tamplate
import os
import json
import logging
Temp = frontend_tamplate()
HTML = Temp.html
JAVAS = Temp.javaS
estiloCSS = Temp.estilo
Json = Temp.json
conteudoH = Temp.post_html
conteudoJ = Temp.javaS_post
List_dir_html = Temp.diretorio_list_html
ListDirJs = Temp.diretorio_list_js

class Project:
    def __init__(self, workspace_name):
        self.workspace_name = workspace_name
        self.BOOTSTRAP_FOLDER = "{workspace}/bootstrap/".format(
            workspace=workspace_name
        )
        self.CSS_FOLDER = "{workspace}/css/".format(
            workspace=workspace_name
        )
        self.POSTS_FOLDER = "{workspace}/conteudo/".format(
            workspace=workspace_name
        )

    def process(self):
        project_workspace = os.path.dirname(self.workspace_name)
        bootstrap_folder = os.path.dirname(self.BOOTSTRAP_FOLDER)
        css_folder = os.path.dirname(self.CSS_FOLDER)
        posts_folder = os.path.dirname(self.POSTS_FOLDER)

        if not os.path.exists(project_workspace):
            os.makedirs(projectproject_workspace_name)
            self.index = open(project_workspace + '/index.html', 'w+')

            #ESCREVEREMOS DENTRO DESSE ARQUIVO O TEXTO ESCRITO NO ARQUIVO TEMPLATE html
            self.index.write(HTML)

            #ABRIREMOS UM ARQUIVO DENTRO DO DIRETORIO. SE NAO EXISTIR, VAMOS CRIA-LO
            self.javascript = open(project_name +'/java.js', 'w+' )
            

            #VAMOS ESCREVER O JAVASCRIPT VINDO DA PAGINA TEMPLATE
            self.javascript.write(JAVAS)

            # O MESMO ACONTECE COM O JSON
            self.j = open(project_name +'/data.json','w+')
            self.j.write(Json)
            
            
            # #SE O DIRETORIO NAO EXISTIR
            if not os.path.exists(bootstrap):
                os.makedirs(bootstrap)

                #ENTRAR NA PASTA bootstrap/ BAIXAR O BOOTSTRAP/DESCOMPACTAR O BOOTSTRAP BAIXADO
                os.system('cd ' + bootstrap + ' && wget https://github.com/twbs/bootstrap/releases/download/v4.1.2/bootstrap-4.1.2-dist.zip && unzip bootstrap-4.1.2-dist.zip')
                self.arq = open(css + '/estilo.css', 'w+')
                self.arq.write(estiloCSS)

            #CRIAR A PASTA CONTENT E INSERIR O JS DOS POSTS E DA LISTAGEM DE DIRETORIOS LÁ CASO O DIRETORIO CONTEUDO NAO EXISTA 
            if not os.path.exists(posts):
                os.makedirs(posts)
                self.js_post = open(posts + '/js_post.js', 'w+')
                self.js_post.write(conteudoJ)
                self.js_dir_list = open(posts + '/dir_list.js', 'w+')
                self.js.dir_list.write(List_dir_js)

            #CASO ELE EXISTA VAMOS APENAS CRIAR/ ESCREVER OS CONTEUDOS NOS ARQUIVOS
            else: 
                self.js_post = open(posts + '/js_post.js', 'w+')
                self.js_post.write(conteudoJ)
                self.js_dir_list = open(posts + '/dir_list.js', 'w+')
                
                self.js_dir_list.write(ListDirJs)
                
        return True

class Post:
    def __init__(self, post_basic_information):
        self.name = post_basic_information[0]
        self.category = post_basic_information[1]
        self.workspace = post_basic_information[2]
    
    def update_posts_metadata(self):
        metadata_file = open(self.workspace + '/data.json', 'r+')
        metadata = files.read()
        dados = json.loads(metadata)      
        agora = datetime.datetime.now()
        dados[1]['posts'][pasta_nome_post] = {"title": "titulo do post", "categoria": str(categoria),"Data": str(agora.day) + '/' + str(agora.month) + '/' + str(agora.year), "conteudo": "SEU CONTEUDO DEVE SER INSERIDO AQUI"} 
        files.seek(0)

        json.dump(dados, metadata_file, indent = 4)
    
    def process(self):
        self.update_posts_metadata()
        category_path = self.workspace + '/conteudo/' + self.category + '/'
        
        if not os.path.exists(category_path):
            os.makedirs(category_path)
           
            category_main_page = self.category + '.html'
            post_template = self.name + '.html'
           
            category_main_page = open(category_path + category_main_page, 'w+')
            category_main_page.write(List_dir_html)
            
            post = open(category_path + post_template, 'w+')
            post.write(conteudoH)
        else:
            post = open(category_path + self.name + '.html', 'w+')
            post.write(conteudoH)
        
        
