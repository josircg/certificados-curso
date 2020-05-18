Este script gera certificados com os nomes indicados em um arquivo CSV e envia email para cada um deles. 

1 ) Instalação

    virtualenv -p python3 <path-venv>
    source <path-venv>/bin/activate
    pip install -r requirements.txt

2 ) Crie o arquivo '''alunos.csv''' e '''certificado.jpg''' no mesmo diretório do script

O arquivo CSV deve vir no formato Nome,Email (delimitado por vírgula). 
O arquivo CSV também pode vir apenas com o nome mas nesse caso, a rotina não enviará o certificado por email. 

3 ) Crie o arquivo local.py com os dados de login do SMTP e dos dados específicos da sua organização:

    smtp = {
        'login': 'xxxx',
        'password': 'xxxx',
        'bcc': 'xxxx'
    }
    
    sender = 'PPGCI IBICT/UFRJ <ppgci@eco.ufrj.br>'
    subject = 'Seminário Internacional de Estudos Críticos em Informação'
    modelo = 'certificado.png'
    
    coluna = 140
    linha = 440
    font_size = 24

A parte mais "chata" da geração do certificado é posicionar o nome no modelo do certificado e gravar as posições em pixels no local.py 

Dicas: Para fazer testes com o posicionamento do nome no seu modelo de certificado, crie um arquivo alunos.csv com apenas o seu nome (sem o email) e rode o script até que o posicionamento fique do seu agrado.

4 ) Execute: python insert.py

Os certificados serão gravados na mesma pasta do script. O email só será enviado se o CSV tiver uma coluna com um email válido.

Este pequeno projeto foi criado durante o Seminário Internacional de Humanidades Digitais em 2019 promovido pelo LARHUD (http://larhud.ibict.br)
 

 

