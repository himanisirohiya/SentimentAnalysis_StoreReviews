import json
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob

with open('reviews.json', 'r') as json_file:
    reviews = json.load(json_file)

# Initialize stopwords and lemmatizer
# Get a set of all stopwords in english language eg: is, was, and, etc
# Lemmatization: convert words to its root form eg: better -> good, eating -> eat
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Preprocess each review
for review in reviews:
    text = review['text'].lower()
    text = re.sub(r'[^A-za-z\s]','',text)
    #Tokenize the text
    words = word_tokenize(text) 
    # Remove stop words and apply Lemmatization
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    # Assemble the review again
    review['text'] = ' '.join(words)

# Extract text of all reviews and perform vectorization
texts = [review['text'] for review in reviews]

# Vectorization using TF-IDF
# Vectorize using TF-IDF
vectorizer = TfidfVectorizer(max_features=1000)
X = vectorizer.fit_transform(texts)

# Perform sentiment analysis using TextBlob and TF-IDF data
for i, text in enumerate(texts):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    reviews[i]['sentiment_score'] = sentiment_score

# Store the updated reviews with sentiment scores
with open('reviews_with_sentiment.json', 'w') as json_file:
    json.dump(reviews, json_file, indent=4)