from django.shortcuts import render
import requests
from newsapi import NewsApiClient

def news_index(request):   
  # Initialize NewsApiClient with your API key
    newsapi = NewsApiClient(api_key=
      '42c6eaee15e644f0879f7f1274b479c2') # Fetch top headlines
    top_headlines = newsapi.get_top_headlines(language='en', page_size=5)

    # Extract relevant news data
    latest_news = []
    for article in top_headlines['articles']:
        headline = article['title']
        description = article['description']
        source = article['source']['name']
        url = article['url']  # Get the URL of the article
        latest_news.append({
            'headline': headline, 
            'source': source,
            'url': url, 
            'description': description
        })

    # Fetch data from other APIs
    r1 = requests.get('https://api.github.com/events')
    events = r1.json()[0]['repo']

    r2 = requests.get('https://www.boredapi.com/api/activity')
    activity = r2.json()['activity']

    r3 = requests.get('https://dog.ceo/api/breeds/image/random')
    dog = r3.json()['message']

    # Prepare context data
    context = {
        'title': 'Welcome to myNews_API Portal',
        'latest_news': latest_news,
        'events': events,
        'activity': activity,
        'dog': dog
    }

    # Render the template with context data
    return render(request, 'news_index.html', context)

