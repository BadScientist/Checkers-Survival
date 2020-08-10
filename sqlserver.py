# new maria db access
# https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/
import sys
import mariadb
import sqlhash

# # Connect to MariaDB Platform
# try:
#     conn = mariadb.connect(
#         user="cs361_condreab",
#         password="Checkers_Studio",
#         host="classmysql.engr.oregonstate.edu",
#         port=3306,
#         database="cs361_condreab"

#     )
# except mariadb.Error as e:
#     print(f"Error connecting to MariaDB Platform: {e}")
#     sys.exit(1)

# # Get Cursor
# cur = conn.cursor()

# cur.execute("SELECT username, credentials FROM User WHERE username = 'condreab'")

# # Print Result-set
# for (username, credentials) in cur:
#     print(f"username: {username}, credentials: {credentials}")

# print(cur.username)

# conn.close()

class SqlServer:
    
    def __init__(self):
        """sqlServer Constructor: creates a sql server object."""
        self.__user = "cs361_condreab"
        self.__password = "Checkers_Studio"
        self.__host = "classmysql.engr.oregonstate.edu"
        self.__port = 3306
        self.__database = "cs361_condreab"
        # self._hash = sqlHash.sqlHash()
        self.__conn = None

        self.__connect()

    def __connect(self):    
        try:
            self.__conn = mariadb.connect(
                user = self.__user,
                password = self.__password,
                host = self.__host,
                port = self.__port,
                database = self.__database
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
        # create the cursor for accesss
        self._cur = self.__conn.cursor()

    def get_cursor(self):
        return self._cur

    def __del__(self):
        """
        sqlServer destructor. closes sql connection.
        """
        # close connection when object deletes from garbage collection
        self.__conn.close()

class SqlAccount:
    # b'$2b$12$MuHPMaxTyaX.cr8FPAgmqe'
    def __init__(self, database, cursor, salt):
        self._database = database
        self._cur = cursor
        self._hash = sqlhash.SqlHash(salt)

    def check_username_exists(self, username):
        """
            Checks if username exists in database. Returns boolean.\n
            username: string
            \tUsername in database (case sensitive).
        """
        try:
            self._cur.execute("SELECT username FROM "+self._database+".User WHERE username=?",
            (username,))
        except mariadb.Error as e:
            print("ERROR:", e)
            return False
        result = self._cur.fetchone()
        if not result:
            return False
        return True

    def check_login(self, username, password):
        """
            Checks username and password (hash). Returns boolean.\n
            username: string
            \tusername of account (case sensitive).
            password: string
            \tpassword of account (case sensitive). Converted to hash byte.
        """
        # convert password to hash
        hash = self._hash.generate_sql_string_hash(password)
        try:
            self._cur.execute("SELECT username FROM "+self._database+".User WHERE username=? AND credentials=?",
            (username, hash))
        except mariadb.Error as e:
            print("ERROR:", e)
            return False

        result = self._cur.fetchone()
        if not result:
            return False
        return True

    def create_account(self, username, email, password):
        """
        Creates an account on the User table
        username: string
        email: string
        password: string
        """
        #create hash byte string for storage
        hash = self._hash.generate_sql_string_hash(password)
        try:
            self._cur.execute("INSERT INTO "+self._database+".User (username, email, credentials) VALUES (?, ?, ?)",
            (username, email, hash))
        except mariadb.Error as e:
            print("ERROR:", e)
            return False
        return True

    def update_email(self, email, username, password):
        """
        Updates the email of an existing user account. Requires password.
        email: string
        username: string
        passsword: string
        """
        #get hash string
        hash = self._hash.generate_sql_string_hash(password)
        try:
            self._cur.execute("UPDATE "+self._database+".User SET email=? WHERE username=? AND credentials=?",
            (email, username, hash))
        except mariadb.Error as e:
            print("ERROR:", e)
            return False
        return True

    def update_password(self, new_password, username, old_password):
        """
        Updates the password of an exsiting user account. Requiers old password.
        new_password: string
        username: string
        old_password: string
        """
        new_hash = self._hash.generate_sql_string_hash(new_password)
        old_hash = self._hash.generate_sql_string_hash(old_password)
        try:
            self._cur.execute("UPDATE "+self._database+".User SET credentials=? WHERE username=? AND credentials=?",
            (new_hash, username, old_hash))
        except mariadb.Error as e:
            print("ERROR:", e)
            return False
        return True

    def delete_account(self, username, password):
        """
        Deletes an account of an existing user accout. Requires password.
        username: string
        password: string
        """
        #require password to be correct
        hash = self._hash.generate_sql_string_hash(password)
        try:
            self._cur.execute("DELETE FROM "+self._database+".User WHERE username=? AND credentials=?",
            (username, hash))
        except mariadb.Error as e:
            print("ERROR:", e)
            return False
        return True

class SqlGame:

    def __init__(self, database, cursor):
        self._database = database
        self._cur = cursor

    # def get_saves(self, username):
    #     # return a list of games saved, sorted by most recent (date)
    
    # def save_game(self, username, player, rooms):
    #     # saves the game state

    # def get_game(self, username, gameID):
    #     # return the game state as a list

    #     # 1. Get player object, append to dictionary
    #     # 2. Get room objects, append to dictionary

    # def delete_game(self, username, gameID):
        
        
        """
            {
                player: {
                    health: Int
                    location: Room
                    weapon: obj
                    inventory: [Item]
                    canvas: Canvas
                }
                rooms: [
                    Room: {
                        x: Int
                        y: Int
                        long_desc: String
                        shrt_desc: String
                        N: Room
                        S: Room
                        E: Room
                        W: Room
                        character: Character {
                            name : String
                            description: String
                            dialogue: String
                            item_offered: Item
                            item_wanted: Item
                            trade_complete: Bool
                        }
                        animal: Animal {    
                            name: String
                            description: String
                            health: Int
                            injure_chance: Double
                            damage: Int
                            hunt_reward: Item
                        }
                        item: Item {name, str_desc, item_type 
                            weapon: {dmg_low dmg_high}}
                            consumable: {value, health_gain, use_count}
                        next_level: Bool
                        event: Event
                    }
                    ]
            }
        """