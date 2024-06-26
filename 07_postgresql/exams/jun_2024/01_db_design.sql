CREATE TABLE IF NOT EXISTS accounts (
	id SERIAL PRIMARY KEY,
	username VARCHAR(30) NOT NULL, 
	password VARCHAR(30) NOT NULL,
	email VARCHAR(50) NOT NULL,
	gender VARCHAR(1) NOT NULL,
	age INT NOT NULL,
	job_title VARCHAR(40) NOT NULL,
	ip VARCHAR(30) NOT NULL,
	
	-- UNIQUE USER NAMES
	CONSTRAINT unique_user
		UNIQUE (username),
	-- M or F for gender
	CONSTRAINT ck_two_genders_only
		CHECK (gender = 'F' or gender = 'M')
);

CREATE TABLE IF NOT EXISTS addresses (
	id SERIAL PRIMARY KEY,
	street VARCHAR(30) NOT NULL,
	town VARCHAR(30) NOT NULL,
	country VARCHAR(30) NOT NULL,
	account_id INT NOT NULL,

	CONSTRAINT fk_add_accounts
		FOREIGN KEY (account_id)
		REFERENCES accounts(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS photos (
	id SERIAL PRIMARY KEY,
	description TEXT,
	capture_date TIMESTAMP NOT NULL,
	views INT NOT NULL DEFAULT 0,

	CONSTRAINT ck_positive_views
		CHECK (views >= 0)
);

CREATE TABLE IF NOT EXISTS comments (
	id SERIAL PRIMARY KEY,
	content VARCHAR(255) NOT NULL,
	published_on TIMESTAMP NOT NULL,
	photo_id INT NOT NULL,

	CONSTRAINT fk_comments_photos
		FOREIGN KEY (photo_id)
		REFERENCES photos(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE
	
);


CREATE TABLE IF NOT EXISTS accounts_photos (
	account_id INT NOT NULL,
	photo_id INT NOT NULL,
    PRIMARY KEY (account_id, photo_id),
	
	CONSTRAINT fk_accounts_photos_accounts
		FOREIGN KEY (account_id)
		REFERENCES accounts(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	CONSTRAINT fk_accounts_photos_photos
		FOREIGN KEY (photo_id)
		REFERENCES photos(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE
	
);

CREATE TABLE IF NOT EXISTS likes (
	id SERIAL PRIMARY KEY,
	account_id INT NOT NULL,
	photo_id INT NOT NULL,
	
	CONSTRAINT fk_likes_accounts
		FOREIGN KEY (account_id)
		REFERENCES accounts(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	CONSTRAINT fk_likes_photos
		FOREIGN KEY (photo_id)
		REFERENCES photos(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

