import os.path
# from __future__ import print_function
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import google.auth
from googleapiclient.http import MediaFileUpload


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


def get_docs():

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
            files = []
            page_token = None
            while True:
                # pylint: disable=maybe-no-member
                response = service.files().list(q="mimeType='application/vnd.google-apps.folder'",
                                                spaces='drive',
                                                fields='nextPageToken, '
                                                    'files(id, name)',
                                                pageToken=page_token).execute()
                for file in response.get('files', []):
                    # Process change
                    print(F'Found file: {file.get("name")}, {file.get("id")}')
                files.extend(response.get('files', []))
                page_token = response.get('nextPageToken', None)
                if page_token is None:
                    break

        except HttpError as error:
            print(F'An error occurred: {error}')
            files = None

        return files
    
    

# main()