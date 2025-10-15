-- SQLite
SELECT * FROM product;

drop TABLE product;

CREATE TABLE product(
    code integer PRIMARY KEY AUTOINCREMENT,
    name char(100),
    price integer DEFAULT 0 
);

INSERT INTO product(name, price)
VALUES('LG세탁기',25000000);
INSERT INTO product(name, price)
VALUES('삼성세탁기',30000000);