CREATE TABLE account (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    last_name VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    password VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE product (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    description TEXT,
    quantity INT,
    price NUMERIC(10, 2),
    tech_characteristics JSONB
);

INSERT INTO account (name, last_name, password, email) 
VALUES
('Amir', 'Zakov', 'zxcvb2009', 'amir.zakov@mail.ru'),
('Elya', 'Zakova', 'pandoralol', 'elvirazakova448@gmail.com');

INSERT INTO product (title, description, quantity, price, tech_characteristics) 
VALUES 
('Smartphone', 'High-end smartphone', 10, 699.99, '{"color": "black", "battery": "4000mAh"}'),
('Laptop', 'Gaming laptop', 5, 1299.99, '{"RAM": "16GB", "GPU": "RTX 3070"}');

DELETE FROM account;
DELETE FROM product;
DROP TABLE account;
DROP TABLE product;

DROP DATABASE db1;
DROP DATABASE db2;
DROP DATABASE db3;
DROP DATABASE db4;
DROP DATABASE db5;

CREATE DATABASE sql_test_db;

CREATE TABLE book (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    description VARCHAR(100),
    price INT,
    quantity INT,
    author VARCHAR(100),
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO book (title, description, price, quantity, author)
VALUES
('ponchik', 'pon', 123, 4, 'Amir'),
('ponchik1', 'pon1', 1234, 44, 'Amir Zakov'),
('ponchik2', 'pon2', 12345, 444, 'Amir Zakov :D');

SELECT * FROM book;

UPDATE book SET (title, description, price, quantity, author) = ('lol', 'lolikon', '54321', 555, 'Ne Amir Zakov :D') WHERE id=3;
