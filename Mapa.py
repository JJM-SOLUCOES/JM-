Python 3.12.9 (tags/v3.12.9:fdb8142, Feb  4 2025, 15:27:58) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Imagem Interativa</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
            background-color: #f4f4f4;
        }
...         h1 {
...             text-align: center;
...         }
...         #descricao {
...             margin-top: 20px;
...             background-color: #e2e2e2;
...             padding: 10px;
...             border-radius: 5px;
...         }
...     </style>
... </head>
... <body>
... 
...     <h1>Imagem Interativa com Explicação</h1>
... 
...     <!-- Sua imagem (substitua 'imagem.jpg' pelo caminho da sua imagem) -->
...     <img src="imagem.jpg" alt="Imagem Interativa" usemap="#mapa" width="600">
... 
...     <!-- Definir as áreas clicáveis -->
...     <map name="mapa">
...         <!-- Ponto 1 - Área retangular -->
...         <area shape="rect" coords="50,50,150,150" href="#" alt="Ponto 1" onclick="mostrarDescricao('Ponto 1', 'Descrição do Ponto 1. Aqui vai a explicação sobre o ponto 1.')">
...         
...         <!-- Ponto 2 - Área circular -->
...         <area shape="circle" coords="400,100,50" href="#" alt="Ponto 2" onclick="mostrarDescricao('Ponto 2', 'Descrição do Ponto 2. Este é o ponto 2, que é interessante porque...')">
...         
...         <!-- Ponto 3 - Área poligonal -->
...         <area shape="poly" coords="300,200,350,250,400,200" href="#" alt="Ponto 3" onclick="mostrarDescricao('Ponto 3', 'Descrição do Ponto 3. Aqui está a explicação do ponto 3.')">
...     </map>
... 
...     <!-- Área para exibir a descrição -->
...     <div id="descricao">
...         <h3 id="tituloDescricao">Clique em um ponto para ver a descrição</h3>
...         <p id="textoDescricao">Aqui será exibida a descrição do ponto clicado.</p>
...     </div>
... 
...     <script>
...         // Função para exibir a descrição ao clicar em um ponto
        function mostrarDescricao(titulo, descricao) {
            const tituloDescricao = document.getElementById('tituloDescricao');
            const textoDescricao = document.getElementById('textoDescricao');
            tituloDescricao.textContent = titulo;
            textoDescricao.textContent = descricao;
        }
    </script>

</body>
