import requests

api_key = 'E1UGbau1SQC_F3jjmci7kUrLyBykSphb9qNrui_2sbJOsn3e9nHrNFynwA5IMwT6kqACTQCYmwg72FaYYlsk3X1On3IPMJB5RN7grldZEyKm7k4w13X157b4FWFLYXYx'

headers = {'Authorization': 'Bearer {}'.format(api_key)}
search_api_url = 'https://api.yelp.com/v3/businesses/search'
params = {'term': 'coffee',
          'location': 'Milan, Italy',
          'is_closed': 'False',
          'limit': 50}

response = requests.get(search_api_url, headers=headers,
                        params=params, timeout=5)

# print(response.url)
# print(response.status_code)

data_dict = response.json()
type(data_dict)
data_dict.keys()

data_dict['businesses'][0]
