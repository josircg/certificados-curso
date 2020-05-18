Este script gera certificados com os nomes indicados em um arquivo CSV e envia email para cada um deles. 

O arquivo CSV deve vir no formato Nome,Email (delimitado por vírgula).

O arquivo CSV também pode vir apenas com o nome (e nesse caso, não enviará o certificado por email). 

1 ) Instalação

    virtualenv -p python3 <path-venv>
    source <path-venv>/bin/activate
    pip install -r requirements.txt

2 ) Copie o arquivo '''alunos.csv''' e '''certificado.jpg''' para o diretório do script

3 ) Crie o arquivo local.py com os dados de login do SMTP:

    smtp = {
        'login': 'xxxx',
        'password': 'xxxx',
        'bcc': 'xxxx'
    }
    
    sender = 'PPGCI IBICT/UFRJ <ppgci@eco.ufrj.br>'
    subject = 'Seminário Internacional de Estudos Críticos em Informação'
    modelo = 'escritos.png'
    
    pos_x = 140
    pos_y = 440
    font_size = 24

4 ) Altere a posição x,y no script onde o nome do aluno deve aparecer.

5 ) Execute: python insert.py

Os certificados serão gravados na mesma pasta do script. O email só será enviado se o CSV tiver uma coluna com um email válido. 

###### A fazer

- Parâmetros para definir o arquivo csv e fazer um teste sem enviar o email ou para gerar um único certificado
- Parametrizar a posição do nome na imagem
