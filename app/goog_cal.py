from __future__ import print_function
import pickle
import os.path
import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

creds = None

def initalise_google_cal_access(creds=creds):

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'app/client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    print(service)

    return service

def get_todays_events(service):

    todays_events = []

    now = datetime.datetime.utcnow().isoformat()
    today = datetime.datetime.utcnow().strftime('%Y-%m-%d')
    today_start = today + 'T00:00:00Z'
    today_end = today + 'T23:59:59Z'

    print('Get upcoming events for the day')
    # events_result = service.events().list(calendarId='primary', timeMin=now + 'Z', singleEvents=True, maxResults=25 ,orderBy='startTime').execute()
    events_result = service.events().list(calendarId='primary', timeMin=today_start, timeMax=today_end, singleEvents=True, maxResults=25 ,orderBy='startTime').execute()
                                         
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
        todays_events.append('No upcoming events today. You are either free or this app is broken...')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        start_formatted = datetime.datetime.strptime(start, '%Y-%m-%dT%H:%M:%SZ').strftime('%H:%M')
        # print(start_formatted.strftime('%H:%M'))

        todays_events.append((start_formatted, event['summary'], event['htmlLink']))

    return todays_events


service = initalise_google_cal_access()
# todays_events = get_todays_events(service=service)