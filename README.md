# Static-Project

Esse projeto teve como objetivo a pritica de conceitos dentro de Javascript, HTML, CSS, Ajax e Python.
A proprosta do projeto e gerar paginas estáticas para o usuario da maneira mais "simples" possivel.

**DEMO** https://darkarmybrasil.github.io/
## CLASSE main:

Arquivo principal, portanto é por lá que a execução do programa inicia.
Essa classe é responsavel por receber as informações necessarias para a criação ou de um novo post ou de um novo projeto e passa-las para a classe gerador que é resposável pela criação de arquivos;
Variaveis:
argumento: recebe a opção de ação do usuario;
pasta_nome_post: variavel destinada a guardar ou o nome de uma pasta ou o nome de um post;
pasta_destino: variavel destinada a guardar o nome da pasta do projeto; 
files:  variavel destinada a guardar o arquivo JSON;
leitura:  variavel destinada a guardar a leitura do arquivo JSON, o retorno é uma string;
dados: variavel destinada a guardar novos dados a serem inseridos no JSON; 
postagem:  variavel destinada a guardar a instancia da classe gerador;
post:  variavel destinada a guardar o retorno do metodo newPost;
	
## CLASSE gerador:

Essa classe tem por finalidade criar de fato os arquivos. Para isso faz-se necessario a passagem de algumas informações importantes como os nomes dos arquivos.
## Variaveis:
Temp: é a instancia da classe hCSS, isso nos permitira ter acesso aos templates/caracteristicas dos nossos arquivos. 
HTML: variavel destinada a guardar o codigo HTML da pagina principal (index);
JAVAS: variavel destinada a guardar o codigo JavaScript da pagina principal (index): 
estiloCSS: variavel destinada a guardar o codigo CSS que será aplicado em todas as paginas existentes no projeto;
Json: variavel destinada a guardar o codigo primario do json;
conteudoH: variavel destinada a guardar o codigo das paginas secundarias,  denominadas posts;
conteudoJ: variavel destinada a guardar o codigo JavaScript que será implementado nas paginas secundarias, denominadas posts;

OBS: O SELF INDICA QUE A VARIAVEL PERTENCE A NOVA INSTANCIA. TODAS AS VARIAVEIS QUE CONTEM UM SELF SÃO VARIAVEIS “ÚNICAS”. ISSO SIGNIFICA QUE PARA CADA NOVA INSTANCIA HÁVERÃO NOVAS VARIAVES.
self.arg: variavel destinada a guardar o  argumento que vem da instancia da classe;
self.pasta: variavel destinada a guardar o nome da pasta do novo projeto;
self.dir: variavel destinada a guardar o caminho da pasta do novo projeto;
self.bootstrap: variavel destinada a guardar o caminho da pasta bootstrap
self.estilo: variavel destinada a guardar o caminho da pasta css
self.content:  variavel destinada a guardar o caminho da pasta onde ficarão os arquivos secundários;
self.nome_post:  variavel destinada a guardar o nome do novo arquivo secundários;
self.pasta_proj:  variavel destinada a guardar o nome da pasta principal do projeto;
self.post:  variavel destinada a guardar o objeto do arquivo;


## Metodos:
gerar_projeto: metodo que criará todos os arquivos base para o projeto tais como: pasta principal, bootstrap, JSON e arquivos do tipo Javascript;

newPost: metodo que criará o arquivo base para todo novo arquivo secundário;

## CLASSE template:

Essa classe que tem como unico objetivo guardar os textos base para a criação dos arquivos;
## Variaveis:
OBS: O SELF INDICA QUE A VARIAVEL PERTENCE A NOVA INSTANCIA. TODAS AS VARIAVEIS QUE CONTEM UM SELF SÃO VARIAVEIS “ÚNICAS”. ISSO SIGNIFICA QUE PARA CADA NOVA INSTANCIA HÁVERÃO NOVAS VARIAVES.
self.json:  variavel destinada a guardar o codigo JSON;
self.html: variavel destinada a guardar o codigo HTML da pagina primaria (index);
self.javaS: variavel destinada a guardar o codigo JavaScript da pagina primaria (index);
self.estilo: variavel destinada a guardar o codigo CSS;
self.post_html: variavel destinada a guardar o codigo HTML da paginas secundaria (posts);
self.javaS_post: variavel destinada a guardar o codigo JavaScript da paginas secundarias (posts);



# Funcionamento: 
## Criar um novo projeto:
```
python3 main.py novo nome_projeto
```
## Criar novos arquivos secundarios:
```
python3 main.py post nome_post nome_pasta_projeto categoria_post
```
PS:OS LINKS PRINCIPAIS DEVEM SER MANIPULADOS NO JSON E DEVEM TER O MESMO NOME DA CATEGORIA ESCOLHIDA
## Ajuda:
```
python3 main.py ou python3 main.py ajuda
```
## Todo o conteudo das paginas são tirados do arquivo data.json, portanto, qualquer alteração a ser feita no conteudo deve ser feita por lá a menos que a alteração seja de fato no design.

