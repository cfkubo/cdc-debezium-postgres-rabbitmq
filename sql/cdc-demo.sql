drop table public.account_transactions;

CREATE TABLE public.account_transactions (
    transaction_id SERIAL PRIMARY KEY,
    account_number BIGINT NOT NULL,
    transaction_date DATE NOT NULL,
    transaction_type VARCHAR(20) NOT NULL, -- e.g., 'deposit', 'withdrawal', 'transfer'
    amount DECIMAL(10, 2) NOT NULL,
    balance DECIMAL(10, 2) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO public.account_transactions (account_number, transaction_date, transaction_type, amount, balance, description)
SELECT
    FLOOR(RANDOM() * (9999999999 - 1000000000) + 1000000000) AS account_number,
    CURRENT_DATE - INTERVAL '1 day' * FLOOR(RANDOM() * 365) AS transaction_date,
    CASE WHEN RANDOM() < 0.5 THEN 'deposit' ELSE 'withdrawal' END AS transaction_type,
    FLOOR(RANDOM() * 10000) / 100.00 AS amount,
    FLOOR(RANDOM() * 100000) / 100.00 AS balance,
    'Sample Transaction'
FROM generate_series(1, 10) AS i;

select * from  public.account_transactions;

drop table public.account_transactions;

INSERT INTO customers (id, first_name, last_name, email)
SELECT i,
'First_' || i,
'Last_' || i,
'first' || i || '.last' || i || '@example.com' AS email
FROM generate_series(1, 10) AS i;

CREATE USER arul WITH SUPERUSER PASSWORD 'password';

CREATE ROLE aruladmin WITH LOGIN SUPERUSER PASSWORD 'password';
