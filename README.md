# Sentiment analysis of hotel reviews
This project is a simple service where you can check the polarity of any sentence, ideally it'd be better to check it on review-type text, as it was trained on the same type of data.

To check how it works go to this  [link](https://sentiment-of-reviews.onrender.com). Enter any text and click 'Get the polarity'

To crate this project I followed next steps:
  1. Getting the data
  2. Data Cleaning
  3. Building a model
  4. Model evaluation 
  5. Deploying the model with FLASK 

# 1. Getting the data

I collected a dataset with almost 800k hotel reviews:
* [515K Hotel Reviews from kaggle](https://www.kaggle.com/jiashenliu/515k-hotel-reviews-data-in-europe)
* [Datafinity Hotels reviews]( https://www.kaggle.com/datafiniti/hotel-reviews#7282_1.csv )

Also we scraped some data from TripAdvisor and used [ReviewShake API](http://reviewshake.com) as a trial and got around 8k of reviews. All the datasets had columns with reviews and scores for the hotels(this is our target to predict)

# 2. Data Cleaning
Firstly I created one whole datatset with all reviews with only text (Review text)
 and scores (made the scores in one range from 0 to 5) columns. For classification I replaced scores with 0 or 1 (if score > 2 then score is 1 ). Also, the final dataset was highly imbalanced (I had only apprx 6% of negative reviews only), so I used resampling technique to add more negative reviews.
 
 # 3. Building a model
 
 I used CNN+LSTM layers to classify the reviews. For more details, please go check 'LATM_CNN_model' notebook.
 
 # 4. Model evaluation
 
 It took apprx 3 hours to train my model just using CPUs and I got next results:
 
 - Accuracy: 90.1%
 - ROC AUC score: 90.2%
 - Precision: 90%
 - Recall: 90%
 - F1: 90%
 
 # 5. Deploying the model with FLask
 
 To deploy the model and show result I decided to create a simple app with Flask. I just used my model and several cleaning functions along with FLASK to show results. Also, I created Render Web Service to run my app on it. Check this
 [link](https://sentiment-of-reviews.onrender.com). 
 
 
  ## Requirements
 - Python 3.7
 - OSX
## Install
    pip install -r requirments.txt
## Usage
    python3 app.py

Then open the link  http://0.0.0.0:5000/  in Chrome.
 

