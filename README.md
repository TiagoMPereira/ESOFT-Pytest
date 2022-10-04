# pytest

[![PyTest CI](https://github.com/TiagoMPereira/pytest_C214/actions/workflows/CI_tests.yml/badge.svg)](https://github.com/TiagoMPereira/pytest_C214/actions/workflows/CI_tests.yml)

Repositório contendo a aplicação referente ao seminário de Engenharia de Software (2º semestre - 2022).

O pytest é uma ferramenta utilizada para criar e executar testes em python. Sua instalação, aplicação e execução são simples e serão descritas em passos posteriores.

<div align='center'>
<img src='img/pytest_img.png' width=250px></img>
</div>

---
## Clonando projeto
O primeiro passo para executar o projeto é cloná-lo na sua máquina. Para isso, abra o terminal de comando, navegue até o diretório onde deseja alocar o projeto e entre com o seguinte comando:  
```git clone https://github.com/TiagoMPereira/pytest_C214.git```  
Em seguida entre no diretório clonado  
```cd pytest_C214```  

---
## Gerência de dependências
No python a gerência de dependências é feita criando um ambiente virtual e especificando quais pacotes (e quais suas versões) serão utilizados no projeto. Para criar um ambiente virtual basta digitar o seguinte comando no terminal:  
```python -m venv env_projeto```  
Uma vez criado, é preciso ativar o ambiente virtual:  
```env_projeto\Scripts\activate.bat``` (Windows cmd)  
```env_projeto\Scripts\Activate.ps1``` (Windows powershell)  
```env_projeto/bin/activate``` (Linux/MacOS)  

Com o ambiente ativado basta importar as dependências:  
```pip install -r requirements.txt```  
Da mesma forma, é possível gerar o arquivo de dependências com todos os pacotes e versões utilizadas digitando:  
```pip freeze > requirements.txt```  

---
## Instalação
Caso o pytest não esteja nos requisitos instalados pelo requirements.txt é possível instalá-lo a parte.  

```pip install pytest```  


---
## Uso

Para utilizar o pytest basta criar um novo projeto python, qualquer IDE pode ser utilizada para tal.  
O pytest, ao ser executado, varre todo o projeto em busca de arquivos nomeados com test_*.py ou *_test.py. Portanto basta alocar os testes em arquivos que sigam tal nomeclatura que serão automaticamente executados.  
A estrutura utilizada no projeto será:  
|---*src/*  
|------*xxxx/*  
|---------*\_\_init\_\_.py*  
|---------*file1.py*  
|---------*file2.py*  
|---*tests/*  
|------*\_\_init\_\_.py*  
|------*func1/*  
|---------*\_\_init\_\_.py*  
|---------*test1.py*   
|------*func2/*  
|---------*\_\_init\_\_.py*  
|---------*test2.py*  
|---------*test3.py*  

Uma vez que os testes foram criados, basta executar o comando  
```pytest```  
e toda a suíte de testes será executada.

--- 
## Descrição do projeto
O projeto consiste na simulação de um elevador.

Foram implementadas as seguintes funcionalidades:

Para o elevador:
- Mover um andar -> Move um andar do elevador, baseado na posição atual.
- Mover -> É fornecido o andar desejado e executa a função de mover um andar até o destino.

Para o usuário:
- Chamar elevador -> Executa o mover do elevador até o andar que o usuário se encontra.

---
## Casos de teste
Arquivo test_elevador:
Teste 1 - Teste elevador em movimento:
    -> Verifica se o elevador esta em movimento
Teste 2 - Teste elevador andar inicial:
    -> Verifica se o elevador esta no andar inicial
Teste 3 - Teste elevador mover um andar:
    -> Verifica se o elevador moveu um andar
Teste 4 - Teste elevador mover andar final subir:
    -> Verifica se o elevador subiu a quantidade de andares que foi mandado
Teste 5 - Teste elevador mover andar final descer:
    -> Verifica se o elevador desceu a quantidade de andares que foi mandado
Teste 6 - Teste elevador mover andar final parado:
    -> Verifica se o elevador tem o status de parado apos mover
Teste 7 - Teste elevador andar inexistente:
    -> Verifica se o andar desejado é valido
Teste 8 - Teste elevador parada emergencial:
    -> Verifica se o elevador parou apos uma solicitacao de parada emergencial

Arquivo test_usuario:
Teste 1 - Teste cria usuario com id:
    -> Verifica se o usuario criado possui o id descrito
Teste 2 - Teste chama elevador:
    -> Verifica se o elevador parou no andar onde foi chamado

---
## CI
Foi adicionada ao repositório uma ação automática para executar toda a suíte de testes sempre que um push for dado em qualquer uma das branches.
