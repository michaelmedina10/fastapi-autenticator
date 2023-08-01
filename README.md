### Objetivo

Objetivo desse projeto é testar o framework fastapi para o desenvolvimento de APIs, FastAPI vem sendo muito usado, devida
sua facilidade de implementação, possibilitando desenvolvimento de funções assíncronas nos endpoints, documentação praticamente automática.

### Execução

Para facilitar a execução desse projeto que faz uso de um banco de dados postgres, iremos fazer uso de documentos docker, para containerizar
nossa aplicação, a principio, a ideia era somente usá-la para o banco de dados, mas desenvolvi um dockerfile para a aplicação em si, logo, basta realizar um: <br>
comando: **git clone** <br>
Depois executar: **docker-compose up** ou **docker-compose up -d** para executar em modo daemon.

### Para lembrar

Para gerar migrations, estamos usando a lib alembic.
comando para gerar, no terminal: **alembic init migrations**

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
comando: **alembic upgrade head**
