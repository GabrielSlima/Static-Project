class hCSS():
    def __init__(self):
        
        self.json = '''[
    {
        "nome_site":"Nome do site",
        "links_menu":{"link1":"Exemplo", "link2":"exemplo", "link3":"exemplo"}
    },
    {
        "posts":{
                    "Titulo":{"title":"titulo","categoria": "categ", "Data":"xx/xx", "Conteudo":"Pode ser que der merda, ou nao"}
                }
    }
]
'''
        
        self.html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="bootstrap/css/estilo.css">
    <title class="titulo"></title>
</head>
<body>
 <nav class="nav navbar-light bg-light navbar-fixed-top navbar-expand-lg">
        <a href="index.html" class="navbar-brand nome_site logo" id="nome" onclick="home()">TESTE</a>
        <button type="button" class="navbar-toggler collapsed" data-toggle="collapse" data-target="#navegacao">
            <span class="navbar-toggler-icon"></span>
        </button>        
        <div class="collapse navbar-collapse menu" id="navegacao">
            <ul class="navbar-nav mr-auto mt-2 mt-lg-0 " id="menu">
                <!-- LINKS PRINCIPAIS CARREGADOS AQUI -->
            </ul>

        </div>
        
    </nav>  
<!--FIM MENU-->

    <div class="container">
        <div class="row">
           
            
            <div class="col-md-12 area" id="area">
             <!-- AQUI SERÃO CARREGADOS OS POSTS -->
            
            </div><!--AREA-->
            
        </div><!--ROW-->
    </div><!--CONTAINER-->
<footer class="page-footer blue border-top col-md-12">
                CopyRight&copy<span class="nome_site"></span>
            </footer><!--RODAPE-->
    <script src="java.js"></script>
</body>
</html>
 <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

    <script src="bootstrap/js/bootstrap.min.js"></script>






'''     
        self.javaS = ''' 
//CRIANDO UM OBJETO PARA A NOVA REQUISIÇÃO
var requisicao = new XMLHttpRequest();

//PREPARANDO A NOVA REQUISICAO, METODO GET, NA URL JJ/data.json, COM ASSINCRONISMO ATIVADO
requisicao.open('GET', 'data.json', true);

//AO CARREGAR A REQUISICAO ATIVAR A FUNÇAO
requisicao.onload = function(){
        //DADOS RETORNADOS DA REQUISICAO
        var dados = JSON.parse(requisicao.responseText);
        console.log(dados);
        //TITULO RETIRADO DA CHAVE nome_site
        var titulo = dados[0]['nome_site'];

        //LINKS DO MENU PRINCIPAL RETIRADOS DA CHAVE links_menu
        var links_principais = dados[0]['links_menu'];
        console.log(links_principais);
       

        //PARA CADA DA CHAVE links_principais
        for(var i in links_principais){
            console.log(i);
            //ADD OS LIKNS DO MENU PRINCIPAL
            document.getElementById('menu').innerHTML += '<a href="conteudo/' + links_principais[i].toString().toLowerCase() + '/' + links_principais[i].toLowerCase()  + '.html" >' + links_principais[i].toString() + '</a>';
        }


        //POSTS RETIRADOS DO SEGUNDO OBJETO DOS DADOS
        sei = dados[1]['posts'];
        console.log(sei);
        //PARA CADA VALOR DO DICIONARIO dados
        for(var i in sei){

            //BUSCAMOS UM ELEMENTO COM O ID ATUAL
            var elemento = document.getElementById(i);
            console.log(i);
            
            var alt = sei[i]['categoria'];
            console.log(alt);
            //SE O ELEMENTO NAO EXISTIR, OU SEJA, NULO
            if(elemento == null){

                //ADICIONA-LO NO CAMPO AREA SOMADO AO QUE JA EXISTE
                document.getElementById('area').innerHTML += '<a onclick=pegarValor("'+ i.toString() + ',' + alt.toString() +'")' + ' alt="' + alt.toString() + '">' + i.toString() + '</a><br><span>' +sei[i]["Data"].toString()+'<br><br>';            
            }
            
        }
         //BUSCA POR ELEMENTOS NO HTML QUE CONTEM UMA CLASSE nome_site
         var nomes = document.getElementsByClassName('nome_site');
         
    try{         
         //PARA CADA VALOR DA LISTA RETORNADA
         for(var i = 0; i <= nomes.length; i++){
 
             //SERA ADICIONADO O TIULO EM FORMATO DE STRING
             nomes[i].innerHTML = titulo.toString();
         }
        }
    catch(err)
    {
        console.log('Ocorreu algum erro...');
    }
    };
