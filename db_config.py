# user = "system"
# password = "password"
# dsn = "dbi:Oracle:host=34.176.7.147;sid=xe;port=1521"
import os
import getpass

google_api_key = os.environ.get("google_api_key", "AIzaSyDixsFdhobHkb6mkKxXrMXnGmw0ELAIgAQ")
user = os.environ.get("PYTHON_USER", "arul")

# dsn = os.environ.get("PYTHON_CONNECT_STRING", "34.176.7.147:1521/XE")
dsn = os.environ.get("PYTHON_CONNECT_STRING", "34.176.7.147:1522/FREE")


pw = os.environ.get("PYTHON_PASSWORD", "password")
# if pw is None:
#     pw = getpass.getpass("Enter password for %s: " % user)

rabbitmq_host = os.environ.get("rabbitmq_host", '34.123.194.117')
rabbitmq_port = os.environ.get("rabbitmq_port", "5672")
rabbitmq_user = os.environ.get("rabbitmq_user", "arul")
rabbitmq_password = os.environ.get("rabbitmq_password", "password")
rabbitmq_queue = os.environ.get("rabbitmq_queue","inventory.transactions")

pg_host = os.environ.get("pg_host", "127.0.0.1")
pg_port = os.environ.get("pg_port", "5432")
pg_database = os.environ.get("pg_database","postgres")
pg_user = os.environ.get("pg_user", "postgres")
pg_password = os.environ.get("pg_password", "postgres")


MODEL = os.environ.get("MODEL", "llama3.1")
LLM_URL = os.environ.get("LLM_URL", "http://localhost:11434")
