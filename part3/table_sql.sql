-- Table of user
CREATE TABLE IF NOT EXISTS users (
id CHAR(36) PRIMARY KEY NOT NULL,
first_name VARCHAR(255) NOT NULL,
last_name VARCHAR(255) NOT NULL,
email VARCHAR(255) NOT NULL UNIQUE,
password VARCHAR(255) NOT NULL,
is_admin BOOLEAN DEFAULT FALSE
);

-- Table of place
CREATE TABLE IF NOT EXISTS places (
id CHAR(36) PRIMARY KEY NOT NULL,
title VARCHAR(255) NOT NULL,
description TEXT,
price DECIMAL(10, 2),
latitude FLOAT NOT NULL,
longitude FLOAT NOT NULL,
owner_id CHAR(36) NOT NULL,
FOREIGN KEY (owner_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Table of review
CREATE TABLE IF NOT EXISTS reviews(
id CHAR(36) PRIMARY KEY NOT NULL,
text TEXT NOT NULL,
rating INT CHECK (rating BETWEEN 1 AND 5) NOT NULL,
user_id CHAR(36) NOT NULL,
place_id CHAR(36) NOT NULL,
FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
FOREIGN KEY (place_id) REFERENCES places(id) ON DELETE CASCADE
);

-- Table of amenity
CREATE TABLE IF NOT EXISTS amenities(
id CHAR(36) PRIMARY KEY NOT NULL,
name VARCHAR(255) UNIQUE NOT NULL
);

-- Table associative of amenity_place
CREATE TABLE IF NOT EXISTS amenity_place(
  place_id CHAR(36) NOT NULL,
    amenity_id CHAR(36) NOT NULL,
    PRIMARY KEY (place_id, amenity_id),
    FOREIGN KEY (place_id) REFERENCES places(id) ON DELETE CASCADE,
    FOREIGN KEY (amenity_id) REFERENCES amenities(id) ON DELETE CASCADE
);

INSERT INTO users (id, email, first_name, last_name, password, is_admin)
VALUES ('36c9050e-ddd3-4c3b-9731-9f487208bbc1',
'admin@hbnb.io', 'Admin', 'HBnB',
'$2b$12$Q8m3vwkZfAcPZy8LQbtiAeVwR8/MtcyR7RZxTGoSCMMBhS1uUvTX6',
True);

INSERT INTO amenities (id, name) VALUES 
('b01b0d1b-7bcb-49f3-b965-ee466b4582d7', 'Swimming Pool'),
('919ada95-ef6f-4611-84ab-2db7a33e3cb9', 'WiFi'),
('69f81034-872b-4ef7-bb9e-97a07f298881', 'Air Conditioning');