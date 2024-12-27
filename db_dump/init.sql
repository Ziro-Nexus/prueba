CREATE TABLE Inventory (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    price DECIMAL(10, 2),
    mac_address CHAR(17),
    serial_number VARCHAR(255),
    manufacturer VARCHAR(255),
    description TEXT,
    container_id INT
);

CREATE TABLE `Container` (
  `container_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `status` varchar(45) NOT NULL,
  `from_warehouse` varchar(45) NOT NULL,
  `to_warehouse` varchar(45) NOT NULL,
  PRIMARY KEY (`container_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO Inventory (name, price, mac_address, serial_number, manufacturer, description)
VALUES 
('Laptop Pro 2049', 2599.99, '00:1B:44:11:3A:B7', 'SN123456789', 'TechCorp', 'High-end laptop with 16GB RAM, 1TB SSD, and an Intel i7 processor.'),

('Smartphone X', 999.99, '00:1A:22:33:44:AA', 'SN987654321', 'MobileTech', 'Latest smartphone with 128GB storage, 5G connectivity, and a 64MP camera.'),

('Gaming PC', 1999.99, '00:2F:34:67:89:DE', 'SN543216789', 'GameMasters', 'Powerful gaming PC with RTX 3090 GPU, 32GB RAM, and 2TB SSD.'),

('Wireless Headphones', 299.99, '00:0D:12:56:7C:4E', 'SN778899001', 'AudioCorp', 'Noise-cancelling wireless headphones with 30-hour battery life and quick charge feature.'),

('Smartwatch Z', 199.99, '00:9C:11:23:45:CD', 'SN567894321', 'WearTech', 'Smartwatch with heart-rate monitoring, GPS, and waterproof design for fitness tracking.');

INSERT INTO Inventory (name, price, mac_address, serial_number, manufacturer, description)
VALUES 
('4K Ultra HD TV', 1499.99, '00:1D:AA:BB:CC:DD', 'SN1029384756', 'VisionTech', '75-inch 4K Ultra HD TV with HDR, Smart TV features, and Dolby Atmos sound.'),

('Bluetooth Speaker', 129.99, '00:3E:54:67:89:12', 'SN2039485761', 'AudioPulse', 'Portable Bluetooth speaker with deep bass, 20-hour battery, and waterproof design.'),

('Tablet Plus', 799.99, '00:4A:21:76:54:88', 'SN9876504321', 'GigaDevices', '10-inch tablet with 256GB storage, quad-core processor, and stylus support.'),

('Gaming Console', 499.99, '00:5B:33:44:55:66', 'SN123454321', 'PlaySphere', 'Next-gen gaming console with 1TB storage, ray-tracing support, and 4K gaming.'),

('Smart Refrigerator', 2499.99, '00:6C:77:88:99:AA', 'SN6655443322', 'HomeSmart', 'Energy-efficient refrigerator with touchscreen, Wi-Fi connectivity, and voice control.'),

('Fitness Tracker', 149.99, '00:7D:88:99:AA:BB', 'SN5566778899', 'FitCorp', 'Lightweight fitness tracker with step counter, sleep analysis, and water resistance.'),

('Wireless Router', 199.99, '00:8E:12:34:56:78', 'SN2233445566', 'NetMax', 'High-speed Wi-Fi 6 router with dual-band support and advanced parental controls.'),

('Desktop Monitor', 299.99, '00:9F:65:43:21:98', 'SN7788991122', 'ScreenPro', '27-inch Full HD monitor with 144Hz refresh rate, 1ms response time, and IPS panel.'),

('Electric Scooter', 599.99, '00:AB:CD:EF:12:34', 'SN4455667788', 'EcoRide', 'Electric scooter with 25-mile range, 15mph top speed, and foldable design.'),

('Virtual Reality Headset', 499.99, '00:BC:DE:23:45:67', 'SN3344556677', 'VisionGames', 'Immersive VR headset with 4K resolution, 6DoF tracking, and ergonomic design.');

ALTER TABLE `Inventory`
  ADD CONSTRAINT `FK_Inventory_Container` FOREIGN KEY (`container_id`) REFERENCES `Container` (`container_id`) ON DELETE CASCADE ON UPDATE CASCADE;
