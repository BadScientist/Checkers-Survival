import unittest
import sqlHash
import sqlServer

class testHashClass(unittest.TestCase):
    def test_1(self):
        test_hash = sqlHash.sqlHash()
        print(test_hash.generate_sql_string_hash("test123"))
        print(test_hash.check_sql_string_hash("test123", "$2b$12$MuHPMaxTyaX.cr8FPAgmqeoGJymzqLh.iREvNOjUBQLvLBJ71Ucde"))
        print(len(test_hash.generate_sql_string_hash("test123")))
        
class testServerClass(unittest.TestCase):
    def test_1(self):
        server_test = sqlServer.sqlServer()
        
        #delete the previous account
        server_test.delete_account("condreab", "test123")
        server_test.delete_account("condreab", "newpass")
        #create new account
        server_test.create_account("condreab", "condreab@oregonstate.edu", "test123")
        
        #check if users exist
        print(server_test.check_username_exists("condreab"))
        print(server_test.check_username_exists("some_random_user"))
        
        #check if login successful
        print(server_test.check_login("condreab", "test123"))
        print(server_test.check_login("condreab", "incorrect_pass"))

        #update email
        server_test.update_email("new_email@oregonstate.edu", "condreab", "test123")

        #change password and check if new password works
        server_test.update_password("newpass", "condreab", "test123")
        print(server_test.check_login("condreab","newpass"))


if __name__ == '__main__':
    unittest.main(exit=False)
