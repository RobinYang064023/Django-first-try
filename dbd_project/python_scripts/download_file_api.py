from __future__ import print_function
from httplib2 import Http

import io
from apiclient.discovery import build
from apiclient.http import MediaIoBaseDownload
from oauth2client import client
from oauth2client import tools
from oauth2client import file

SCOPES = 'https://www.googleapis.com/auth/drive.readonly'
store = file.Storage('client_id.json')
APPLICATION_NAME = 'Python download drive'

def download_csv(file_id, file_name):
  
  #Shows basic usage of the Google Drive API.

  
  # Setup the Drive v3 API

  creds = store.get()
  if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_id.json', SCOPES)
    creds = tools.run_flow(flow, store)
  service = build('drive', 'v3', http=creds.authorize(Http()))

  request = service.files().export_media(fileId=file_id, mimeType='text/csv')
  fh = open(file_name, 'w', newline = '')
  #fh = io.BytesIO()
  fh = io.FileIO(file_name, 'wb')
  
  downloader = MediaIoBaseDownload(fh, request)
  done = False
  while done is False:
    status, done = downloader.next_chunk()
    print ("Download %d%%." % int(status.progress() * 100))
  fh.close()


def drive_ls():  
  # Setup the Drive v3 API
  SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'
  store = file.Storage('credentials.json')
  creds = store.get()
  if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
  service = build('drive', 'v3', http=creds.authorize(Http()))
  
  # Call the Drive v3 API
  results = service.files().list(
    pageSize=10, fields="nextPageToken, files(id, name)").execute()
  items = results.get('files', [])
  if not items:
    print('No files found.')
  else:
    print('Files:')
    for item in items:
      print('{0} ({1})'.format(item['name'], item['id']))

if __name__ == '__main__':
  download_csv()
