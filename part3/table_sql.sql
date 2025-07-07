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
