from selenium import webdriver

url = "https://www.naver.com"
#PhantomJS 드라이버 추출
#browser = webdriver.PhantomJS('C:/phantomjs-2.1.1-windows/bin/phantomjs.exe')
options = webdriver.ChromeOptions()
options.add_argument('headless')
browser= webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe", chrome_options=options)

#3초대기
browser.implicitly_wait(3)

#url 읽어들이기
browser.get(url)

#화면캡처
browser.save_screenshot('Websites.png')

#브라우저 종료
browser.quit()