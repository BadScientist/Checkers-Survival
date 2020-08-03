# new maria db access
# https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/
import mariadb
import sys
import sqlHash

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

class sqlServer:
    
    def __init__(self, user="cs361_condreab", password="Checkers_Studio", host="classmysql.engr.oregonstate.edu", port=3306, database="cs361_condreab"):
        """sqlServer Constructor: creates a sql server object. Defaults to project values.\n
        user: string
        \t sql server user
        password: string 
        \tsql server password
        host: string
        \tsql server host
        port: int
        \tsql server port number
        database: string 
        \tsql server database"""
        self._user = user
        self._password = password
        self._host = host
        self._port = port
        self._database = database
        self._hash = sqlHash.sqlHash()
    
        try:
            self._conn = mariadb.connect(
                user = self._user,
                password = self._password,
                host = self._host,
                port = self._port,
                database = self._database
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
        # create the cursor for accesss
        self._cur = self._conn.cursor()

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


    def __del__(self):
        """
        sqlServer destructor. closes sql connection.
        """
        # close connection when object deletes from garbage collection
        self._conn.close()
