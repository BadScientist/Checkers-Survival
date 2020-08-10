import unittest
import sqlhash
import sqlserver

class testHashClass(unittest.TestCase):
    def test_1(self):
        test_hash = sqlhash.SqlHash()
        print(test_hash.generate_sql_string_hash("test123"))
        print(test_hash.check_sql_string_hash("test123", "$2b$12$MuHPMaxTyaX.cr8FPAgmqeoGJymzqLh.iREvNOjUBQLvLBJ71Ucde"))
        print(len(test_hash.generate_sql_string_hash("test123")))
        
class testServerClass(unittest.TestCase):
    def test_1(self):
        server_test = sqlserver.SqlServer()

        account_query = sqlserver.SqlAccount("cs361_condreab", server_test.get_cursor(), b'$2b$12$MuHPMaxTyaX.cr8FPAgmqe')
        
        #delete the previous account
        account_query.delete_account("condreab", "test123")
        account_query.delete_account("condreab", "newpass")
        #create new account
        self.assertTrue(account_query.create_account("condreab", "condreab@oregonstate.edu", "test123"))
        
        #check if users exist
        self.assertTrue(account_query.check_username_exists("condreab"))
        self.assertFalse(account_query.check_username_exists("some_random_user"))
        
        #check if login successful
        self.assertTrue(account_query.check_login("condreab", "test123"))
        self.assertFalse(account_query.check_login("condreab", "incorrect_pass"))

        #update email
        self.assertTrue(account_query.update_email("new_email@oregonstate.edu", "condreab", "test123"))

        #change password and check if new password works
        self.assertTrue(account_query.update_password("newpass", "condreab", "test123"))
        self.assertTrue(account_query.check_login("condreab","newpass"))


if __name__ == '__main__':
    unittest.main(exit=False)
