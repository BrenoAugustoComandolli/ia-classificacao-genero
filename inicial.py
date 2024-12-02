import requests

CLIENT_ID = ''
CLIENT_SECRET = ''

auth_url = 'https://accounts.spotify.com/api/token'
auth_response = requests.post(auth_url, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

access_token = auth_response.json().get('access_token')
print(access_token)