import requests
from bs4 import BeautifulSoup

# 1. Wikipedia 페이지 요청
# requests.get()를 사용하여 특정 웹 페이지의 HTML 코드를 가져옵니다.
# URL은 "https://en.wikipedia.org/wiki/Web_scraping"이며, 이는 웹 스크래핑에 대한 Wikipedia 페이지입니다.
# 웹 페이지를 서버로부터 요청하여 응답 객체(response)를 받습니다.
url = "https://en.wikipedia.org/wiki/Web_scraping"
response = requests.get(url)

# 2. BeautifulSoup 객체 생성
# BeautifulSoup 객체는 HTML이나 XML 문서를 파싱하는 데 사용됩니다.
# response.text는 요청한 웹 페이지의 HTML 소스를 문자열로 가져오는 것이며, 이 문자열을 BeautifulSoup에 넘겨 HTML 문서를 파싱합니다.
# 'html.parser'는 기본 HTML 파서로, HTML을 분석하고 구문 트리를 구축하는 데 사용됩니다.
soup = BeautifulSoup(response.text, 'html.parser')

# 3. 첫 번째 제목 <h1> 태그 추출
# soup.find()는 HTML에서 특정 태그를 찾는 메서드입니다. 여기서는 첫 번째 <h1> 태그를 찾습니다.
# <h1> 태그는 일반적으로 웹 페이지의 가장 큰 제목을 의미합니다.
# .text는 해당 태그 안의 텍스트만을 추출하는 메서드입니다. <h1> 태그는 'Web scraping'이라는 텍스트를 포함하고 있습니다.
title = soup.find('h1').text
print(f"Title: {title}")  # 'Web scraping'이라는 제목을 출력합니다.

# 4. 모든 <p> 태그 (단락) 추출
# soup.find_all()은 HTML 문서에서 지정된 모든 태그를 찾는 메서드입니다. 여기서는 <p> 태그 (단락)를 모두 찾습니다.
# Wikipedia 문서에서는 <p> 태그가 단락을 나타내며, 웹 페이지의 본문 내용이 포함되어 있습니다.
# find_all()은 리스트를 반환하므로, 추출된 <p> 태그들을 하나씩 처리하기 위해 for 루프를 사용합니다.
paragraphs = soup.find_all('p')

# 5. 각 단락의 내용을 출력
# enumerate() 함수는 반복문에서 인덱스와 해당 요소를 함께 반환해줍니다. 여기서 i는 인덱스(1부터 시작), paragraph는 <p> 태그입니다.
# paragraph.text는 <p> 태그 내의 텍스트만을 추출합니다.
# 텍스트의 처음 100글자만 출력하기 위해 슬라이싱 [:100]을 사용합니다. 그 뒤에 '...'을 붙여 전체 텍스트가 아닌 일부만 출력되었음을 나타냅니다.
for i, paragraph in enumerate(paragraphs, 1):
    print(f"Paragraph {i}: {paragraph.text[:100]}...")  # 처음 100글자만 출력
