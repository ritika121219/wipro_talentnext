#ques1. Write a program to find check if a string has only octal digits. Given string ['789', '123', '004']
strings = ['789', '123', '004']

for s in strings:
    if all(char in '01234567' for char in s):
        print(f"✅ '{s}' contains only octal digits.")
    else:
        print(f"❌ '{s}' does NOT contain only octal digits.")


#ques2. Extract the user id, domain name and suffix from the following email addresses.
#emails zuck@facebook.com
#sunder33@google.com
#jeff42@amazon.com"""
emails = ['zuck@facebook.com', 'sunder33@google.com', 'jeff42@amazon.com']

for email in emails:
    user_id, domain_full = email.split('@')
    domain, suffix = domain_full.split('.')
    
    print(f"User ID: {user_id}, Domain: {domain}, Suffix: {suffix}")



#ques3. Split the following irregular sentence into proper words
#sentence "A, very very; irregular_sentence as expected outout: A very very irregular sentence
import re

sentence = "A, very very; irregular_sentence"


cleaned = re.sub(r'[^\w\s]', ' ', sentence)

cleaned = cleaned.replace('_', ' ')
result = re.sub(r'\s+', ' ', cleaned).strip()

print(result)


#ques4. Clean up the following tweet so that it contains only the user's message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.

#tweet Good advice! RT @ThelfiextWeb: what I would do differently if I was learning to code today


import re

tweet = "Good advice! RT @ThelfiextWeb: what I would do differently if I was learning to code today"

tweet = re.sub(r'\bRT\b|\bCC\b', '', tweet)


tweet = re.sub(r'@\w+|#\w+|http\S+', '', tweet)


tweet = re.sub(r'[^\w\s]', '', tweet)


cleaned_tweet = re.sub(r'\s+', ' ', tweet).strip()

print(cleaned_tweet)




#ques5. Extract all the text portions between the tags from the following HTML page: https://raw.githubusercontent.com/selva86/datasets/master/sample.html

#Code to retrieve the HTML page is given below:

#import requests

#requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")

#desired_output['Your Title Here', 'Link Name', 'This is a Header', 'This is a Medium Header', This is a new paragraph! This is a another paragraph!', 'This is a new sentence without a paragraph break, in bold italics.']
import requests
from bs4 import BeautifulSoup


url = "https://raw.githubusercontent.com/selva86/datasets/master/sample.html"
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')


results = []
results.append(soup.title.string.strip())

results.append(soup.a.string.strip())

results.append(soup.h1.string.strip())
results.append(soup.h2.string.strip())

paragraphs = soup.find_all('p')
para_text = ' '.join(p.get_text(strip=True) for p in paragraphs)
results.append(para_text)

bold_italic = soup.find('b').get_text(strip=True)
results.append(bold_italic)

print(results)



#ques6. Given below list of words, identify the words that begin and end with the same character.
'''civic
trust
widows
maximum
museums
as
as'''
words = [
    "civic",
    "trust",
    "widows",
    "maximum",
    "museums",
    "as",
    "as"
]

result = [word for word in words if word[0] == word[-1]]

print(result)
