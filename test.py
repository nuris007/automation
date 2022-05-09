from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = "./chromedriver"
url = 'https://beta.frip.co.kr'

option = Options()
option.add_experimental_option("prefs", {
"profile.default_content_setting_values.notifications": 1
})

#위에 옵션 이용해서 권한 알립 팝업 종료시키고 사이트 열기
driver = webdriver.Chrome(chrome_options=option, executable_path=CHROME_DRIVER_PATH)
driver.get(url)
time.sleep(2)

# #메인 팝업 종료
# driver.find_element_by_css_selector('.TextButton-sc-175c9eu-0.pGWkJ').click()


# time.sleep(3)

# #로그인 버튼 선택
driver.find_elements_by_css_selector('.GlobalNavigationBar__TopNavMenu-og74wb-4.kgHgrk')[2].click()
time.sleep(2)

# #ID 입력창 찾아서 ID 입력
driver.find_element_by_css_selector('.Form__Input-sc-1quypp7-1.iRBMai').send_keys('qa02@frientrip.com')
time.sleep(2)


# #PW 입력창 찾아서 PW 입력
driver.find_elements_by_css_selector('.Form__Input-sc-1quypp7-1.iRBMai')[1].send_keys('1234qwer!@')
time.sleep(2)

# #로그인 버튼 선택
driver.find_element_by_css_selector('.Button-bqxlp0-0.dDCuWg').click()
time.sleep(5)


#메인배너 전체보기 > 첫번째 배너 선택
driver.find_element_by_css_selector('.BannerInfoButton__Button-cnb5ia-0.gdRosb').click()
time.sleep(2)
driver.find_element_by_css_selector('.FullScreenWrapper-sc-1s73ffa-0.buhPvC').click()
time.sleep(2)
driver.back()

# 서브 배너 선택
driver.find_element_by_css_selector('.slick-slider.ImageSlider__StyledSlider-sc-1obm2ug-1.pFyVo.slick-initialized').click()
time.sleep(2)
driver.back()


#숏컷 10개 진입
i=0
while i < 10:
    driver.find_elements_by_css_selector('.Image__StyledImage-v97gyx-1.VUNpu')[i].click()
    time.sleep(2)
    driver.back()
    time.sleep(2)
    i = i+1


#컨텐츠 전체보기 > 첫번째 프립 선택
i=0
while i < 4:
    if i != 0:
        driver.find_elements_by_css_selector('.ProductSectionHeader__LinkWrapper-sc-1lmfow6-4.iQnPKA')[i].click()
        time.sleep(2)
        driver.find_elements_by_css_selector('.Image__StyledImage-v97gyx-1.VUNpu')[0].click()
        time.sleep(2)
        driver.back()
        time.sleep(2)
        driver.back()
        time.sleep(2)
    else :
        driver.find_elements_by_css_selector('.ProductSectionHeader__LinkWrapper-sc-1lmfow6-4.iQnPKA')[i].click()
        time.sleep(2)
        driver.find_element_by_css_selector('.Fade__Wrapper-sc-1s0ipfq-0.koasSX').click()
        time.sleep(2)
        driver.back()
        time.sleep(2)
        driver.back()
        time.sleep(2)
    i = i+1

# driver.find_elements_by_css_selector('.ProductSectionHeader__LinkWrapper-sc-1lmfow6-4.iQnPKA')[0].click()
# time.sleep(2)
# driver.find_elements_by_css_selector('.Fade__Wrapper-sc-1s0ipfq-0.koasSX')[0].click()
# time.sleep(2)
# driver.back()
# time.sleep(2)
# driver.back()
# time.sleep(2)

# driver.find_elements_by_css_selector('.ProductSectionHeader__LinkWrapper-sc-1lmfow6-4.iQnPKA')[1].click()
# time.sleep(2)
# driver.find_elements_by_css_selector('.Image__StyledImage-v97gyx-1.VUNpu')[0].click()
# time.sleep(2)
# driver.back()
# time.sleep(2)
# driver.back()
# time.sleep(2)

# driver.find_elements_by_css_selector('.ProductSectionHeader__LinkWrapper-sc-1lmfow6-4.iQnPKA')[2].click()
# time.sleep(2)
# driver.find_elements_by_css_selector('.Image__StyledImage-v97gyx-1.VUNpu')[0].click()
# time.sleep(2)
# driver.back()
# time.sleep(2)
# driver.back()
# time.sleep(2)

# driver.find_elements_by_css_selector('.ProductSectionHeader__LinkWrapper-sc-1lmfow6-4.iQnPKA')[3].click()
# time.sleep(2)
# driver.find_elements_by_css_selector('.Image__StyledImage-v97gyx-1.VUNpu')[0].click()
# time.sleep(2)
# driver.back()
# time.sleep(2)
# driver.back()
# time.sleep(2)


