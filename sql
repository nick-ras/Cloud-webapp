-- Assuming the table is already empty, or you've cleared it with DELETE FROM boxes;
CREATE TABLE boxes (
    id INT PRIMARY KEY IDENTITY(1,1),
    size INT NOT NULL CHECK (size IN (1, 2, 3)),
    location NVARCHAR(100) NOT NULL,
    in_use BIT NOT NULL DEFAULT 0,
    booked_until_interval15 DATETIME2 NULL,
    user_id INT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE users (
    id INT PRIMARY KEY IDENTITY(1,1),
    email NVARCHAR(100) NOT NULL UNIQUE,
    password NVARCHAR(100) NOT NULL,
    created_on DATETIME2 NOT NULL,
    is_admin BIT NOT NULL DEFAULT 0
);


INSERT INTO boxes (size, location) VALUES 
-- Size 1
(1, 'Tivoli Gardens'),
(1, 'Tivoli Gardens'),
(1, 'Nyhavn'),
(1, 'Nyhavn'),
(1, 'The Round Tower'),
(1, 'The Round Tower'),
(1, 'Strøget'),
(1, 'Strøget'),
(1, 'Frederik''s Church'),
(1, 'Frederik''s Church'),

-- Size 2
(2, 'Tivoli Gardens'),
(2, 'Tivoli Gardens'),
(2, 'Nyhavn'),
(2, 'Nyhavn'),
(2, 'The Round Tower'),
(2, 'The Round Tower'),
(2, 'Strøget'),
(2, 'Strøget'),
(2, 'Frederik''s Church'),
(2, 'Frederik''s Church'),

-- Size 3
(3, 'Tivoli Gardens'),
(3, 'Tivoli Gardens'),
(3, 'Nyhavn'),
(3, 'Nyhavn'),
(3, 'The Round Tower'),
(3, 'The Round Tower'),
(3, 'Strøget'),
(3, 'Strøget'),
(3, 'Frederik''s Church'),
(3, 'Frederik''s Church');
