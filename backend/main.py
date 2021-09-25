import requests
import speech_recognition as sr

api_key = 'E1UGbau1SQC_F3jjmci7kUrLyBykSphb9qNrui_2sbJOsn3e9nHrNFynwA5IMwT6kqACTQCYmwg72FaYYlsk3X1On3IPMJB5RN7grldZEyKm7k4w13X157b4FWFLYXYx'

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("You said " + r.recognize_google(audio))
    term = r.recognize_google(audio)
    location = 'Milan, Italy'

    headers = {'Authorization': 'Bearer {}'.format(api_key)}
    search_api_url = 'https://api.yelp.com/v3/businesses/search'
    params = {'term': term,
              'location': location,
              'is_closed': 'False',
              'limit': 50}

    response = requests.get(search_api_url, headers=headers,
                            params=params, timeout=5)

    # print(response.url)
    # print(response.status_code)

    data_dict = response.json()
    type(data_dict)
    data_dict.keys()

    print(data_dict['businesses'][0])

except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print(
        "Could not request results from Speech Recognition service; {0}".format(e))
