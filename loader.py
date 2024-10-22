import psycopg2
import time

def run_query():
    conn = psycopg2.connect("dbname=postgres_db user=pgrwuser password=158mUK5lNw41Pjk2Fm3EuGIKdF5s0q host=XXXXXXXXXXXX port=5432")
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO public.account_transactions (account_number, transaction_date, transaction_type, amount, balance, description)
        SELECT 
            FLOOR(RANDOM() * (9999999999 - 1000000000) + 1000000000) AS account_number,
            CURRENT_DATE - INTERVAL '1 day' * FLOOR(RANDOM() * 365) AS transaction_date,
            CASE WHEN RANDOM() < 0.5 THEN 'deposit' ELSE 'withdrawal' END AS transaction_type,
            FLOOR(RANDOM() * 10000) / 100.00 AS amount,
            FLOOR(RANDOM() * 100000) / 100.00 AS balance,
            'Sample Transaction'
        FROM generate_series(1, 10) AS i;
    """)
    conn.commit()
    cur.close()
    conn.close()

while True:
    run_query()
    time.sleep(5)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(debug=True, host='0.0.0.0', port=port)
