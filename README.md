# twitter-summarizer-YangHuNU

## Goals

+ Analyze the first 5 pictures from a Twitter user's Timeline
+ Use Tweepy to search and grab pictures
+ Use Google Vision API for image analysis
+ Apply CI/CD for program testing

## Dev Environment

Install Tweepy
>pip install tweepy

Install Google Cloud Vision
>pip install google-cloud-vision

## Credentials

+ Expecting Twitter API authentications (need developer's account)
+ Expecting Google API authentications

## User's Guide

+ Clone this repository
+ Implement your own API keys
+ Excute on terminal with the following command:
python main.py
+ If you wish to get access to other Twitter user's picture analysis, modify in main.py. 
    * get_all_tweets() method takes parameters of Twitter's user name in parentheses as string

## CI/CD
Test runs will be valid as API authentications are provided.

Currently Tests through GitHub Actions are unsuccessful. However pytest runs locally with provided API keys can pass.

## Sample Outputs

With given twitter users, there are 5 test runs provided. The following two pictures are each from test run 1 and test run 2.

Notice that for test run 1, there is only one picture shown on the user's timeline. Therefore, only the existing one picture will be sent for analysis. In test run 2, there are many pictures posted on the user's Timeline; thus, the first 5 will be sent for analysis. 

![Test run 1](https://github.com/BUEC500C1/twitter-summarizer-YangHuNU/blob/master/images/test_run1.png)
![Test run 2](https://github.com/BUEC500C1/twitter-summarizer-YangHuNU/blob/master/images/test_run3.png)

## References

+ [Google Vision API Documents](https://cloud.google.com/vision)
+ [Tweepy Documentations](http://docs.tweepy.org/en/latest/)