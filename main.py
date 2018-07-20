from generate import gerador
import sys, json, datetime
if len(sys.argv) < 3:
    print('Insira argumentos validos por favor...\n\n')
    print('''Modo de usar:\nCRIAR UM NOVO PROJETO \t\t novo NOME_PROJETO\nCRIAR UM NOVO POST\t\tpost NOME_DO_POST PASTA_DO_PROJETO''')

else:
    
    #A OPCAO SERA O PRIMEIRO ARGUMENTO
    argumento = sys.argv[1]

    #SERA O SEGUNDO A PASTA OU NOME DO POST
    pasta_nome_post = sys.argv[2]


    if argumento.lower() == 'novo' and pasta_nome_post != " ":
        print("Tentando gerar arquivos...")

        #INSTANCIAMOS A CLASSE PASSANDO OS ARGUMENTOS
        projeto = gerador(argumento, pasta_nome_post + '/')

        #SE A RESPOSTA FOR TRUE
        if projeto:
            print('Feito')  
    if argumento.lower() == 'ajuda':
        print('''Modo de usar:\n\n CRIAR UM NOVO PROJETO \t\t novo NOME_PROJETO\nCRIAR UM NOVO POST\t\tpost NOME_DO_POST PASTA_DO_PROJETO''')
    #SE O ARGUMENTO FOR POST, O NOME DO POST DEVE SER PASSADO JUNTO A PASTA DO PROJETO  

        
    if argumento.lower() == 'post' and pasta_nome_post != " " and sys.argv[3] != " ":
        print("Gerando arquivos...")
        #PRIMEIRO SERA INSERIDO, O POST, NO JSON
        #ABERTURA DO ARQUIVO EM MODO ESCRITA/LEITURA
        pasta_destino = sys.argv[3]  
        try:
            files = open(str(pasta_destino) + '/data.json', 'r+')
             #LEITURA DO ARQUIVO
            leitura = files.read()
            #PASSANDO DE JSON PARA PARA ALGO QUE O PYTHON ENTENDA, GERALMENTE, LISTA, DICIONARIOS ETC.
            dados = json.loads(leitura)
                
            #INSTANCIA DA CLASS DATETIME
            agora = datetime.datetime.now()

            #ATRIBUIÇÃO DE UM NOVO POST COM DADOS GENERICOS
            dados[1]['posts'][pasta_nome_post] = {"title": "titulo do post", "Data": str(agora.day) + '/' + str(agora.month) + '/' + str(agora.year), "conteudo": "SEU CONTEUDO DEVE SER INSERIDO AQUI"}
                
            files.seek(0)

            #"OFICIALIZANDO" AS ALTERAÇOES DO JSON DANDO UM DUMP, NADA MAIS É DO QUE GERAR O NOVO BINARIO JSON
            json.dump(dados, files, indent = 4)

            files.truncate()
            #ISNTANCIA DA CLASSE GENERATE, TAIS ARGUMENTOS DEVEM SER PASSADOS
            postagem = gerador(" "," ")
            post = postagem.newPost(pasta_nome_post, str(pasta_destino))
            if post:
                print('Feito') 
    
        except FileNotFoundError:
            print('Talvez o diretorio informado não exista.')    
      
    
 