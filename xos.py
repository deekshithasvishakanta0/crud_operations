import requests
from requests_html import HTML

base_url = 'https://stackoverflow.com/questions/tagged/python'
tag="questions"
query_filter="Votes"
url = f"{base_url}{tag}?tab={query_filter}"
url

r = requests.get(url)
html_str= r.text

html = HTML(html=html_str)

question_classes = html.find("s-link")
print(question_classes)