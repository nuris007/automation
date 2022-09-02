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

# 판매 등록 페이지 진입
driver.get("https://admin-v3-dev.frip.co.kr/product/create")
time.sleep(2)

# 호스트 선택
driver.find_elements_by_css_selector('.form-control')[0].send_keys('qa05')
time.sleep(1)
driver.find_element_by_css_selector('.vbst-item.list-group-item.list-group-item-action').click()

#프립 유형 선택(오프라인)
driver.find_elements_by_css_selector('.my-2.col-lg-6.align-self-stretch')[0].click()
time.sleep(2)

#카테고리 선택 항목까지 스크롤
scrolllist1 = driver.find_elements_by_class_name('mt-3.pl-3.text-wrap.input-label-style')[3]
driver.execute_script("arguments[0].scrollIntoView(true);", scrolllist1)
time.sleep(2)

#카테고리 검색 라디오 버튼 선택
driver.find_element_by_xpath('//*[@id="category"]/div[2]').click()

#카테고리 입력 후 선택
driver.find_elements_by_css_selector('.form-control')[2].send_keys('서핑')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="__BVID__53"]/div/span/form/div[3]/div/div/div[2]/div/div/div/div[1]/div[2]/a[1]').click()
time.sleep(2)
action.key_down(Keys.TAB).perform()
action.reset_actions()

#프립 속성 선택
driver.find_elements_by_css_selector('.my-2.col-lg-6.align-self-stretch')[5].click()
time.sleep(2)

#프립명 입력
driver.find_elements_by_css_selector('.form-control')[4].send_keys('[QA]프립 자동화 테스트 입니다.11')

#진행 장소 항목까지 스크롤
scrolllist2 = driver.find_elements_by_class_name('btn.frip-button.float-right.btn-outline-frip-default.btn-md')[0]
driver.execute_script("arguments[0].scrollIntoView(true);", scrolllist2)
time.sleep(2)

#진행 장소 선택
driver.find_elements_by_css_selector('.btn.frip-button.float-right.btn-outline-frip-default.btn-md')[0].click()
time.sleep(5)

#팝업에서 장소 선택
driver.find_elements_by_css_selector('.text-frip-primary')[6].click()
time.sleep(2)

#[다음] 버튼 선택
#driver.find_element_by_css_selector('.btn.frip-button.btn-frip-primary.btn-tab').click()
driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div/div[2]/div[2]/button').click()
time.sleep(2)

#옵션 정보 입력까지 스크롤
scrolllist3 = driver.find_elements_by_class_name('text-sm.font-weight-bold.mr-2')[0]
driver.execute_script("arguments[0].scrollIntoView(true);", scrolllist3)
time.sleep(2)

#옵션 정보 입력
driver.find_elements_by_css_selector('.form-control')[10].send_keys('색')
driver.find_elements_by_css_selector('.form-control')[11].send_keys('노랑,빨강')
driver.find_element_by_css_selector('.btn.frip-button.my-3.btn-frip-primary.btn-tab').click()
time.sleep(2)
driver.find_elements_by_css_selector('.btn.frip-button.btn-outline-frip-default.btn-sm')[2].click()
time.sleep(2)
action.key_down(Keys.TAB).key_down(Keys.TAB).send_keys('1000').key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.ENTER).perform()
action.reset_actions()

#[다음] 버튼 선택
driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div/div[2]/div[2]/button[2]').click()
time.sleep(2)

#대표 이미지 업로드
driver.find_element_by_xpath('//*[@id="__BVID__213"]/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/div/div/div[1]/input').send_keys('/Users/nuri/Desktop/하자/스크린샷 2020-12-07 오후 5.29.13.png')
time.sleep(5)

#프립 상세 입력란 까지 스크롤
scrolllist3 = driver.find_elements_by_class_name('text-right.mb-2')[0]
driver.execute_script("arguments[0].scrollIntoView(true);", scrolllist3)
time.sleep(2)

#프립 상세 설명
driver.find_element_by_css_selector('.fr-element.fr-view').click()
time.sleep(2)
driver.find_element_by_css_selector('.fr-element.fr-view').send_keys('테스트 상품입니다.')
time.sleep(2)

#[다음] 버튼 선택
driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div/div[2]/div[2]/button[2]').click()
time.sleep(2)

#포함사항 설정
driver.find_element_by_xpath('//*[@id="__BVID__260"]/div/div/input').send_keys('재료비,케이크 상자,음료 1잔')
time.sleep(2)
driver.find_elements_by_css_selector('.btn.frip-button.mx-2.btn-frip-secondary')[0].click()

#스크롤_불불포함사항 까지
scrolllist4 = driver.find_elements_by_class_name('btn.frip-button.mx-2.btn-frip-secondary')[1]
time.sleep(2)
driver.execute_script("arguments[0].scrollIntoView(true);", scrolllist4)
time.sleep(2)

#불포함사항 설정
driver.find_element_by_xpath('//*[@id="__BVID__266"]/div/div/input').send_keys('교통바,의류 및 장비')
time.sleep(2)
driver.find_elements_by_css_selector('.btn.frip-button.mx-2.btn-frip-secondary')[1].click()
time.sleep(2)

#대원준비물 설정
driver.find_element_by_xpath('//*[@id="__BVID__272"]/div/div/input').send_keys('앞치마,볼펜')
time.sleep(2)
driver.find_elements_by_css_selector('.btn.frip-button.mx-2.btn-frip-secondary')[2].click()
time.sleep(2)

#[다음] 버튼 선택
driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div/div[2]/div[2]/button[2]').click()
time.sleep(3)

#[다음] 버튼 선택
driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div/div[2]/div[2]/button[2]').click()
time.sleep(3)

#[저장] 버튼 선택
driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div/div[2]/div[2]/span[2]/span[1]/button').click()
time.sleep(5)

#[검수요청] 버튼 선택
driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div/div[2]/div[2]/span[3]/button').click()
time.sleep(5)

#프립 목록에서 해당 프립 선택
driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div/div[2]/div[2]/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/div/a').click()
time.sleep(5)

driver.refresh()
time.sleep(3)

#[검수] 버튼 선택
driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div/div[2]/div[2]/button[2]').click()
time.sleep(5)

# [확인] 버튼 선택
# driver.find_elements_by_css_selector('.btn.frip-button.btn-frip-primary.btn-tab')[2].click()
driver.find_element_by_xpath('//*[@id="__BVID__87___BV_modal_body_"]/div/div/div[2]/button[1]').click()
time.sleep(3)

# action.key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.RIGHT).key_down(Keys.LEFT).perform()
# action.reset_actions()
# time.sleep(3)

