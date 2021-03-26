import core
import sys
import json
import datetime
import logging

AVAILABLE_FLOWS = {
    "new": {
        "arguments": [
            "project_name"
        ],
        "processor": core.create_new_project
    },
    "post": {
        "arguments": [
            "post_name",
            "project_name",
            "post_category"
        ],
        "processor": core.create_new_post
    }
}
MINIMUM_COMMAND_LINE_ARGS = 1
FLOW_POSITION = 1
SCRIPT_NAME = 1

USAGE_SUMMARY = """
How to use ->
python3 main.py <COMMAND> <COMMAND_ARGUMENTS>
Create a new project: python3 main.py new <PROJECT_NAME>
Create a new blog post: python3 main.py post <POST_NAME> <PROJECT_NAME> <POST_CATEGORY>
"""

def exit_program():
    invalid_arguments_message = """
    Invalid amount of arguments, please try again with: \n {usage_summary}
    """
    invalid_arguments_message = invalid_arguments_message.format(
        usage_summary=USAGE_SUMMARY
    )
    logging.info(invalid_arguments_message)
    sys.exit(1)

user_input = sys.argv

if (len(user_input) -SCRIPT_NAME < MINIMUM_COMMAND_LINE_ARGS or 
        not AVAILABLE_FLOWS.get(user_input[FLOW_POSITION])):
    exit_program()

if len(user_input) -SCRIPT_NAME != len(AVAILABLE_FLOWS.get(user_input[FLOW_POSITION])):
    exit_program()

processor = AVAILABLE_FLOWS[user_input[FLOW_POSITION]]['processor']
processor(user_input[FLOW_POSITION + 1: ])
else:
    if argumento.lower() == 'post' and pasta_nome_post != " " and sys.argv[3] != " " and sys.argv[4] != " ":
        print("Gerando arquivos...")
        #PRIMEIRO SERA INSERIDO, O POST, NO JSON
        #ABERTURA DO ARQUIVO EM MODO ESCRITA/LEITURA
        pasta_destino = sys.argv[3]
        categoria = sys.argv[4]  
        try:
            files = open(str(pasta_destino) + '/data.json', 'r+')
             #LEITURA DO ARQUIVO
            leitura = files.read()
            #PASSANDO DE JSON PARA PARA ALGO QUE O PYTHON ENTENDA, GERALMENTE, LISTA, DICIONARIOS ETC.
            dados = json.loads(leitura)
                
            #INSTANCIA DA CLASS DATETIME
            agora = datetime.datetime.now()

            #ATRIBUIÇÃO DE UM NOVO POST COM DADOS GENERICOS
            dados[1]['posts'][pasta_nome_post] = {"title": "titulo do post", "categoria": str(categoria),"Data": str(agora.day) + '/' + str(agora.month) + '/' + str(agora.year), "conteudo": "SEU CONTEUDO DEVE SER INSERIDO AQUI"}
                
            files.seek(0)

            #"OFICIALIZANDO" AS ALTERAÇOES DO JSON DANDO UM DUMP, NADA MAIS É DO QUE GERAR O NOVO BINARIO JSON
            json.dump(dados, files, indent = 4)

            files.truncate()
            #ISNTANCIA DA CLASSE GENERATE, TAIS ARGUMENTOS DEVEM SER PASSADOS
            postagem = gerador(" "," ")
            post = postagem.newPost(pasta_nome_post, str(pasta_destino),categoria)
            if post:
                print('Feito') 
    
        except FileNotFoundError:
            print('Talvez o diretorio informado não exista.')    
      
    
 
