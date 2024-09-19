CREATE TABLE Inventory (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    mac_address CHAR(17) NOT NULL,
    serial_number VARCHAR(255) NOT NULL,
    manufacturer VARCHAR(255),
    description TEXT
);
