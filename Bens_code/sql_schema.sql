-- USER

CREATE TABLE cs361_condreab.User
(
  username VARCHAR(25) NOT NULL UNIQUE,
  email VARCHAR(25) NOT NULL UNIQUE,
  credentials VARCHAR(64) NOT NULL,
  PRIMARY KEY (username),
  CONSTRAINT user_info UNIQUE(username, email)
);

-- delete table
DROP TABLE cs361_condreab.User;

-- create an account
INSERT INTO cs361_condreab.User (username, email, credentials)
VALUES ('INSERT_USERNAME', 'INSERT_EMAIL', 'INSERT_PASSWORD')

-- update password
UPDATE cs361_condreab.User
SET Credentials = 'INSERT_HASH_HERE'
WHERE username = 'INSERT_USERNAME_HERE';

-- update email
UPDATE cs361_condreab.User
SET email = 'INSERT_EMAIL'
WHERE username = 'INSERT_USERNAME'

-- query User
SELECT username, credentials
FROM cs361_condreab.User
WHERE username = 'INSERT_USERNAME_HERE'
AND credentials = 'INSERT_HASH_HERE';

-- delete User
DELETE FROM cs361_condreab.User
WHERE username = 'USER_NAME'

IF EXISTS(
  SELECT 0 FROM cs361_condreab.User
  WHERE username = 'USERNAME'
)
SELECT 1
ELSE
SELECT 0

-- test
SELECT COUNT(*)
FROM cs361_condreab.User
WHERE username = 'condreab'

-- GAME
CREATE TABLE cs361_condreab.Game
(
  game_ID INT NOT NULL UNIQUE AUTO_INCREMENT,
  game_start_date DATETIME NOT NULL,
  game_save_date DATETIME NOT NULL,
  player_ID INT NOT NULL,
  username VARCHAR(25) NOT NULL,
  PRIMARY KEY (game_ID),
  FOREIGN KEY (player_ID) REFERENCES cs361_condreab.Player(player_ID),
  FOREIGN KEY (username) REFERENCES cs361_condreab.User(username)
);

ALTER TABLE cs361_condreab.Game
ADD FOREIGN KEY (player_ID) REFERENCES cs361_condreab.Player(player_ID);
ALTER TABLE cs361_condreab.Game
ADD FOREIGN KEY (username) REFERENCES cs361_condreab.User(username);



CREATE TABLE cs361_condreab.Room
(
  room_ID INT NOT NULL UNIQUE,
  x_coord INT NOT NULL,
  y_coord INT NOT NULL,
  short_description TEXT NOT NULL,
  long_description TEXT NOT NULL,
  next_level BOOLEAN NOT NULL,
  game_ID INT NOT NULL,
  north_room INT UNIQUE,
  east_room INT UNIQUE,
  south_room INT UNIQUE,
  west_room INT UNIQUE,
  PRIMARY KEY (room_ID),
  FOREIGN KEY (game_ID) REFERENCES cs361_condreab.Game(game_ID)
  FOREIGN KEY (north_room) REFERENCES cs361_condreab.Room(room_ID)
  FOREIGN KEY (east_room) REFERENCES cs361_condreab.Room(room_ID)
  FOREIGN KEY (south_room) REFERENCES cs361_condreab.Room(room_ID)
  FOREIGN KEY (west_room) REFERENCES cs361_condreab.Room(room_ID)
);

CREATE TABLE cs361_condreab.Player
(
  health INT NOT NULL,
  weapon INT NOT NULL,
  player_ID INT NOT NULL UNIQUE,
  room_ID INT NOT NULL,
  PRIMARY KEY (player_ID),
  FOREIGN KEY (weapon) REFERENCES cs361_condreab.Item(item_ID)
  FOREIGN KEY (room_ID) REFERENCES cs361_condreab.Room(room_ID)
);

CREATE TABLE cs361_condreab.Item
(
  item_ID INT NOT NULL UNIQUE,
  item_name VARCHAR(25) NOT NULL,
  item_description TEXT NOT NULL,
  item_type VARCHAR(25) NOT NULL,
  dmg_low INT,
  dmg_high INT,
  item_value INT,
  health_gain INT,
  use_count INT,
  player_ID INT,
  room_ID INT,
  animal_ID INT,
  PRIMARY KEY (item_ID),
  FOREIGN KEY (player_ID) REFERENCES cs361_condreab.Player(player_ID),
  FOREIGN KEY (room_ID) REFERENCES cs361_condreab.Room(room_ID),
  FOREIGN KEY (animal_ID) REFERENCES cs361_condreab.Animal(animal_ID)
);

CREATE TABLE cs361_condreab.Event
(
  event_value INT NOT NULL,
  event_description TEXT NOT NULL,
  event_ID INT NOT NULL UNIQUE,
  number_of_choices INT NOT NULL,
  event_name VARCHAR(25) NOT NULL,
  room_ID INT NOT NULL,
  PRIMARY KEY (event_ID),
  FOREIGN KEY (room_ID) REFERENCES cs361_condreab.Room(room_ID)
);

CREATE TABLE cs361_condreab.Character
(
  character_ID INT NOT NULL UNIQUE,
  character_name VARCHAR(25) NOT NULL,
  character_description TEXT NOT NULL,
  dialogue TEXT NOT NULL,
  trade_complete BOOLEAN NOT NULL,
  room_ID INT NOT NULL,
  offer_item_ID INT NOT NULL,
  want_item_ID INT NOT NULL,
  PRIMARY KEY (character_ID),
  FOREIGN KEY (room_ID) REFERENCES cs361_condreab.Room(room_ID),
  FOREIGN KEY (offer_item_ID) REFERENCES cs361_condreab.Item(item_ID),
  FOREIGN KEY (wanted_item_ID) REFERENCES cs361_condreab.Item(item_ID)
);

CREATE TABLE cs361_condreab.Animal
(
  animal_ID INT NOT NULL UNIQUE,
  animal_name VARCHAR(25) NOT NULL,
  animal_description TEXT NOT NULL,
  health INT NOT NULL,
  injure_chance FLOAT NOT NULL,
  damage INT NOT NULL,
  room_ID INT NOT NULL,
  PRIMARY KEY (animal_ID),
  FOREIGN KEY (room_ID) REFERENCES cs361_condreab.Room(room_ID)
);

-- CREATE TABLE cs361_condreab.connected
-- (
--   room_ID_1 INT NOT NULL,
--   room_ID_2 INT NOT NULL,
--   PRIMARY KEY (room_ID_1, room_ID_2),
--   FOREIGN KEY (room_ID_1) REFERENCES cs361_condreab.Room(room_ID),
--   FOREIGN KEY (room_ID_2) REFERENCES cs361_condreab.Room(room_ID)
-- );

CREATE TRIGGER `GameSaveInsert` BEFORE INSERT ON `Game`
 FOR EACH ROW BEGIN
SET NEW.game_save_date = NOW();
END

CREATE TRIGGER `GameSaveUpdate` BEFORE UPDATE ON `Game`
 FOR EACH ROW BEGIN
SET NEW.game_save_date = NOW();
END
