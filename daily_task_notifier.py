##################################################################
#   File name: daily_task_notifier.py                            #
#   Written by: Minbo Chung                                      #
#   File created: 2023-08-18                                     #
##################################################################

from my_credentials import MyCredentials
from abc import ABC, abstractmethod

class DailyTaskNotifier(ABC):
    def __init__(self, email=None, pw=None):
        local_email, local_password  = MyCredentials().get_creds()
        self.email = local_email if email==None else email
        self.pw = local_password if pw==None else pw
    ...


if __name__=="__main__":
    x = MyCredentials()
    print(x.get_creds())