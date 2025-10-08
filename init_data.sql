INSERT INTO clients (name, address) VALUES
('Иван Иванов', 'Москва'),
('ООО Ромашка', 'Санкт-Петербург');

INSERT INTO categories (name, parent_id) VALUES
('Ноутбуки', NULL),
('Холодильники', NULL),
('Посудомоечные машины', NULL),
('Acer', 1),
('Lenovo', 1),
('однокамерные', 2),
('двухкамерные', 2);

INSERT INTO products (name, price, quantity, category_id) VALUES
('Ноутбук Acer', 60000.00, 100, 4),
('Холодильник однокамерный', 30000.00, 200, 6),
('Посудомойка', 12000.00, 150, 3);

INSERT INTO orders (client_id, created_at) VALUES
(1, NOW()),
(2, NOW());
