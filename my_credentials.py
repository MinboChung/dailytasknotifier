##################################################################
#   File name: my_credentials.py                                 #
#   Written by: Minbo Chung                                      #
#   File created: 2023-08-18                                     #
##################################################################

from configparser import ConfigParser

class MyCredentials():
    def __init__(self):
        config = ConfigParser()
        # Create your own config.ini file in cred folder.
        config.read('./cred/config.ini')

        self.usrname = config.get('gmail_account_info', 'username')
        self.psw = config.get('gmail_account_info', 'password')
    
    def get_creds(self):
        return (self.usrname, self.psw)

if __name__=="__main__":
    x = MyCredentials()

    print(x.get_creds())