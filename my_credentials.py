##################################################################
#   File name: my_credentials.py                                 #
#   Written by: Minbo Chung                                      #
#   File created: 2023-08-18                                     #
##################################################################

from configparser import ConfigParser

# Retrieve Tasks info from minbochung95
# Send email via minbochung95.dev

class MyCredentials():
    def __init__(self):
        config = ConfigParser()
        # Create your own config.ini file in cred folder.
        config.read('./cred/config.ini')
        print("sections:", config.sections())
        self.task_usr = config.get('task_receiver', 'username')
        self.task_psw = config.get('task_receiver', 'password')
        self.tasks_build_credentials = config.get('path_to_oauth2_credentials', 'task')
        self.sender_usr = config.get('email_sender', 'username')
        self.sender_psw = config.get('email_sender', 'password')
        self.gmail_build_credentials = config.get('path_to_oauth2_credentials', 'gmail')

    def get_task_creds(self):
        return self.task_usr, self.task_psw
    def get_email_sender_creds(self):
        return self.sender_usr, self.sender_psw
    def get_oauth2_credentials(self):
        return self.tasks_build_credentials, self.gmail_build_credentials
    
if __name__=="__main__":
    x = MyCredentials()
    sender, _ = x.get_email_sender_creds()
    receiver, _ = x.get_task_creds()
    print(f"Task account: {receiver}\nSender account: {sender}")