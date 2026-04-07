-- Demo database for data-agent-sql

CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    city TEXT,
    created_at TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    stock INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    total_price REAL NOT NULL,
    order_date TEXT DEFAULT (datetime('now')),
    status TEXT DEFAULT 'pending',
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Seed data
INSERT INTO customers (name, email, city) VALUES
    ('张三', 'zhangsan@example.com', '北京'),
    ('李四', 'lisi@example.com', '上海'),
    ('王五', 'wangwu@example.com', '广州'),
    ('赵六', 'zhaoliu@example.com', '深圳'),
    ('钱七', 'qianqi@example.com', '杭州');

INSERT INTO products (name, category, price, stock) VALUES
    ('笔记本电脑', '电子产品', 5999.00, 50),
    ('无线鼠标', '电子产品', 99.00, 200),
    ('机械键盘', '电子产品', 299.00, 150),
    ('运动鞋', '服装', 499.00, 80),
    ('T恤', '服装', 89.00, 300);

INSERT INTO orders (customer_id, product_id, quantity, total_price, status) VALUES
    (1, 1, 1, 5999.00, 'completed'),
    (1, 2, 2, 198.00, 'completed'),
    (2, 3, 1, 299.00, 'completed'),
    (3, 4, 2, 998.00, 'pending'),
    (4, 5, 5, 445.00, 'pending'),
    (5, 1, 1, 5999.00, 'completed'),
    (2, 4, 1, 499.00, 'shipped'),
    (3, 2, 3, 297.00, 'shipped');
