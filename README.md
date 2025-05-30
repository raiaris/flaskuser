# Documentação do Projeto

## Requisitos

Antes de iniciar, certifique-se de ter os seguintes requisitos instalados:

- Python 3.x
- pip (gerenciador de pacotes do Python)
- Virtualenv (opcional, mas recomendado)
- [Flask](https://flask.palletsprojects.com/)
- [Flask-Migrate](https://flask-migrate.readthedocs.io/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)

Você pode instalar as dependências do projeto utilizando o arquivo `requirements.txt`:


## Instalação de Dependências

Execute o comando abaixo para instalar as dependências do projeto:

```bash
pip install -r requirements.txt
```

---

## Inicializando o Banco de Dados com Flask-Migrate

Siga os passos abaixo para configurar e iniciar o banco de dados localmente utilizando o Flask-Migrate:

1. **Abra o terminal na raiz do projeto.**

2. **Inicialize o diretório de migrações (apenas na primeira vez):**
   ```bash
   flask db init
   ```

3. **Gere um arquivo de migração com base nas alterações do modelo:**
   ```bash
   flask db migrate -m "Mensagem descritiva da migração"
   ```

4. **Aplique as migrações ao banco de dados:**
   ```bash
   flask db upgrade
   ```

Esses comandos irão criar as tabelas e estruturas necessárias no banco de dados definido na configuração do seu projeto Flask.

---

## Observações

- Certifique-se de que as variáveis de ambiente necessárias (como `FLASK_APP`) estejam configuradas antes de executar os comandos acima.
- Para mais informações, consulte a [documentação oficial do Flask-Migrate](https://flask-migrate.readthedocs.io/).
- Os metodos estao documentados no localhost, utilizando o swagger para facilitar o teste