//FAZER A REQUISICAO DE FATO    
requisicao.send(null);
function pegarValor(valor, categoria)
{
    seila = valor.split(',');
    console.log(seila);
    valor = seila[0];
    categoria = seila[1];
  
    console.log(valor.toString());
    console.log('*****************');
    console.log(categoria);
    window.location = "conteudo/"+ categoria + "/"+valor+".html?valor="+valor;
 
}

'''  
        self.estilo = '''.menu a
        {
          
            padding: 20px;
            border-radius: 10%;
            text-decoration: none;
            margin: 0 .5em;
            color: grey;
            transition: 1s;
        }
        .menu a:hover
        {
            
            color: black;
        }
        .area 
        {
            text-align: left;
        }
        .area a 
        {
            color: grey;
            text-decoration: none;
            transition: 1s;
            font-size: 1.5em;
        }
        .area a:hover
        {
            cursor: all-scroll;
            color: black;
        } 
        .page-footer
        {
            /* position:fixed; */
            bottom:0;
            /* border-top:  grey solid; */
            padding: 1em;
            
        }
        #nome
        {
            color: black;
            transition: 1s;
        }
        #nome:hover
        {
            cursor: all-scroll;
            color: grey;
        }
.logo
{
    display:block;
    height: 40px;
    margin-top: 10px;
    margin-left: 10px;
}
.thumb
{
    display:block;
    margin-left: auto;
    margin-right: auto;
}
footer
{
    background: #f8f9fa;
}
''' 

        self.post_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="../../bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="../../bootstrap/css/estilo.css">
    <title class="titulo"></title>
</head>
<body>
 <nav class="nav navbar-light bg-light navbar-fixed-top navbar-expand-lg">
        <a href="index.html" class="navbar-brand nome_site logo" id="nome" onclick="home()">TESTE</a>
        <button type="button" class="navbar-toggler collapsed" data-toggle="collapse" data-target="#navegacao">
            <span class="navbar-toggler-icon"></span>
        </button>        
        <div class="collapse navbar-collapse menu" id="navegacao">
            <ul class="navbar-nav mr-auto mt-2 mt-lg-0 " id="menu">
                <!-- LINKS PRINCIPAIS CARREGADOS AQUI -->
            </ul>

        </div>
        
    </nav>  

    <div class="container">
        <div class="row">
          <div class="page-header"> 
            <h1 id="nome_post"></h1>
            <p class="lead" id="data"></p>
          </div>
          <hr class="col-md-12">
            <div class="col-md-12 area" id="area">
             <!-- AQUI SERÃO CARREGADOS OS POSTS -->
            
            </div><!--AREA-->

            
            
            
        </div><!--ROW-->
    </div><!--CONTAINER-->
<footer class="page-footer blue border-top col-md-12">
                CopyRight&copy<span class="nome_site"></span>
            </footer><!--RODAPE-->
    <script src="../js_post.js"></script>
</body>
</html>'''          
        self.javaS_post = ''' 
function lerURL(string)
{
    var parametros = false;
    //GUARDA, A PARTIR DO PONTO DE INTERROGAÇÃO, A STRING DO INTERVALOR 1 ATÉ O INTERVALO DO TAMANHO DA STRING APOS O "?"
    var local = location.search.substring(1, location.search.length);
    var valor_parametro = false;
    
    //PEGA A STRING LOCAL E TRANSFORMA EM  LISTA
    var parametros = local.split('&');
    
    
    //FAZEMOS UM LOOPING PERCORRENDO A LISTA
    for(var i =0; i < parametros.length; i++)
    {

        nome_parametro = parametros[i].substring(0, parametros[i].indexOf('='));
        if(nome_parametro == string)
        {
            valor_parametro = parametros[i].substring(parametros[i].indexOf('=')+1);
        }
    }

    if(valor_parametro)
    {
        return valor_parametro;
    }
    else
    {
        return undefined;
    }        
    
}

var valor = lerURL('valor');

var objeto = new XMLHttpRequest();
objeto.open('GET', '../../data.json', true);
objeto.onload = function()
{
    var resposta = JSON.parse(objeto.responseText);
    var titulos = resposta[0]['nome_site'];
    var titulo_post = resposta[1]['posts'][valor]['title'];
    var post = resposta[1]['posts'][valor]['conteudo'];
    var data = resposta[1]['posts'][valor]['Data'];
    var menu_links = resposta[0]['links_menu'];
    for(i in menu_links)
    {
        document.getElementById('menu').innerHTML += "<a href=" + menu_links[i].toString().toLowerCase()+ ".html>" + menu_links[i].toString() + "</a>";
    }    
    var nomes = document.getElementsByClassName('nome_site');
    for(var i =0; i < nomes.length; i++)
    {
        nomes[i].innerHTML = titulos.toString();    
    }
    
    document.getElementById('nome_post').innerHTML = titulo_post.toString();
    document.getElementById('data').innerHTML = data.toString();
    //PREENCHIMENTO DO POST
    document.getElementById('area').innerHTML = post.toString();
      
};

objeto.send(null);

function home()
{
    window.location = "../../index.html";
}
'''  
        self.diretorio_list_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="../../bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="../../bootstrap/css/estilo.css">
    <title class="titulo"></title>
