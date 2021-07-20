# Este repositório contém: 





1. Um robô (webdriver) desenvolvido em Python com a biblioteca selenium, que faz login em uma conta no instagram, acessa o link de uma publicação passada pelo usuário, e sorteia 1 usuário dentre os usuários que comentaram a publicação.
2. O programa é vinculado a uma aplicação web desenvolvida com Flask, que serve de interface para o usuário inputar as informações necessárias para o programa rodar. 




#  Este repositório tem como finalidade:





1. Mostrar um pouco dos meus conhecimentos em Python e em todas as bibliotecas usadas neste programa.

2. Tentar contribuir com a comunidade compartilhando meus exemplos e experiências, e também me abrir para aprendizados e contribuições.

3. Servir como meu material de apoio para relembrar conceitos, sintaxes, bibliotecas e funções de todos os recursos que foram usados para construir este projeto.



# Neste repositório foram usadas as bibliotecas:





1. selenium
2. webdriver_manager - módulo chrome, função ChromeDriveManager
3. random
4. time - função sleep



# Para melhor explorá-lo, como principal sugestão, siga os passos abaixo:






1. Clone o repositório para o seu ambiente de desenvolvimento

2. Abra o terminal, caminhe até a pasta clonada do projeto. 

3. Na linha de comando, digite **pip3 install selenium --users** para instalar a biblioteca Requests

4. Na linha de comando, digite **pip3 install webdriver_manager --users** para instalar a biblioteca webdriver_manager, que contém o módulo chrome com a função ChromeDriveManager, que será utilizada para a automatização.

5. Certifique-se de você tem o Google Chrome instalado em seu computador

   

Após a instalação de todas as bibliotecas necessárias, vamos executar:



6. Veja bem, para este caso especifico você não precisará adicionar ao código do arquivo main.py um usuário e senha de uma conta no Instagram para acessar a publicação, mas se o robô fosse fazer qualquer acão dentro do Instagram, como comentar ou curtir algum post, você precisaria colocar estas informações no código. Caso queira realizar o teste com estas informações, siga os passos 7 e 8 abaixo. 

7. Com o usuário e senha em mãos, abra o arquivo funcoes.py contido dentro da pasta.

   

8. Nas linhas 29 e 30, existem os trechos de código

   - input_username.send_keys("**COLOQUE O USUARIO AQUI**"): substitua o trecho entre aspas "COLOQUE O USUARIO AQUI" pelo nome de usuário do Instagram que você usará.

   - input_password.send_keys("**COLOQUE A SENHA AQUI**"): substitua o trecho entre aspas "COLOQUE A SENHA AQUI" pela senha de usuário do Instagram que você usará 

     

9. Na linha de comando, ainda dentro da pasta do projeto, digite **python3 main.py**

   

10. Pronto, o programa será executado:
    - No terminal, o servidor será iniciado
    - Copie o código com o endereço "http://...." que será gerado no termial após a mensagem **"Running on http://.........."**
    - Cole este endereço em uma janela de navegador que não seja a aberta automaticamente pelo programa, pois é nela que você acompanhará os passos do robô até atingir o objetivo final: sortear um usuário. 
    - Na aba do Chrome aberta pelo programa, provavelmente aparecerá uma informação de que o navegador está controlado por um programa de teste automatizado.
    - Vá para a janela com a aplicação web gerada pelo servidor.
    - No campo "Insira a URL de uma postagem" cole a URL do post no instagram que você escolheu, lembrando que o post deve conter comentários de usuários. 
    - Em seguida, selecione a opção de vencedores que gostaria de obter e clique em "Selecionar vencedor"
    - Pronto, o robó começará a funcionar, vá para a janela aberta automaticamente pelo programa e veja o passo a passo sendo executado pelo programa para atingir o objetivo final. 
    - Quando o sorteio for feito, a aplicação web retornará uma página com o resultado. 



#  Como foram organizados os conteúdos:





O sistema é composto por 8 arquivos:

1. **main.py**: aqui está localizado o código principal, com as instruções lógicas das ações que serão realizadas através das funções e também com a inicialização do flask.
2. **funcoes.py**: aqui estão as funções cria_lista_usuarios_unicos (URL) e sorteia_usuario (lista_usuarios), que serão utilizadas no código principal para fazer o programa rodar. 
3. **Templates (diretorio)**: diretório onde estão contidas as páginas html da aplicação:
   -  **index.html:** página home da aplicação, onde o usuário fará o input dos dados necessários para a aplicação funcionar, neste caso, o link do post no instagram que terá usuários sorteados. 
   - **result.html:** página que retornará o output com o usuário sorteado. 

4. **README.md:** este arquivo com todas as orientações de como explorar o diretório e o programa. 
