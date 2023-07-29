Para gerar migrations estamos usando a lib alembic.
comando para gerar, no terminal: alembic init migrations

Por questões de lembrar as configs, é necessário alterar o arquivo env.py dentro da pasta
migrations:
![Alt text](image.png)
<br>
E adicionar o Base com os metadatas de suas models:<br>
![Alt text](image-1.png)

<br>
Para gerar as migrations, basta executar no terminal o comando:<br>
alembic revision --autogenerate -m "add users table" <br>

O comando acima gera o script da migration, com o passo a passo para as models serem criadas no BD.<br>
Agora iremos executar o comando para realmente criar a tabela:
comando: alembic upgrade head
