from selenium import webdriver  # selenium pip install 필요
from bs4 import BeautifulSoup   # BeautifulSoup pip install 필요

# chromedrivwer의 위치 지정(없으면 인터넷에서 다운 필요)
path = "C:/selenium/chromedriver"

options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("disable-gpu")

driver = webdriver.Chrome(path, options=options)

# 스크래핑할 웹페이지 선택
url = "https://finance.naver.com/sise/sise_deal_rank.nhn"   #네이버 주식_외국인 순매수
driver.implicitly_wait(3)   #인터넷 로딩위해 3초 기다림

driver.get(url)
# driver.switch_to.frame("buy")   # 해당 표는 iframe으로 되어있기 때문에 iframe을 로딩시켜줌
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

def ago2_foreign_top5():
    i = 0 # Top5까지 자료 가져오기 위한 카운터
    data_foreign_top5 = []
    ago2_xpath1 = "/html/body/div/div/div/div[1]/table[2]/tbody/" # 어제 일자 외국인 상위매수 종목 앞 PATH