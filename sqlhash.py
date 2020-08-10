import bcrypt

# passwd = b's$cret12'
# salt = bcrypt.gensalt(12)
# hashed = bcrypt.hashpw(passwd, salt)

# print(salt)
# print(hashed)
# print(type(hashed))
# print(hashed.decode('utf-8'))

# print(bcrypt.checkpw(passwd, hashed)) #True/False

# def generate_sql_string_hash(password):
#     """generates a byte string used for storage in the sql databased"""
#     return bcrypt.hashpw(password.encode('utf-8'), stored_salt).decode('utf-8')

class SqlHash:
    def __init__(self, salt=b'$2b$12$MuHPMaxTyaX.cr8FPAgmqe'):
        """Creates a Checkers Studio hash object"""
        self._salt = salt # stored salt

    def generate_sql_string_hash(self, password):
        """generates a byte string used for storage in the sql databased.\n 
        Returns byte hash string of password.\n
        password: string
        \tutf-8 password"""
        return bcrypt.hashpw(password.encode('utf-8'), self._salt).decode('utf-8')
 
    def check_sql_string_hash(self, password, string_hash):
        """Checks if the password string matches the hash string. Returns boolean\n
        password: string
        \tutf-8 password. Up to 60 length.
        string_hash: string
        \tutf-8 hash. Up to 72 length.
        """
        return bcrypt.checkpw(password.encode('utf-8'), string_hash.encode('utf-8'))
    
    def set_salt(self, rounds=12):
        """set the current salt to a randomized one, returns salt as a byte string.\n
        rounds: Int
        \tsalt rounds. The higher the integer, the slower the hash.
        """
        self._salt = bcrypt.gensalt(rounds)
        return self._salt.decode('utf-8')
