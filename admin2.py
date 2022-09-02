from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time


driver = webdriver.Chrome('./chromedriver')
driver.get("https://admin-v3-dev.frip.co.kr/login")
driver.maximize_window()
time.sleep(2)
action = ActionChains(driver)


# 아이디 입력
driver.find_elements_by_css_selector('.form-control')[0].send_keys('nuri@frientrip.com')
time.sleep(2)
#패스워드 입력
driver.find_elements_by_css_selector('.form-control')[1].send_keys('kobe3815!@')
time.sleep(2)
#로그인 버튼 클릭
driver.find_element_by_css_selector('.btn.frip-button.my-4.btn-frip-primary').click()
time.sleep(5)

# # 판매 등록 페이지 진입
# driver.get("https://admin-v3-dev.frip.co.kr/product/list")
# time.sleep(2)


#프립 목록에서 해당 프립 선택
driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div/div[2]/div[2]/div[2]/div/div[3]/table/tbody/tr[2]/td[2]/div/a').click()
time.sleep(2)
# # tabs = driver.window_handles
# # print(tabs)
# element = driver.find_elements_by_css_selector('.cell.el-tooltip')[2]
# driver.execute_script("arguments[0].click;",element)
# # time.sleep(2)


#[검수] 버튼 선택
driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div/div[2]/div[2]/button[2]').click()
time.sleep(3)


driver.find_element_by_xpath('//*[@id="__BVID__887___BV_modal_body_"]/div/div/div[2]/button[2]').click()
time.sleep(3)
# #[확인] 버튼 선택
# action.key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.RIGHT).key_down(Keys.LEFT).perform()
# action.reset_actions()
# time.sleep(3)