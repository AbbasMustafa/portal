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


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="credentials.json"


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

   

        creds, _ = google.auth.default()

    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)
        file_metadata = {
            'name': f'ORDER# {orderId}',
            'mimeType': 'application/vnd.google-apps.folder'
        }

   
        file = service.files().create(body=file_metadata, fields='id').execute()
        print(F'Folder ID: "{file.get("id")}".')
        folderId = file.get('id')

        for fileName in fileName:
            
            file_metadata = {
                'name': fileName,
                'parents': [folderId]
            }
            media = MediaFileUpload(f'{directory}/{fileName}', resumable=True)
            
            file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            print(F'File ID: "{file.get("id")}".')
            fileId.append(file.get('id'))

        return [folderId, fileId]

    except HttpError as error:
        print(F'An error occurred: {error}')
        return None


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

   

        creds, _ = google.auth.default()

    try:
        service = build('drive', 'v3', credentials=creds)

        # Call the Drive v3 API
        results = service.files().list(q=f" '{folderId}' in parents and trashed = false",
                                            spaces='drive',
            pageSize=10, fields="nextPageToken, files(*)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
            return
        print('Files:')
        for item in items:
            filesDetail.append([item['name'],item['webViewLink']])
            # print(item['name'])
            # print(item['webViewLink'])

            # print(u'{0} ({1}) {2}'.format(item['name'], item['id'], item['selfLink']))

        return filesDetail
    
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')
    
    
    # try:
        # create drive api client
        # service = build('drive', 'v3', credentials=creds)
    #     folder_id = '1mWLRE14TeJXtJWUyYcBo27aMi84fjCM7'
    #     query = f"parents = {folder_id}"

    #     response = service.files().list(q=query).execute()
    #     files = response.get('files')
    #     nextPageToken = response.get('nextPageToken')
    #     print(f'Response: {response}')

    #     while nextPageToken:
    #         response = service.files().list(q=query).execute()
    #         files.extend(response.get('files'))
    #         nextPageToken = response.get('nextPageToken')
    #         print(f'Response: {response}')
        
    # except HttpError as error:
    #     # TODO(developer) - Handle errors from drive API.
    #     print(f'An error occurred: {error}')