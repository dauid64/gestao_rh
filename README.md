# Gestão de RH

> Projeto com foco em se aprofundar em algumas funcionalidades avançadas do Django se baseando em um sistema de RH.

## 🤓 Aprendizados
- Organização - Dividindo as apps na pasta "apps" para centraliza-las.

- Class Based View - CRUD completos utilizando as classes genéricas que o Django fornece para facilitar a implementação e limpeza do código, além de sobscrever métodos para se torna adpativo aos requisitos de qualquer aplicação.

- Deploy - utilizei uWSGI e Nginx para fazer deploy em qualquer plataforma de cloud computing (AWS, google cloud, etc.), não conseguindo manter ativo por questões de custos.

- Ajax - Usei ajax para tornar mais dinâmica a página e não precisar de carregamentos em algumas opções como tornar um select dinâmico ou ativar/desativar algum campo de um model utilizando request Ajax.

- Relatórios - Download de PDF, CSV e Excel de informações do banco para criação de relatórios.

- API REST - Criação de alguns simples endpoints para compartilhamento de dados da aplicação.

- Celery - Uma das partes mais divertidas que foi a utilização do Celery para envio de e-mail assíncrono e também agendamento de tarefas com o Celery Beat.

- Multiplos DB - Configuração das rotas para utilização de vários banco de dados em uma só aplicação.

- Traduções - Utilizei o sistema de traduções do Django para traduzir a aplicação para português, inglês e espanhol.

## 🚀 Instalando Gestao RH

1) Na pasta main do projeto que é chamada "gestao_rh" crie um arquivo chamado local_settings e crie as suas configurações de banco de dados, E-mail e Celery url

2) Linux e macOS:
    ```
        python -m venv nome_do_ambiente
        nome_do_ambiente/bin/activate
        pip install -r requirements.txt
        python manage.py makemigrations
        python manage.py migrate
    ```
    Windows:
    ```
        python -m venv nome_do_ambiente
        nome_do_ambiente/Scipts/activate
        pip install -r requirements.txt
        python manage.py makemigrations
        python manage.py migrate
    ```

3) inicie o projeto com 
    ```
        python manage.py runserver
    ```