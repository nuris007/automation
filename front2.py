from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

CHROME_DRIVER_PATH = "./chromedriver"
url = 'https://staging.frip.co.kr/'


option = Options()
option.add_experimental_option("prefs", {
"profile.default_content_setting_values.notifications": 1
})

#위에 옵션 이용해서 권한 알립 팝업 종료시키고 사이트 열기
driver = webdriver.Chrome(chrome_options=option, executable_path=CHROME_DRIVER_PATH)
driver.get(url)
time.sleep(2)

action = ActionChains(driver)

#윈도우창 최대
driver.maximize_window()
time.sleep(2)

#메인 팝업 종료
driver.find_element_by_css_selector('.TextButton-sc-175c9eu-0.pGWkJ').click()
time.sleep(3)

#로그인 버튼 선택
driver.find_elements_by_css_selector('.GlobalNavigationBar__TopNavMenu-og74wb-4.kgHgrk')[2].click()
time.sleep(2)

#ID 입력창 찾아서 ID 입력
driver.find_element_by_css_selector('.Form__Input-sc-1quypp7-1.iRBMai').send_keys('qa_user3@frientrip.com')
time.sleep(2)


#PW 입력창 찾아서 PW 입력
driver.find_elements_by_css_selector('.Form__Input-sc-1quypp7-1.iRBMai')[1].send_keys('frip1234!!')
time.sleep(2)

#로그인 버튼 선택
driver.find_element_by_css_selector('.Button-bqxlp0-0.dDCuWg').click()
time.sleep(5)

# 서브 배너 선택 후 새 창 닫기
driver.find_element_by_css_selector('.slick-slider.ImageSlider__StyledSlider-sc-1obm2ug-1.pFyVo.slick-initialized').click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
driver.close()
time.sleep(2)

# 기존 창 선택하기
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)

#숏컷 10개 진입
i=0
while i < 10:
    driver.find_elements_by_css_selector('.Image__StyledImage-v97gyx-1.VUNpu')[i].click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    i = i+1
