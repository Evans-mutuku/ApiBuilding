import requests
from django.shortcuts import render 
import random
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect


def index(request):
  response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
  data = response.json()
  fact = data['text']

  r3 = requests.get('https://dog.ceo/api/breeds/image/random')
  res3 = r3.json()
  dog = res3['message']

  # This is the assignment for the Hackathon, 
  # Instructions: 
  # Use this API and randomize the students
  response2 = requests.get('https://freetestapi.com/api/v1/students')
  data2 = response2.json()

    # Shuffle the list of students
  random.shuffle(data2)

    # Select a random student
  random_student = random.choice(data2)
    
    # Extract the name of the random student
  name = random_student.get('name', '')





  return render(request, 'index.html', {'fact': fact, 'dog': dog,  'name': name})


