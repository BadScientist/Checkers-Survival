CREATE TABLE cs361_condreab.User
(
  username VARCHAR(25) NOT NULL UNIQUE,
  email VARCHAR(25) NOT NULL UNIQUE,
  credentials VARCHAR(64) NOT NULL,
  PRIMARY KEY (username),
  CONSTRAINT user_info UNIQUE(username, email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE cs361_condreab.Game
(
  game_ID INT NOT NULL UNIQUE AUTO_INCREMENT,
  game_start_date DATETIME NOT NULL,
  game_save_date DATETIME NOT NULL,
  username VARCHAR(25) NOT NULL,
  PRIMARY KEY (game_ID)
--   FOREIGN KEY (username) REFERENCES cs361_condreab.User(username)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE cs361_condreab.Player
(
  player_ID INT NOT NULL UNIQUE AUTO_INCREMENT,
  game_ID INT NOT NULL,
  health INT NOT NULL,
  weapon INT NOT NULL,
  room_ID INT NOT NULL,
  PRIMARY KEY (player_ID)
--   FOREIGN KEY (game_ID) REFERENCES cs361_condreab.Game(game_ID),
--   FOREIGN KEY (weapon) REFERENCES cs361_condreab.Item(item_ID)
--   FOREIGN KEY (room_ID) REFERENCES cs361_condreab.Room(room_ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE cs361_condreab.Room
(
  room_ID INT NOT NULL UNIQUE AUTO_INCREMENT,
  x_coord INT NOT NULL,
  y_coord INT NOT NULL,
  short_description TEXT NOT NULL,
  long_description TEXT NOT NULL,
  next_level BOOLEAN NOT NULL DEFAULT FALSE,
  game_ID INT NOT NULL,
  north_room INT,
  east_room INT,
  south_room INT,
  west_room INT,
  PRIMARY KEY (room_ID)
--   FOREIGN KEY (game_ID) REFERENCES cs361_condreab.Game(game_ID)
--   FOREIGN KEY (north_room) REFERENCES cs361_condreab.Room(room_ID)
--   FOREIGN KEY (east_room) REFERENCES cs361_condreab.Room(room_ID)
--   FOREIGN KEY (south_room) REFERENCES cs361_condreab.Room(room_ID)
--   FOREIGN KEY (west_room) REFERENCES cs361_condreab.Room(room_ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE cs361_condreab.Item
(
  item_ID INT NOT NULL UNIQUE AUTO_INCREMENT,
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
  PRIMARY KEY (item_ID)
--   FOREIGN KEY (player_ID) REFERENCES cs361_condreab.Player(player_ID),
--   FOREIGN KEY (room_ID) REFERENCES cs361_condreab.Room(room_ID),
--   FOREIGN KEY (animal_ID) REFERENCES cs361_condreab.Animal(animal_ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE cs361_condreab.Event
(
  event_ID INT NOT NULL UNIQUE AUTO_INCREMENT,
  event_value INT NOT NULL,
  event_description TEXT NOT NULL,
  number_of_choices INT NOT NULL,
  event_name VARCHAR(25) NOT NULL,
  room_ID INT NOT NULL,
  PRIMARY KEY (event_ID)
--   FOREIGN KEY (room_ID) REFERENCES cs361_condreab.Room(room_ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE cs361_condreab.Character
(
  character_ID INT NOT NULL UNIQUE AUTO_INCREMENT,
  character_name VARCHAR(25) NOT NULL,
  character_description TEXT NOT NULL,
  dialogue TEXT NOT NULL,
  trade_complete BOOLEAN NOT NULL,
  room_ID INT NOT NULL,
  offer_item_ID INT NOT NULL,
  want_item_ID INT NOT NULL,
  PRIMARY KEY (character_ID)
--   FOREIGN KEY (room_ID) REFERENCES cs361_condreab.Room(room_ID),
--   FOREIGN KEY (offer_item_ID) REFERENCES cs361_condreab.Item(item_ID),
--   FOREIGN KEY (wanted_item_ID) REFERENCES cs361_condreab.Item(item_ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE cs361_condreab.Animal
(
  animal_ID INT NOT NULL UNIQUE AUTO_INCREMENT,
  animal_name VARCHAR(25) NOT NULL,
  animal_description TEXT NOT NULL,
  health INT NOT NULL,
  injure_chance FLOAT NOT NULL,
  damage INT NOT NULL,
  room_ID INT NOT NULL,
  item_ID INT NOT NULL,
  PRIMARY KEY (animal_ID)
--   FOREIGN KEY (room_ID) REFERENCES cs361_condreab.Room(room_ID)
--   FOREIGN KEY (item_ID) REFEERENCES cs361_condreab.Item(item_ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Foreign keys
ALTER TABLE cs361_condreab.Game
-- ADD FOREIGN KEY (player_ID) REFERENCES cs361_condreab.Player(player_ID);
-- ALTER TABLE cs361_condreab.Game
ADD FOREIGN KEY (username) REFERENCES cs361_condreab.User(username);

ALTER TABLE cs361_condreab.Room
ADD FOREIGN KEY (game_ID) REFERENCES cs361_condreab.Game(game_ID);
ALTER TABLE cs361_condreab.Room
ADD FOREIGN KEY (north_room) REFERENCES cs361_condreab.Room(room_ID);
ALTER TABLE cs361_condreab.Room
ADD FOREIGN KEY (east_room) REFERENCES cs361_condreab.Room(room_ID);
ALTER TABLE cs361_condreab.Room
ADD FOREIGN KEY (south_room) REFERENCES cs361_condreab.Room(room_ID);
ALTER TABLE cs361_condreab.Room
ADD FOREIGN KEY (west_room) REFERENCES cs361_condreab.Room(room_ID);

ALTER TABLE cs361_condreab.Player
ADD FOREIGN KEY (game_ID) REFERENCES cs361_condreab.Game(game_ID);
ALTER TABLE cs361_condreab.Player
ADD FOREIGN KEY (weapon) REFERENCES cs361_condreab.Item(item_ID);
ALTER TABLE cs361_condreab.Player
ADD FOREIGN KEY (room_ID) REFERENCES cs361_condreab.Room(room_ID);


ALTER TABLE cs361_condreab.Item
ADD FOREIGN KEY (player_ID) REFERENCES cs361_condreab.Player(player_ID);
ALTER TABLE cs361_condreab.Item
ADD FOREIGN KEY (room_ID) REFERENCES cs361_condreab.Room(room_ID);
ALTER TABLE cs361_condreab.Item
ADD FOREIGN KEY (animal_ID) REFERENCES cs361_condreab.Animal(animal_ID);

ALTER TABLE cs361_condreab.Event
ADD FOREIGN KEY (room_ID) REFERENCES cs361_condreab.Room(room_ID);

ALTER TABLE cs361_condreab.Character
ADD FOREIGN KEY (room_ID) REFERENCES cs361_condreab.Room(room_ID);
ALTER TABLE cs361_condreab.Character
ADD FOREIGN KEY (offer_item_ID) REFERENCES cs361_condreab.Item(item_ID);
ALTER TABLE cs361_condreab.Character
ADD FOREIGN KEY (want_item_ID) REFERENCES cs361_condreab.Item(item_ID);

ALTER TABLE cs361_condreab.Animal
ADD FOREIGN KEY (room_ID) REFERENCES cs361_condreab.Room(room_ID);
ALTER TABLE cs361_condreab.Animal
ADD FOREIGN KEY (item_ID) REFERENCES cs361_condreab.Item(item_ID);

-- add these triggers manually 

-- CREATE TRIGGER `GameSaveInsert` BEFORE INSERT ON `Game`
-- FOR EACH ROW BEGIN
-- SET NEW.game_save_date = NOW();
-- END;

-- CREATE TRIGGER `GameSaveUpdate` BEFORE UPDATE ON `Game`
-- FOR EACH ROW BEGIN
-- SET NEW.game_save_date = NOW();
-- END;
