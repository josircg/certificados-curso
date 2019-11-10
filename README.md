Este script gera certificados com os nomes indicados em um arquivo CSV e envia email para cada um deles: 

1 ) Instalação

    virtualenv -p python3 <path-venv>
    source <path-venv>/bin/activate
    pip install -r requirements.txt

2 ) Copie o arquivo '''alunos.csv''' e '''certificado.jpg''' para o diretório do script

3 ) Crie o arquivo local.py com os dados de login do SMTP:

    smtp = {
      'login': 'xxxx@gmail.com',
      'password': 'yyyy'
    }

4 ) Altere a posição x,y no script onde o nome do aluno deve aparecer.

5 ) Execute: python insert.py

Os certificados serão gravados na mesma pasta do script. O email só será enviado se o CSV tiver uma coluna com um email válido. 

###### A fazer

- Parâmetros para definir o arquivo csv e fazer um teste sem enviar o email ou para gerar um único certificado
- Parametrizar a posição do nome na imagem
