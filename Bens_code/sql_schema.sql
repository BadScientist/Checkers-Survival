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

-- query user
SELECT username, credentials
FROM cs361_condreab.User
WHERE username = 'INSERT_USERNAME_HERE'
AND credentials = 'INSERT_HASH_HERE';

-- delete user
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

-- get rooms with Username and gameID

-- get player with username and gameID

-- save player with username and gameID

-- save rooms with username and gameID

-- delete game data with gameID


