#make initial calls to api

import requests

sportsdata_ioKey = '5188a91387e44d0eb060a5c22248d0cd'
#Make API call and store the response.
# Active teams
url = 'https://api.sportsdata.io/v3/nfl/scores/json/Teams?key=5188a91387e44d0eb060a5c22248d0cd'
# Players by team
# url = 'https://api.sportsdata.io/v3/nfl/scores/json/Players/NE?key=5188a91387e44d0eb060a5c22248d0cd'
# Stats for Cam Newton 2020 week 1
# url = 'https://api.sportsdata.io/v3/nfl/stats/json/PlayerGameStatsByPlayerID/2020REG/1/13320?key=5188a91387e44d0eb060a5c22248d0cd'
r = requests.get(url)
print(f"Status code: {r.status_code}")
#Store the response in a variable
response_dicts = r.json()
#process results
number_of_teams = len(response_dicts)
print(f"Teams returned: {number_of_teams}")
response_dict = response_dicts[0]
print(f"\nKeys:{len(response_dict)}")
# Print list of keys
# for key in sorted(response_dict.keys()):
#     print(key)
for i in range(number_of_teams):
    print(response_dicts[i]['Key'])
