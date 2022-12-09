import os.path
# from __future__ import print_function
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import google.auth
from googleapiclient.http import MediaFileUpload
import requests
from flask import json 
import time


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= "credentials.json"


def fileUpload(fileName, orderId, directory):
    
    fileId=[]
    # ----------------     OAuth     ---------------
    
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

   

        # creds, _ = google.auth.default()


    try:

        # create drive api client
        service = build('drive', 'v3', credentials=creds)
        file_metadata = {
            'name': f'ORDER# {orderId}',
            'mimeType': 'application/vnd.google-apps.folder'
        }

   
        file = service.files().create(body=file_metadata, fields='id').execute()
        # print(F'Folder ID: "{file.get("id")}".')
        folderId = file.get('id')

        for fileName in fileName:
            
            file_metadata = {
                'name': fileName,
                'parents': [folderId]
            }
            media = MediaFileUpload(f'{directory}/{fileName}', resumable=True)
            
            file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            # print(F'File ID: "{file.get("id")}".')
            fileId.append(file.get('id'))



        service = build('drive', 'v3', credentials=creds)
        ids = []
        file_id = file.get("id")

        def callback(request_id, response, exception):
            if exception:
                # Handle error
                print(exception)
            else:
                # print(f'Request_Id: {request_id}')
                # print(F'Permission Id: {response.get("id")}')
                ids.append(response.get('id'))

        batch = service.new_batch_http_request(callback=callback)
        user_permission = {
            'type': 'anyone',
            'role': 'writer'
        }
        batch.add(service.permissions().create(fileId=folderId,
                                               body=user_permission,
                                               fields='id',))

        batch.execute()

        return [folderId, fileId]

    except HttpError as error:
        print(F'An error occurred: {error}')
        return None




#================================= Update Files ==============================
def fileUpdate(fileName, folderId, directory):
    fileId=[]
    # ----------------     OAuth     ---------------
    # print(fileName, folderId, directory)
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

        
    try:

    # create drive api client
        service = build('drive', 'v3', credentials=creds)

        for fileName in fileName:
        
            file_metadata = {
                'name': fileName,
                'parents': [folderId]
            }
            media = MediaFileUpload(f'{directory}/{fileName}', resumable=True)
            
            file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            # print(F'File ID: "{file.get("id")}".')
            fileId.append(file.get('id'))
        
        return [folderId, fileId]
        

    except HttpError as error:
        print(F'An error occurred: {error}')
        return None
    






# =================================== File Get =========================

def fileGet(folderId):

    filesDetail = []

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

   

        # creds, _ = google.auth.default()

    try:
        service = build('drive', 'v3', credentials=creds)

        # Call the Drive v3 API
        results = service.files().list(q=f" '{folderId}' in parents and trashed = false",
                                            spaces='drive',
        fields="nextPageToken, files(*)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
            return

        for item in items:
            filesDetail.append([item['name'],item['webViewLink']])
            # print(item['name'])
            # print(item['webViewLink'])

            # print(u'{0} ({1}) {2}'.format(item['name'], item['id'], item['selfLink']))
        # print('files details', filesDetail)
        return filesDetail
    
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')
    
    