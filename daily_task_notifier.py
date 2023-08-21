##################################################################
#   File name: daily_task_notifier.py                            #
#   Written by: Minbo Chung                                      #
#   File created: 2023-08-18                                     #
##################################################################

from my_credentials import MyCredentials
from abc import ABC, abstractmethod
import base64
from email.message import EmailMessage
import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
import pprint
pp = pprint.PrettyPrinter(indent=6)

# Todo: For the jenkins email address.
# This should be implemented after GoogleAPIHandler.
class JenkinsHanlder:
    def __init__(self):
        # self.usr, self.pw, _ = MyCredentials.get_creds()
        ...
    ...

# Todo: Abstracted class for handling Tasks and gmail.
# Maybe to create a separate python file that 
class GoogleAPIHandler(ABC):
    def __init__(self):
        self.task_credential_json, self.email_credential_json = MyCredentials().get_oauth2_credentials()
        self.service = self.build_service()

    @abstractmethod
    def build_service(self):
        ...

class TasksAPIHandler(GoogleAPIHandler):
    def __init__(self):
        # If scopes are modified, delete the file token.json
        # This will view the tasks and it will likely be changed.
        self.scope = ['https://www.googleapis.com/auth/tasks.readonly']
        super().__init__()

    def build_service(self):
        creds = None

        if os.path.exists('./cred/task_api_token.json'):
            creds = Credentials.from_authorized_user_file('./cred/task_api_token.json', self.scope)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.task_credential_json, self.scope
                )
                # Todo: Find an alternative port number besides 8080 if necessary.
                creds = flow.run_local_server(port=0)
                with open('./cred/task_api_token.json', 'w') as token:
                    token.write(creds.to_json())
                    
        try:
            service = build('tasks', 'v1', credentials=creds)
        except Exception:
            print("TaskAPIHandler: Unable to connect.")
            service = None

        return service
        
    def get_todo_lists(self):
        try:
            res = self.service.tasks().list().execute()
            tasks = res.get('items', [])
            if not tasks:
                print('get_todo_lists: no lists are found.')
        except HttpError as e:
            pp.pprint(e)
        return tasks
    
    def get_tasks(self, tasks_id:str="dHNjYWRPbFRGQTB3QWR3Tg"):
        try:
            res = self.service.tasks().list(tasklist=tasks_id).execute()
            tasks = res.get('items', [])
            if not tasks:
                print('get_tasks: The list of tasks is empty.')                
        except HttpError as e:
            pp.pprint(e)
        return tasks

class GmailAPIHandler(GoogleAPIHandler):
    def build_service(self):
        try:
            service = build('gmail', 'v1', credentials=self.gmail_credential)
        except Exception:
            print("GmailAPIHanlder: Unable to connect.")
            service = None
        return service
        
    def query(self):
        ...
    ...

# Todo: 
class DailyTaskNotifier(ABC):
    def __init__(self):
        ...
    @staticmethod
    def get_tasks():
        ...
    @staticmethod
    def gmail_create_draft():
        ...


if __name__=="__main__":
    task_handler = TasksAPIHandler()
    pp.pprint(task_handler.get_tasks())