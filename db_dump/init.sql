CREATE TABLE Inventory (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    price DECIMAL(10, 2),
    mac_address CHAR(17),
    serial_number VARCHAR(255),
    manufacturer VARCHAR(255),
    description TEXT
);
