# EU-Code-Week

## How to use this app
* Clone the repository
* Run "npm install"
* Run "yarn ios" to run the simulator (for MAC USERS)
 
## Recommendation algorithm
For this algorithm we use 'active filtering', a technique that can filter out items that a user might like on the basis of reactions by similar users, so that we can pull the data from other users in order to analyze their preferences and send them advices.

This method works by searching a large group of people and finding a smaller set of users with tastes similar to a particular user. 
It looks at the items they like and combines them to create a ranked list of suggestions.

There are many ways to decide which users are similar and combine their choices to create a list of recommendations. 

Our Version is made in python.

### The dataset
We pull the data directly from the API, which is very useful to analyze places and preferences.
The users' reaction can be explicit (rating on a scale of 1 to 5, likes or dislikes) or implicit (viewing an item, adding it to a wish list, the time spent on an article).

### Steps involved in collaborative filtering
We asked ourselves these questions:
* How do you determine which users or items are similar to one another?
* Given that you know which users are similar, how do you determine the rating that a user would give to an item based on the ratings of similar users?
* How do you measure the accuracy of the ratings you calculate?

The third question for how to measure the accuracy of your predictions also has multiple answers, which include error calculation techniques that can be used in many places and not just recommenders based on collaborative filtering.

## Wav2vec 2.0, learning the structure of pitch from raw audio

* This new model learns basic speech units used to tackle a self-supervised task. The model is trained to predict the correct speech unit for masked parts of the audio, while at the same time learning what the speech units should be.

* With just 10 minutes of transcribed speech and 53K hours of unlabeled speech, wav2vec 2.0 enables speech recognition models at a word error rate (WER) of 8.6 percent on noisy speech and 5.2 percent on clean speech on the standard LibriSpeech benchmark.


 