</head>
<body>
 <nav class="nav navbar-light bg-light navbar-fixed-top navbar-expand-lg">
        <a href="index.html" class="navbar-brand nome_site logo" id="nome" onclick="home()">TESTE</a>
        <button type="button" class="navbar-toggler collapsed" data-toggle="collapse" data-target="#navegacao">
            <span class="navbar-toggler-icon"></span>
        </button>        
        <div class="collapse navbar-collapse menu" id="navegacao">
            <ul class="navbar-nav mr-auto mt-2 mt-lg-0 " id="menu">
                <!-- LINKS PRINCIPAIS CARREGADOS AQUI -->
            </ul>

        </div>
        
    </nav>  

    <div class="container">
        <div class="row">
          <div class="page-header"> 
            <h1 id="">Items relacionados: </h1>
          </div>
          <hr class="col-md-12">
            <div class="col-md-12 area" id="area">
             <!-- AQUI SERÃO CARREGADOS OS ITEMS -->
            
            </div><!--AREA-->

            
            
            
        </div><!--ROW-->
    </div><!--CONTAINER-->
<footer class="page-footer blue border-top col-md-12">
                CopyRight&copy<span class="nome_site"></span>
            </footer><!--RODAPE-->
    <script src="../dir_list.js"></script>
</body>
</html> 
'''

    
        self.diretorio_list_js = ''' var objeto = new XMLHttpRequest();
objeto.open('GET', '../../data.json', true);

objeto.onload = function()
{
    console.log('asdasdasd');
    var resposta = JSON.parse(objeto.responseText);
    console.log(resposta[0]);
    var titulos = resposta[0]['nome_site'];
    console.log(titulos);
    var items = resposta[1]['posts'];
    var menu_links = resposta[0]['links_menu'];
    for(i in menu_links)
    {
        document.getElementById('menu').innerHTML += "<a href=" + menu_links[i].toString().toLowerCase() + ".html>" + menu_links[i].toString() + "</a>";
    }    
    
    //LENDO A URL PARA PEGAR O NOME DA CATEGORIA ATUAL
    var link = /\w+.html/;
    var local = window.location.toString();
    var resultado = local.match(link).toString();
    console.log(local, resultado);

    var catName = resultado.substring(0, resultado.indexOf('.'));
    console.log(catName);
    console.log(" ");
    
     for(var i in items)
    {
        //console.log(i);
        if(items[i]['categoria'] == catName)
        {
            var alt = items[i]['categoria'];
            console.log('asdasd');
            document.getElementById('area').innerHTML += '<a onclick=pegarValor("'+ i.toString() + '")' + ' alt="' + alt.toString() + '">' + i.toString() + '</a><br><span>' +items[i]["Data"].toString()+'<br><br>'; 
        }
    }
    var nomes = document.getElementsByClassName('nome_site');
             
    try{         
         //PARA CADA VALOR DA LISTA RETORNADA
         for(var i = 0; i < nomes.length; i++){
 
             //SERA ADICIONADO O TIULO EM FORMATO DE STRING
             nomes[i].innerHTML = titulos.toString();
         }
        }

    catch(err)
    {
        console.log('Ocorreu algum erro...');
    }
    
   
    //PREENCHIMENTO COM OS ITEMS RELACIONADOS
    //document.getElementById('area').innerHTML = post.toString();
      
}; 

objeto.send(null);
console.log('asdasd');
function pegarValor(valor)
{
    window.location = valor+".html?valor="+valor;
 
}

function home()
{
    window.location = "../../index.html";
}
'''
    
