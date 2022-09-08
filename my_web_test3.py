"""
Native App 다루기.

전화걸기

"""

from appium import webdriver
import time
from appium.webdriver import appium_service
from selenium.webdriver.support.select import Select  # drop-down 에서 선택하는 거 구현할때.

my_desired_caps = dict(

    deviceName='R3CM801B9CX', # 삼성폰, adb devices 로 알아낸 이름
    # deviceName='Android', # 이렇게 해도 되긴 되는구나
    platformName='Android',

    
    # adb shell 에서 가져온 전화걸기 앱 정보 :: com.samsung.android.dialer/.DialtactsActivity
    appPackage='com.samsung.android.dialer',
    appActivity='.DialtactsActivity'
)


APPIUM_SERVER_PORT = 4723
appium_local_server = f'http://127.0.0.1:{APPIUM_SERVER_PORT}'


## 이렇게만 해도, 전화걸기 앱이 실행된다.
driver = webdriver.Remote(f'{appium_local_server}/wd/hub' , desired_capabilities=my_desired_caps ) 


time.sleep(2)
driver.quit()

