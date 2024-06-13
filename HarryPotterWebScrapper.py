from bs4 import BeautifulSoup
import requests
import inflection

#Libraries requirement: 
#  - requests
#  - beautifulsoup
#  - inflection

# 1 Getting the html
URL = "https://www.wizardingworld.com/es/quiz"
r = requests.get(URL)
html=r.text

# 2 HTML Parsing
soup = BeautifulSoup(html, 'html.parser')
type(soup)

target_classes = ["HubFeatureItem?root___qlhz", "ImageWithDetails_image_wrapper__c0Xr1"] 

class_elements = soup.find_all(class_ = target_classes, href=True)

quizes_list = []

for class_element in class_elements:
  quizes_list.append(
    inflection.titleize(
      class_element['href'].lstrip("/es/quiz/")
    )
  )

print(quizes_list)
