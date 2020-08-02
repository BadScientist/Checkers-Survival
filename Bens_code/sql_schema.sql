CREATE TABLE cs361_condreab.User
(
  username varchar(25) NOT NULL UNIQUE,
  email varchar(25) NOT NULL UNIQUE,
  credentials varchar(64) NOT NULL,
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

SELECT COUNT(*)
FROM cs361_condreab.User
WHERE username = 'condreab'