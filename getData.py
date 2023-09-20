import googlemaps
import time
import config
import json
from faker import Faker
import random

# Set up your API key
api_key = config.api_key
gmaps = googlemaps.Client(key=api_key)

# Specify the place ID or location details for the store
place_id = config.place_id
all_reviews = []
# Request the place details, including reviews
place_details = gmaps.place(place_id=place_id, fields=['reviews'])
# Extract the reviews from the place details
reviews = place_details['result']['reviews']
# Check if there are more reviews and fetch additional pages using pagetoken
while 'next_page_token' in place_details:
    next_page_token = place_details['next_page_token']
    time.sleep(20)  # Add a short delay between requests (2 seconds in this example)
    place_details = gmaps.place(place_id=place_id, fields=['reviews'], page_token=next_page_token)
    reviews += place_details['result']['reviews']

# Process the reviews as per your requirements
for review in reviews:
    # print(review)
    text = review['text']
    rating = review['rating']
    # Perform sentiment analysis or any other desired operations
    # with the review text and rating

fake = Faker()

# Simulated review data with varying text aligned with rating
simulated_reviews = []
for _ in range(10):
    rating = random.randint(1, 5)
    
    if rating == 5:
        text = fake.paragraph(nb_sentences=3, ext_word_list=["excellent", "fantastic", "amazing", "great"])
    elif rating == 4:
        text = fake.paragraph(nb_sentences=3, ext_word_list=["good", "nice", "satisfactory", "commendable"])
    elif rating == 3:
        text = fake.paragraph(nb_sentences=3, ext_word_list=["average", "okay", "neutral", "decent"])
    elif rating == 2:
        text = fake.paragraph(nb_sentences=3, ext_word_list=["disappointing", "subpar", "below average", "unsatisfactory"])
    else:
        text = fake.paragraph(nb_sentences=3, ext_word_list=["poor", "horrible", "terrible", "bad"])
    
    review = {
        'author_name': fake.name(),
        'rating': rating,
        'text': text,
        'time': fake.unix_time()
    }
    reviews.append(review)

# Store Google Maps reviews in all_reviews
for review in reviews:
    all_reviews.append({
        'author_name': review['author_name'],
        'rating': review['rating'],
        'text': review['text'],
        'time': review['time']
    })


# Store simulated reviews in all_reviews
for review in simulated_reviews:
    all_reviews.append({
        'author_name': review['author_name'],
        'rating': review['rating'],
        'text': review['text'],
        'time': review['time']
    })

# Save all reviews to a JSON file
with open('reviews.json', 'w') as json_file:
    json.dump(all_reviews, json_file, indent=4)