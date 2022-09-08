"""
크롬 브라우저로 wikipedia 들어가서, 언어선택에서 다른나라 언어 고르는거 구현

드랍다운 , 드랍다운에서 select

"""

from appium import webdriver
import time
from appium.webdriver import appium_service
from selenium.webdriver.support.select import Select  # drop-down 에서 선택하는 거 구현할때.

from appium.webdriver.appium_service import AppiumService, MAIN_SCRIPT_PATH # appium을 코드로 실행 시킬수 있다.



my_appium_server = AppiumService()
APPIUM_SERVER_PORT = '4723'



## 이거 그냥 쓰지 말자.###########################################
my_appium_server.start(args=['--address', '127.0.0.1', '--port', str(APPIUM_SERVER_PORT)] , node='/Users/seon-hyeongjo/.nvm/versions/node/v16.4.2/bin/node' , main_script = '/Users/seon-hyeongjo/.nvm/versions/node/v16.4.2/lib/node_modules/appium/lib/main.js' )   # 안되네.. 
print (my_appium_server.is_running)
print (my_appium_server.is_listening)
#################################################


my_desired_caps = dict(

    deviceName='R3CM801B9CX', # 삼성폰, adb devices 로 알아낸 이름
    # deviceName='Android', # 이렇게 해도 되긴 되는구나
    platformName='Android',
    browserName='Chrome'

)



appium_local_server = f'http://127.0.0.1:{APPIUM_SERVER_PORT}'

driver = webdriver.Remote(f'{appium_local_server}/wd/hub' , desired_capabilities=my_desired_caps )  # 현재 appium server 떠있는 포트

driver.get('http://wikipedia.org')

print (driver.title)




# dropdown = driver.find_element_by_id('searchLanguage')  # 이러면, 에러발생
dropdown = driver.find_element_by_css_selector('#searchLanguage')  # 이러면, 정상 작동.. 같은 엘리먼트라도, 선택 방법에 따라 다르구나

select = Select(dropdown)
select.select_by_value('hi') # html보면, 각 선택 가능한 언어마다 고유의 value가 있다. 그 값을 사용한다.



"""
find_element 와 find_elements 는 달라... find_elements 는 [] 를 반환한다.
"""
options = driver.find_elements_by_tag_name('option')  # 각 언어마다 option태그로 되어있다. option으로 보자


print (f'length of options : {len(options)}')

for option in options:

    text = option.text
    lang = option.get_attribute('lang')

    print (f'text : {text} , lang : {lang}')



time.sleep(2)

driver.quit()

my_appium_server.stop()