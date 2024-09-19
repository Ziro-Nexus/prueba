CREATE TABLE Inventory (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    price DECIMAL(10, 2),
    mac_address CHAR(17),
    serial_number VARCHAR(255),
    manufacturer VARCHAR(255),
    description TEXT
);


INSERT INTO Inventory (name, price, mac_address, serial_number, manufacturer, description)
VALUES 
('Laptop Pro 2049', 2599.99, '00:1B:44:11:3A:B7', 'SN123456789', 'TechCorp', 'High-end laptop with 16GB RAM, 1TB SSD, and an Intel i7 processor.'),

('Smartphone X', 999.99, '00:1A:22:33:44:AA', 'SN987654321', 'MobileTech', 'Latest smartphone with 128GB storage, 5G connectivity, and a 64MP camera.'),

('Gaming PC', 1999.99, '00:2F:34:67:89:DE', 'SN543216789', 'GameMasters', 'Powerful gaming PC with RTX 3090 GPU, 32GB RAM, and 2TB SSD.'),

('Wireless Headphones', 299.99, '00:0D:12:56:7C:4E', 'SN778899001', 'AudioCorp', 'Noise-cancelling wireless headphones with 30-hour battery life and quick charge feature.'),

('Smartwatch Z', 199.99, '00:9C:11:23:45:CD', 'SN567894321', 'WearTech', 'Smartwatch with heart-rate monitoring, GPS, and waterproof design for fitness tracking.');
