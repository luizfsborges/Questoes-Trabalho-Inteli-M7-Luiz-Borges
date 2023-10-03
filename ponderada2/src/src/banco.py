import psycopg2
from psycopg2 import sql
from psycopg2.extras import DictCursor
import docker
import time

class Banco:
    def __init__(self, dbname, user, password, host='localhost', port=5432):
        self._start_postgresql_container()
        self._wait_for_postgresql()
        
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cursor = self.conn.cursor(cursor_factory=DictCursor)

    def _start_postgresql_container(self):
        client = docker.from_env()
        try:
            # Attempt to find an existing container
            container = client.containers.get('postgres-container')
            if container.status == 'running':
                print("PostgreSQL container is already running.")
                return
        except docker.errors.NotFound:
            pass

        # If not found, start a new PostgreSQL container
        print("Starting PostgreSQL container...")
        client.containers.run(
            'postgres:latest',
            name='postgres-container',
            detach=True,
            ports={'5432/tcp': 5432},
            environment={
                'POSTGRES_USER': 'your_username',
                'POSTGRES_PASSWORD': 'your_password',
                'POSTGRES_DB': 'notes_db'
            }
        )

    def _wait_for_postgresql(self, max_retries=30, retry_interval=1):
        for _ in range(max_retries):
            try:
                psycopg2.connect(
                    dbname='notes_db',
                    user='your_username',
                    password='your_password',
                    host='localhost',
                    port=5432
                )
                print("PostgreSQL is ready.")
                return
            except psycopg2.OperationalError as e:
                print(f"Waiting for PostgreSQL: {e}")
                time.sleep(retry_interval)

        raise Exception("Timed out waiting for PostgreSQL to start.")

    def criar_tabela_notas(self):
        query = """
            CREATE TABLE IF NOT EXISTS notas (
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                content TEXT NOT NULL
            );
        """
        self.cursor.execute(query)
        self.conn.commit()

    def adicionar_nota(self, title, content):
        query = """
            INSERT INTO notas (title, content) VALUES (%s, %s);
        """
        self.cursor.execute(query, (title, content))
        self.conn.commit()

    def obter_notas(self):
        query = "SELECT * FROM notas;"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def editar_nota(self, note_id, title, content):
        query = "UPDATE notas SET title=%s, content=%s WHERE id=%s;"
        self.cursor.execute(query, (title, content, note_id))
        self.conn.commit()

    def deletar_nota(self, note_id):
        query = "DELETE FROM notas WHERE id=%s;"
        self.cursor.execute(query, (note_id,))
        self.conn.commit()

    def fechar_conexao(self):
        self.cursor.close()
        self.conn.close()