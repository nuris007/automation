"""
크롬 브라우저로 구글 사이트 들어가기
"""

from appium import webdriver
import time


my_desired_caps = dict(

deviceName='R3CM801B9CX', # 삼성폰, adb devices 로 알아낸 이름
# deviceName='Android', # 이렇게 해도 되긴 되는구나
platformName='Android',
browserName='Chrome'

)


appium_local_server = 'http://127.0.0.1:4723'

driver = webdriver.Remote(f'{appium_local_server}/wd/hub' , desired_capabilities=my_desired_caps )  # 현재 appium server 떠있는 포트

driver.get('http://www.google.com')

print (driver.title)

# driver.find_element_by 종류가 엄청 많다.. 이거 이용해서 element 찾으면 된다.
# driver.find_element_by_xpath("//*[@name='q']").send_keys("Hello Appium !!!")
# driver.find_element_by_css_selector("*[name='q']").send_keys("Hello Appium !!!")
# driver.find_element_by_name("q").send_keys("Hello Appium !!!")  # 이건 에러 남

time.sleep(2)

driver.quit()