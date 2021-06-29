# Scraping



## 1. BeautifulSoup

- `request.text` 를 이용해 가져온 데이터는 텍스트 형태의 html 이다. 

- 텍스트 형태의 html을 객체 형태로 만들어서 원하는 요소에 접근할 수 있게 하는 것이 `BeautifulSoup`

- ```bash
  $ pip install beautifulsoup4
  ```

  

### 1-1) 사용법

```python
import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)

else : 
    print(response.status_code)
```



### 1-2) HTML 태그 이용: find()

- 함수 인자로 찾고자 하는 **태그**의 이름(name), 속성(attribute), 속성값(value)이 들어간다. 

- `find_all()` : 해당 조건에 맞는 모든 태그들을 가져온다.

- `find()`: 해당 조건에 맞는 하나의 태그를 가져온다. 중복이면 첫 번째 태그를 가져온다.

  - ```python
    tag = "<p class='chichi' id='1'> Hello World! </p>" 
    soup = BeautifulSoup(tag) 
    
    # 태그 이름만 특정 
    soup.find('p') 
    
    # 태그 속성만 특정 
    soup.find(class_='chichi') 
    soup.find(attrs = {'class':'chichi'}) 
    
    # 태그 이름과 속성 모두 특정 
    soup.find('p', class_='chichi')
    ```

  - ```python
    tag = "<p class='chichi' id='1'> Hello World! </p>" 
    soup = BeautifulSoup(tag) 
    object_tag = soup.find('p') 
    
    #태그의 이름 
    object_tag.name 
    #결과: 'p' 
    
    #태그에 담긴 텍스트 
    object_tag.text 
    #결과: ' Hello World! ' 
    
    #태그의 속성과 속성값 
    object_tag.attrs 
    #결과: {'class': ['chichi'], 'id': '1'}
    ```



### 1-3) CSS 태그 이용: select()

- `select()` 는 CSS selector로 해당 객체를 찾아 반환한다.

- `select()` == `find_all()`

- `select_one()` == `find()`

  - ```python
    # 태그 이름만 특정 
    soup.select_one('p') 
    
    # 태그 class 특정 
    soup.select_one('.chichi') 
    
    # 태그 이름과 class 모두 특정 
    soup.select_one('p.chichi')
    
    # 태그 id 특정 
    soup.select_one('#1') 
    
    # 태그 이름과 id 모두 특정 
    soup.select_one('p#1') 
    
    # 태그 이름과 class, id 모두 특정 
    soup.select_one('p.chichi#1')
    ```

- 직접 하위 경로를 지정할 수 있다.

  - ```python
    #find 
    soup.find('div').find('p') 
    
    #select 
    soup.select_one('div > p')
    ```





## 2. Selenium

- `beautifulsoup`만으로 자바스크립트가 동적으로 생성한 정보는 가져올 수 없는 한계가 있다.
- 이를 해결하기 위해 `selenium`이라는 웹 테스팅 프레임워크를 사용한다.
- web driver 라는 가상의 브라우저 프로그램(웹 테스트 도구)을 이용하여 동적인 작업을 구현한다.

- ```bash
  $ pip install selenium
  ```



### 2-1) 사용법

```python
from selenium import webdriver

path = "Webdriver 경로"
driver = webdriver.Chrome(path)

url = "https://www.naver.com"
driver.get(url)
```



### 2-2) 태그 찾기

- 태그명, id, class

- `driver.find_element_by_css_selector()`



### 2-3) 키 입력하기

- `send_keys('치치')`
