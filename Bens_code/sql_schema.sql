CREATE TABLE cs361_condreab.User
(
  username varchar(25) NOT NULL UNIQUE,
  email varchar(25) NOT NULL UNIQUE,
  credentials varchar(64) NOT NULL,
  PRIMARY KEY (username),
  CONSTRAINT user_info UNIQUE(username, email)  
);
-- create game table
CREATE TABLE cs361_condreab.Game
(
  gameID INT NOT NULL UNIQUE,
  startDate DATETIME,
  saveDate DATETIME,
  username varchar(25),
  PRIMARY KEY (gameID),
  FOREIGN KEY (username) REFERENCES User(username)
);

-- create player table
CREATE TABLE cs361_condreab.Player
(
  health INT NOT NULL,
  weapon INT,
  roomID INT,
  itemID INT,
  gameID INT,
  FOREIGN KEY (weapon) REFERENCES Item(ItemID),
  
);

-- create rooms table

-- create character table

-- create animal table

-- create item table

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

-- get rooms with username and gameID

-- get player with username and gameID

-- save player with username and gameID

-- save rooms with username and gameID

-- delete game data with gameID


CREATE TABLE User
(
  username VARCHAR(25) NOT NULL UNIQUE,
  email VARCHAR(25) NOT NULL UNIQUE,
  credentials VARCHAR(64) NOT NULL,
  PRIMARY KEY (username),
  CONSTRAINT user_info UNIQUE(username, email)
);

CREATE TABLE Game
(
  game_ID INT NOT NULL,
  start_date DATETIME NOT NULL,
  save_date DATETIME NOT NULL,
  player_ID INT NOT NULL,
  username VARCHAR(25) NOT NULL,
  PRIMARY KEY (game_ID),
  FOREIGN KEY (player_ID) REFERENCES Player(player_ID),
  FOREIGN KEY (username) REFERENCES User(username)
);

CREATE TABLE Room
(
  room_ID INT NOT NULL,
  x_coord INT NOT NULL,
  y_coord INT NOT NULL,
  short_description TEXT NOT NULL,
  long_description TEXT NOT NULL,
  next_level BOOLEAN NOT NULL,
  game_ID INT NOT NULL,
  PRIMARY KEY (room_ID),
  FOREIGN KEY (game_ID) REFERENCES Game(game_ID)
);

CREATE TABLE Player
(
  health INT NOT NULL,
  weapon INT NOT NULL,
  player_ID INT NOT NULL,
  room_ID INT NOT NULL,
  PRIMARY KEY (player_ID),
  FOREIGN KEY (weapon) REFERENCES Item(item_ID)
  FOREIGN KEY (room_ID) REFERENCES Room(room_ID)
);

CREATE TABLE Item
(
  item_ID INT NOT NULL,
  name VARCHAR(25) NOT NULL,
  description TEXT NOT NULL,
  type VARCHAR(25) NOT NULL,
  dmg_low INT,
  dmg_high INT,
  value INT,
  health_gain INT,
  use_count INT,
  player_ID INT,
  room_ID INT,
  animal_ID INT,
  PRIMARY KEY (item_ID),
  FOREIGN KEY (player_ID) REFERENCES Player(player_ID),
  FOREIGN KEY (room_ID) REFERENCES Room(room_ID),
  FOREIGN KEY (animal_ID) REFERENCES Animal(animal_ID)
);

CREATE TABLE Event
(
  value INT NOT NULL,
  description TEXT NOT NULL,
  event_ID INT NOT NULL,
  number_of_choices INT NOT NULL,
  name VARCHAR(25) NOT NULL,
  room_ID INT NOT NULL,
  PRIMARY KEY (event_ID),
  FOREIGN KEY (room_ID) REFERENCES Room(room_ID)
);

CREATE TABLE Character
(
  character_ID INT NOT NULL,
  name VARCHAR(25) NOT NULL,
  description TEXT NOT NULL,
  dialogue TEXT NOT NULL,
  trade_complete BOOLEAN NOT NULL,
  room_ID INT NOT NULL,
  offer_item_ID INT NOT NULL,
  wanted_item_ID INT NOT NULL,
  PRIMARY KEY (character_ID),
  FOREIGN KEY (room_ID) REFERENCES Room(room_ID),
  FOREIGN KEY (offer_item_ID) REFERENCES Item(item_ID),
  FOREIGN KEY (wanted_item_ID) REFERENCES Item(item_ID)
);

CREATE TABLE Animal
(
  animal_ID INT NOT NULL,
  name VARCHAR(25) NOT NULL,
  description TEXT NOT NULL,
  health INT NOT NULL,
  injure_chance FLOAT NOT NULL,
  damage INT NOT NULL,
  room_ID INT NOT NULL,
  PRIMARY KEY (animal_ID),
  FOREIGN KEY (room_ID) REFERENCES Room(room_ID)
);

CREATE TABLE connected
(
  room_ID_1 INT NOT NULL,
  room_ID_2 INT NOT NULL,
  PRIMARY KEY (room_ID_1, room_ID_2),
  FOREIGN KEY (room_ID_1) REFERENCES Room(room_ID),
  FOREIGN KEY (room_ID_2) REFERENCES Room(room_ID)
);