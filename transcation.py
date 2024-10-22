from flask import Flask, render_template
import pika
import json
import configparser
import db_config
import os

config = configparser.ConfigParser()
config.read('config.py')
rabbitmq_host = db_config.rabbitmq_host
rabbitmq_port = db_config.rabbitmq_port
rabbitmq_user = db_config.rabbitmq_user
rabbitmq_password = db_config.rabbitmq_password # Handle potential errors
QUEUE_NAME = db_config.rabbitmq_queue

# Flask app setup
app = Flask(__name__)

def connect_rabbitmq():
    """Connects to RabbitMQ and returns a channel."""
    credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_password)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port, credentials=credentials)
    )

    channel = connection.channel()

    # channel.queue_declare(queue=QUEUE_NAME)
    return channel

def process_messages(channel):
    """
    Processes all available messages in the queue,
    extracts relevant data, and returns a list of dictionaries.
    """
    transactions = []
    while True:
        method, properties, body = channel.basic_get(QUEUE_NAME, auto_ack=False)
        if not body:
            break
        data = json.loads(body)
        payload = data.get("payload", {})
        after = payload.get("after", {})

        # Extract relevant data from after object
        transaction_id = after.get("transaction_id")
        account_number = after.get("account_number")
        transaction_date = after.get("transaction_date")
        transaction_type = after.get("transaction_type")
        amount = after.get("amount")
        balance = after.get("balance")
        description = after.get("description")

        # Build a dictionary for each transaction
        transaction_data = {
            "transaction_id": transaction_id,
            "account_number": account_number,
            "transaction_date": transaction_date,
            "transaction_type": transaction_type,
            "amount": amount,
            "balance": balance,
            "description": description
        }
        transactions.append(transaction_data)
        print("Heelooo")
        print(transaction_data)
        # channel.basic_nack(delivery_tag=method.delivery_tag, requeue=True)

    return transactions

@app.route("/")
def index():
    """
    Connects to RabbitMQ, retrieves all messages,
    processes them, and renders the HTML template with data.
    """
    channel = connect_rabbitmq()
    # channel.basic_nack(requeue=True)
    transactions = process_messages(channel)
    # channel.basic_nack(delivery_tag=method.delivery_tag, requeue=True)
    return render_template("index.html", transactions=transactions)
    return channel



if __name__ == "__main__":
    port = int(os.getenv("PORT", 8081))
    app.run(debug=True, host='0.0.0.0', port=port)