# 프립 호스트 지원 배너 선택 후 새창 닫기
driver.find_element_by_css_selector('.HostBanner__BannerImage-sc-15wm6s2-1.eaJzkp').click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
driver.close()

# 기존 창 선택하기
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)

# # 메인 화면 프립 상품 선택
# driver.find_elements_by_css_selector('.pureness__ImageWrapper-iebc1w-1.kzeAqh')[0].click()
# time.sleep(2)
# driver.back()
# time.sleep(2)

# 상세페이지 진입 (일정없는 프립)
driver.get("https://beta.frip.co.kr/products/131330")
time.sleep(2)

# 스크롤 내리기
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(2)

# 스크롤 올리기
driver.execute_script("window.scrollTo(0,0);")
time.sleep(2)

# 참여하기 선택
driver.find_element_by_css_selector('.Button-bqxlp0-0.cKPTge.Button__StyledSubmitButton-sc-1dkzbac-0.eIJDxV').click()
time.sleep(2)

# 옵션 선택
driver.find_element_by_css_selector('.sc-fzoLsD.chhiKR').click()
time.sleep(2)

# 다음 버튼 선택
driver.find_element_by_css_selector('.sc-fzoyTs.jZUSDr').click()
time.sleep(2)

# 추가정보1 입력창 찾아서 답변 입력
driver.find_elements_by_css_selector('.Text__Textarea-odx25q-0.emdYcF')[0].send_keys('추가질문 입력 테스트 길게 짤게')
time.sleep(2)

# 추가정보2 입력창 찾아서 답변 입력
driver.find_elements_by_css_selector('.Text__Textarea-odx25q-0.emdYcF')[1].send_keys('네')
time.sleep(2)

# 추가정보3 입력창 찾아서 답변 입력
driver.find_elements_by_css_selector('.Text__Textarea-odx25q-0.emdYcF')[2].send_keys('원투쓰립ㅈㄷㄱ쇼ㅛㅑㅕㅐㅑㅕㅑㅐㅐㅑㅁㄴ아ㅠㅜㄴ머ㅏ어휴ㅣㅏㅁㄴ크ㅜㅌ츄ㅡㅜㅠㅊㅌㅋ!@#$%^&qwerytyuiiopolkjhgfdfdsa;')
time.sleep(2)

# 다음 버튼 선택
driver.find_element_by_css_selector('.Button-bqxlp0-0.cKPTge').click()
time.sleep(2)

# 에너지 전체 사용 버튼 선택
driver.find_elements_by_css_selector('.InnerActionButton-io567l-0.cVMMHP')[2].click()
time.sleep(2)

# 결제하기 버튼 선택
driver.find_element_by_css_selector('.Button-bqxlp0-0.cKPTge').click()
time.sleep(5)

# 확인 버튼 선택
driver.find_element_by_css_selector('.Button-bqxlp0-0.dKEMjR').click()
time.sleep(2)


# 상세페이지 진입 (일정있는 프립)
driver.get("https://beta.frip.co.kr/products/131329")
time.sleep(2)

# 스크롤 내리기
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(2)

# 스크롤 올리기
driver.execute_script("window.scrollTo(0,0);")
time.sleep(2)

# 참여하기 선택
driver.find_element_by_css_selector('.Button-bqxlp0-0.cKPTge.Button__StyledSubmitButton-sc-1dkzbac-0.eIJDxV').click()
time.sleep(2)

# 다음달 > 버튼 선택
driver.find_element_by_css_selector('.Navigator__IconArrowRight-mpcfrj-0.fLGRFD').click()
time.sleep(2)

# 날짜 선택
driver.find_elements_by_css_selector('.CalendarDay__CalendarDayBg-sc-1wu1mgi-1.dVIQcN')[2].click()
time.sleep(2)

# 시간 선택
driver.find_element_by_css_selector('.sc-fzpans.cKJzHK').click()
time.sleep(2)

# 아이템 선택
driver.find_elements_by_css_selector('.sc-fzpans.cKJzHK')[2].click()
time.sleep(2)

# 다음 버튼 선택
driver.find_element_by_css_selector('.sc-fzoyTs.jZUSDr').click()
time.sleep(2)

# 에너지 전체 사용 버튼 선택
driver.find_elements_by_css_selector('.InnerActionButton-io567l-0.cVMMHP')[2].click()
time.sleep(2)

# 결제하기 버튼 선택
driver.find_element_by_css_selector('.Button-bqxlp0-0.cKPTge').click()
time.sleep(5)

# 확인 버튼 선택
driver.find_element_by_css_selector('.Button-bqxlp0-0.dKEMjR').click()
time.sleep(2)

# 확인 버튼 선택
driver.find_element_by_css_selector('.Button-bqxlp0-0.dKEMjR').click()
time.sleep(2)
