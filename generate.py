from template import hCSS
import os, json
Temp = hCSS()
HTML = Temp.html
JAVAS = Temp.javaS
estiloCSS = Temp.estilo
Json = Temp.json
conteudoH = Temp.post_html
conteudoJ = Temp.javaS_post
List_dir_html = Temp.diretorio_list_html
ListDirJs = Temp.diretorio_list_js
class gerador():
    def __init__(self,arg,pasta):
        self.arg = arg
        self.pasta = pasta

        
        if self.arg.lower() == 'novo':
            self.gerar_projeto(self.pasta)

    def gerar_projeto (self, pasta):
        self.dir = os.path.dirname(pasta)
        self.bootstrap = os.path.dirname(str(self.dir)+ '/bootstrap/')
        self.estilo = os.path.dirname(str(self.bootstrap)+'/css/')
        self.content = os.path.dirname(str(self.dir) + '/conteudo/')
        self.principal_content = os.path.dirname(str(self.dir) + '/conteudo/principal/')

        #VERIFICAMOS SE A PASTA EXISTE
        if not os.path.exists(self.dir):

            #SE NÃO EXISTIR, VAMOS CRIA-LA
            os.makedirs(self.dir)
            #ABRIREMOS UM ARQUIVO DENTRO DO DIRETORIO, SE ELE NAO EXISTIR, CRIAMOS UM ARQUIVO INDEX DENTRO DO DIRETORIO E O ABRIREMOS
            self.index = open(str(self.dir) + '/index.html', 'w+')

            #ESCREVEREMOS DENTRO DESSE ARQUIVO O TEXTO ESCRITO NO ARQUIVO TEMPLATE html
            self.index.write(HTML)

            #ABRIREMOS UM ARQUIVO DENTRO DO DIRETORIO. SE NAO EXISTIR, VAMOS CRIA-LO
            self.javascript = open(str(self.dir)+'/java.js', 'w+' )
            

            #VAMOS ESCREVER O JAVASCRIPT VINDO DA PAGINA TEMPLATE
            self.javascript.write(JAVAS)

            # O MESMO ACONTECE COM O JSON
            self.j = open(str(self.dir)+'/data.json','w+')
            self.j.write(Json)

            os.makedirs(self.principal_content)
            
            
            # #SE O DIRETORIO NAO EXISTIR
            if not os.path.exists(self.bootstrap):
                os.makedirs(self.bootstrap)

                #ENTRAR NA PASTA self.bootstrap/ BAIXAR O BOOTSTRAP/DESCOMPACTAR O BOOTSTRAP BAIXADO
                os.system('cd ' + str(self.bootstrap) + ' && wget https://github.com/twbs/bootstrap/releases/download/v4.1.2/bootstrap-4.1.2-dist.zip && unzip bootstrap-4.1.2-dist.zip')
                self.arq = open(str(self.estilo) + '/estilo.css', 'w+')
                self.arq.write(estiloCSS)

            #CRIAR A PASTA CONTENT E INSERIR O JS DOS POSTS E DA LISTAGEM DE DIRETORIOS LÁ CASO O DIRETORIO CONTEUDO NAO EXISTA 
            if not os.path.exists(self.content):
                os.makedirs(self.content)
                self.js_post = open(str(self.content) + '/js_post.js', 'w+')
                self.js_post.write(conteudoJ)
                self.js_dir_list = open(str(self.content) + '/dir_list.js', 'w+')
                self.js.dir_list.write(List_dir_js)

            #CASO ELE EXISTA VAMOS APENAS CRIAR/ ESCREVER OS CONTEUDOS NOS ARQUIVOS
            else: 
                self.js_post = open(str(self.content) + '/js_post.js', 'w+')
                self.js_post.write(conteudoJ)
                self.js_dir_list = open(str(self.content) + '/dir_list.js', 'w+')
                
                self.js_dir_list.write(ListDirJs)
                
        return True            


    #CRIAR POSTS
    def newPost(self, nome_post, pasta_proj, categoria):
        self.nome_post = nome_post
        self.pasta_proj = pasta_proj
        self.categoria = categoria
        self.caminho = self.pasta_proj + '/conteudo/' + self.categoria + '/'
        
        if not os.path.exists(self.caminho):
            os.makedirs(self.caminho)
            self.dir_list = open(self.caminho + str(categoria) + '.html', 'w+')
            self.dir_list.write(List_dir_html)
            self.post = open(self.caminho + str(self.nome_post) + '.html', 'w+')
            self.post.write(conteudoH)
        else:
            
            self.post = open(self.caminho + str(self.nome_post) + '.html', 'w+')
            self.post.write(conteudoH)
        return True
