-- Assuming the table is already empty, or you've cleared it with DELETE FROM boxes;

CREATE TABLE [dbo].[users] (
    id INT PRIMARY KEY IDENTITY(1,1),
    email NVARCHAR(100) NOT NULL UNIQUE,
    password NVARCHAR(100) NOT NULL,
    created_on DATETIME2 NOT NULL,
    is_admin BIT NOT NULL DEFAULT 0
);


CREATE TABLE [dbo].[boxes] (
    id INT PRIMARY KEY IDENTITY(1,1),
    size INT NOT NULL CHECK (size IN (1, 2, 3)),
    location NVARCHAR(100) NOT NULL,
    in_use BIT NOT NULL DEFAULT 0,
    booked_until_interval15 DATETIME2 NULL,
    user_id INT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO [dbo].[boxes] (size, location) VALUES 
-- Size 1INSERT INTO [dbo].[boxes] (size, location, in_use) VALUES 
(1, 'Tivoli Gardens', 0),
(1, 'Tivoli Gardens', 0),
(1, 'Nyhavn', 0),
(1, 'Nyhavn', 0),
(1, 'The Round Tower', 0),
(1, 'The Round Tower', 0),
(1, 'Strøget', 0),
(1, 'Strøget', 0),
(1, 'Frederik''s Church', 0),
(1, 'Frederik''s Church', 0),

-- Size 2
(2, 'Tivoli Gardens', 0),
(2, 'Tivoli Gardens', 0),
(2, 'Nyhavn', 0),
(2, 'Nyhavn', 0),
(2, 'The Round Tower', 0),
(2, 'The Round Tower', 0),
(2, 'Strøget', 0),
(2, 'Strøget', 0),
(2, 'Frederik''s Church', 0),
(2, 'Frederik''s Church', 0),

-- Size 3
(3, 'Tivoli Gardens', 0),
(3, 'Tivoli Gardens', 0),
(3, 'Nyhavn', 0),
(3, 'Nyhavn', 0),
(3, 'The Round Tower', 0),
(3, 'The Round Tower', 0),
(3, 'Strøget', 0),
(3, 'Strøget', 0),
(3, 'Frederik''s Church', 0),
(3, 'Frederik''s Church', 0);