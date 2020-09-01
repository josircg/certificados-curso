Este script gera certificados com os nomes indicados em um arquivo CSV e envia email para cada um deles. 

1 ) Instalação

    virtualenv -p python3 <path-venv>
    source <path-venv>/bin/activate
    pip install -r requirements.txt

2 ) Crie o arquivo '''alunos.csv''' e '''certificado.png''' no mesmo diretório do script

O arquivo CSV deve vir no formato Nome,Email (delimitado por vírgula). 
O arquivo CSV também pode vir apenas com o nome mas nesse caso, a rotina não enviará o certificado por email. 

3 ) Se você só tenha o modelo em PDF, use o script util para converter para .png:

    python util.py convert_pdf <nome do arquivo>

4 ) Crie o arquivo local.py com os dados de login do SMTP e dos dados específicos da sua organização:

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

5 ) Caso existam emails duplicados no seu arquivo CSV, utilize o script para remover os duplicados:

    python util.py remove_duplic <arquivo csv> 
    
IMPORTANTE: O sistema gera um arquivo novo com o nome alunos.csv.

6 ) Execute: python insert.py alunos.csv

Os certificados serão gravados na mesma pasta do script. O email só será enviado se o CSV tiver uma coluna com um email válido.

Este pequeno projeto foi criado durante o Seminário Internacional de Humanidades Digitais em 2019 promovido pelo LARHUD (http://larhud.ibict.br)
 
RESUMO DA OPERAÇÃO:

A partir do PDF e de um CSV com os nomes e emails dos participantes:

1) Converta o PDF do modelo: python util.py convert_pdf <pdf>
2) Altere o local.py para incluir o título do email, a imagem que será utilizada e o posicionamento do nome
3) Teste a rotina com: python insert.py teste2.csvpy 
4) Entre no seu email para verificar se a rotina foi bem sucedida
5) Remova os emails duplicados: python util.py remove_duplic <csv>
6) Execute pra valer: python insert.py alunos.csv
