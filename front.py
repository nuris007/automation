from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# 스크롤 맨 아래로 내렸다 올로기
def scrolls():
    # 스크롤 내리기
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(2)
    # 스크롤 올리기
    driver.execute_script("window.scrollTo(0,0);")
    time.sleep(2)

# 새 창 선택 > 새창 종료 > 기존창 선택 
def new_tabs():
    # 새 창 선택
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    driver.close()
    time.sleep(2)
    # 기존 창 선택하기
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)


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

#최상단 [호스트 지원] 버튼 선택
driver.find_elements_by_css_selector('.GlobalNavigationBar__TopNavMenu-og74wb-4.kgHgrk')[0].click()
time.sleep(2)
# 새 창 선택 > 새창 종료 > 기존창 선택 함수
new_tabs()

#최상단 [자주 묻는 질문] 버튼 선택
driver.find_elements_by_css_selector('.GlobalNavigationBar__TopNavMenu-og74wb-4.kgHgrk')[2].click()
time.sleep(2)
driver.find_elements_by_css_selector('.FAQEntity__TitleWrapper-cpxlp5-0.ldvBHS')[0].click()
time.sleep(2)
driver.back()
time.sleep(2)

#최상단 [공지사항] 버튼 선택
driver.find_elements_by_css_selector('.GlobalNavigationBar__TopNavMenu-og74wb-4.kgHgrk')[3].click()
time.sleep(2)
driver.find_elements_by_css_selector('.NoticeEntity__Title-sc-1x9h6uc-2.ipMFPV')[0].click()
time.sleep(2)
driver.back()
time.sleep(2)

# 카테고리 버튼 선택
driver.find_elements_by_css_selector('.GlobalNavigationBar__IconWrapper-og74wb-11.bXkqmJ')[0].click()
time.sleep(2)
driver.find_elements_by_css_selector('.CategoryItem__TextDeemed-sc-7y9o4v-3.fjwRlv')[0].click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.back()
time.sleep(2)

# 피드 버튼 선택
driver.find_elements_by_css_selector('.GlobalNavigationBar__IconWrapper-og74wb-11.bXkqmJ')[1].click()
time.sleep(5)
driver.find_elements_by_css_selector('.FeedImage__Wrapper-sc-1g1oaf4-0.jGjBCL')[0].click()
time.sleep(5)
driver.find_element_by_css_selector('.close_1x3s325').click()
time.sleep(2)
driver.find_elements_by_css_selector('.ProductLink__Wrapper-sc-1agbsre-0.ittDAj.CardFeed__StyledProductLink-sc-1hnsnr8-1.ePVeWN')[0].click()
time.sleep(3)
driver.back()
time.sleep(2)
driver.back()
time.sleep(2)

# 저장 하고 저장 취소
# 홈에서 첫번째 상품 저장
driver.find_elements_by_css_selector('.Button-bqxlp0-0.ButtonWish__StyledButton-sc-7k8l60-0.dXNbSn.enp_mobon_cart')[0].click()
time.sleep(3)
# 홈에서 첫번째 상품 상세 진입
driver.find_elements_by_css_selector('.CardProduct__InfoWrapper-a817d1-1.hPIfDi')[0].click()
time.sleep(3)
# 첫번째 상품 상세 진입 > 호스트 저장 버튼 선택
driver.find_element_by_css_selector('.Button-bqxlp0-0.ButtonWish__StyledButton-sc-7k8l60-0.eZGjgL.enp_mobon_cart').click()
time.sleep(3)
driver.back()
time.sleep(3)

# 홈에서 두번째 상품 상세 진입
driver.find_elements_by_css_selector('.CardProduct__InfoWrapper-a817d1-1.hPIfDi')[1].click()
time.sleep(3)
# 상세에서 상품 저장 버튼 선택
driver.find_element_by_css_selector('.SaveActionButton__Button-sc-18l2t54-0.dQtonX.enp_mobon_cart').click()
time.sleep(5)
# 상세에서 호스트 버튼 선택해서 호스트 상세 진입
driver.find_element_by_css_selector('.Profile__ProfileImage-sc-18xe7ny-3.hEglGi').click()
time.sleep(3)
# 호스트 상세에서 호스트 저장 버튼 선택
driver.find_element_by_css_selector('.Button-bqxlp0-0.ButtonWish__StyledButton-sc-7k8l60-0.eZGjgL.enp_mobon_cart').click()
time.sleep(3)
driver.back()
time.sleep(2)
driver.back()
time.sleep(2)
# 홈에서 상단 저장 버튼 선택
driver.find_elements_by_css_selector('.GlobalNavigationBar__IconWrapper-og74wb-11.bXkqmJ')[2].click()
time.sleep(3)
# 저장 > 호스트 탭 선택
driver.find_element_by_css_selector('.Button-bqxlp0-0.NavigationButton__StyledButton-sc-121z7og-0.NbmIN').click()
time.sleep(3)
# 호스트 저장 목록에서 첫번째 호스트 저장 취소
driver.find_elements_by_css_selector('.Button-bqxlp0-0.ButtonWish__StyledButton-sc-7k8l60-0.eZGjgL.enp_mobon_cart')[0].click()
time.sleep(3)
# 호스트 저장 목록에서 두번째 호스트 상세 진입
driver.find_elements_by_css_selector('.Ratio-ratio')[1].click()
time.sleep(3)
# 호스트 상세에서 호스트 저장 해제 버튼 선택
driver.find_element_by_css_selector('.Button-bqxlp0-0.ButtonWish__StyledButton-sc-7k8l60-0.eZGjgL.enp_mobon_cart').click()
time.sleep(3)
driver.back()
time.sleep(3)
# 새로고침
driver.refresh()
time.sleep(3)
# 저장 > 프립탭 선택
driver.get("https://staging.frip.co.kr/my/wishes/frip")
time.sleep(2)
# 프립 저장 목록에서 첫번째 프립 저장 해제
driver.find_elements_by_css_selector('.Button-bqxlp0-0.ButtonWish__StyledButton-sc-7k8l60-0.dXNbSn.enp_mobon_cart')[0].click()
time.sleep(3)
# 프립 저장 목록에서 두번째 프립 상세 진입
driver.find_elements_by_css_selector('.Ratio-ratio')[1].click()
time.sleep(3)
# 프립 상세에서 프립 저장 해제 버튼 선택
driver.find_element_by_css_selector('.SaveActionButton__Button-sc-18l2t54-0.dQtonX.enp_mobon_cart').click()
time.sleep(3)
driver.back()
time.sleep(2)
# 프립 로고 선택해서 홈으로 이동해서 첫번째 두번째 프립 저장 해제 확인
driver.find_element_by_css_selector('.GlobalNavigationBar__MainLogo-og74wb-13.butSez').click()
time.sleep(3)

# 홈에서 첫번째 상품 상세 진입하여 프립과 호스트 저장 해제 확인
driver.find_elements_by_css_selector('.CardProduct__InfoWrapper-a817d1-1.hPIfDi')[0].click()
time.sleep(5)
driver.back()
time.sleep(2)
# 홈에서 두번째 상품 상세 진입하여 프립과 호스트 저장 해제 확인
driver.find_elements_by_css_selector('.CardProduct__InfoWrapper-a817d1-1.hPIfDi')[1].click()
time.sleep(5)
driver.back()
time.sleep(2)

#메인배너 전체보기 > 첫번째 배너 선택
driver.find_element_by_css_selector('.BannerInfoButton__Button-cnb5ia-0.gdRosb').click()
time.sleep(3)
action.key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.ENTER).perform()
time.sleep(2)
driver.back()
time.sleep(2)

# # 서브 배너 선택 후 새 창 닫기
# driver.find_element_by_css_selector('.slick-slider.ImageSlider__StyledSlider-sc-1obm2ug-1.pFyVo.slick-initialized').click()
# time.sleep(2)
# driver.back()
# time.sleep(2)

# 새 창 선택 > 새창 종료 > 기존창 선택 함수
# new_tabs()

#리플래시
driver.refresh()
time.sleep(2)

#숏컷 10개 진입
i=0
while i < 10:
    driver.find_elements_by_css_selector('.Image__StyledImage-v97gyx-1.VUNpu')[i].click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    i = i+1


#컨텐츠 전체보기 > 첫번째 프립 선택
i=0
while i < 6:
    if i != 2:
        driver.find_elements_by_css_selector('.ProductSectionHeader__LinkWrapper-sc-1lmfow6-4.iQnPKA')[i].click()
        time.sleep(3)
        driver.find_elements_by_css_selector('.Image__StyledImage-v97gyx-1.VUNpu')[0].click()
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.back()
        time.sleep(3)
    else :
        driver.find_elements_by_css_selector('.ProductSectionHeader__LinkWrapper-sc-1lmfow6-4.iQnPKA')[i].click()
        time.sleep(3)
        driver.find_element_by_css_selector('.Fade__Wrapper-sc-1s0ipfq-0.koasSX').click()
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.back()
        time.sleep(3)
    i = i+1

# 프립 호스트 지원 배너 선택 후 새창 닫기
driver.find_element_by_css_selector('.HostBanner__BannerImage-sc-15wm6s2-1.eaJzkp').click()
time.sleep(2)
# 새 창 선택 > 새창 종료 > 기존창 선택 함수
new_tabs()

# 매거진
driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[9]/div/header/a').click()
time.sleep(2)
driver.find_elements_by_css_selector('.MagazineListPage__MagazineWrapper-hh1ck3-2.jZtIEr')[0].click()
time.sleep(2)
driver.back()
time.sleep(3)
driver.back()
time.sleep(3)

# 새로고침
driver.refresh()
time.sleep(3)
# 새로고침
driver.refresh()
time.sleep(3)
scrolls()

#-------------------------------------------------------------------------------------------
# 상세페이지 진입 (날짜 조율형)
driver.get("https://staging.frip.co.kr/products/158832")
time.sleep(5)

#스크롤 맨 아래로 내렸다 맨위로 올리는 함수
scrolls()

# 참여하기 선택
driver.find_element_by_css_selector('.Button-bqxlp0-0.cKPTge.Button__StyledSubmitButton-sc-1dkzbac-0.eIJDxV').click()
time.sleep(3)

# 옵션 선택
driver.find_elements_by_css_selector('.sc-fzplWN.hXZweA')[0].click()
time.sleep(3)

# 옵션 타이틀까지 스크롤
scrolllist1 = driver.find_element_by_class_name('ProductOptionPage__Title-sc-1jhikr6-3.hKCubr')
driver.execute_script("arguments[0].scrollIntoView(true);", scrolllist1)
time.sleep(3)

# 다음 버튼 선택
driver.find_element_by_css_selector('.sc-fzoXWK.hnKkAN').click()
time.sleep(5)

# 추가정보1 입력창 찾아서 답변 입력
driver.find_elements_by_css_selector('.Text__Textarea-odx25q-0.gdXJEj')[0].send_keys('추가질문 입력 테스트 길게 짤게')
time.sleep(2)

# 추가정보2 입력창 찾아서 답변 입력
driver.find_elements_by_css_selector('.Text__Textarea-odx25q-0.gdXJEj')[1].send_keys('원투쓰립ㅈㄷㄱ쇼ㅛㅑㅕㅐㅑㅕㅑㅐㅐㅑㅁㄴ아ㅠㅜㄴ머ㅏ어휴ㅣㅏㅁㄴ크ㅜㅌ츄ㅡㅜㅠㅊㅌㅋ!@#$%^&qwerytyuiiopolkjhgfdfdsa;')
time.sleep(2)

# 다음 버튼 선택
driver.find_element_by_css_selector('.Button-bqxlp0-0.cKPTge').click()
time.sleep(2)

# 옵션 타이틀까지 스크롤
scrolllist2 = driver.find_elements_by_class_name('PageTitle__PurchasePageTitle-ex62ss-0.jcPaBR')[2]
driver.execute_script("arguments[0].scrollIntoView(true);", scrolllist2)
time.sleep(3)

# 에너지 전체 사용 버튼 선택
driver.find_elements_by_css_selector('.InnerActionButton-io567l-0.cVMMHP')[3].click()
time.sleep(3)

# 에너지까지 스크롤
scrolllist3 = driver.find_element_by_class_name('SubTitle-eeu9i7-0.AmountHeldSubTitle__Wrapper-ldhy4b-0.kTpLsm')
driver.execute_script("arguments[0].scrollIntoView(true);", scrolllist3)
time.sleep(3)

# 이번 프립은 누구랑 하시나요?? 선택
i=0
while  i < 4 :
    if i == 0 :
        driver.find_elements_by_class_name('CrewCollection__Chip-leein5-4.sTDkW')[i].click()
        time.sleep(1)
        driver.find_elements_by_class_name('CrewCollection__Chip-leein5-4.sTDkW')[i].click()
        time.sleep(1)
        i = i+1
    else :
        driver.find_elements_by_class_name('CrewCollection__Chip-leein5-4.sTDkW')[i].click()
        time.sleep(1)
        i = i+1

# 결제하기 버튼 선택
driver.find_element_by_css_selector('.Button-bqxlp0-0.cKPTge').click()
time.sleep(6)

# 확인 버튼 선택
driver.find_element_by_css_selector('.Button-bqxlp0-0.dKEMjR').click()
time.sleep(2)

# 구매한 상품의 결제 상세 내역 선택 (결제 내역에 첫번째 결제 상세 내역 선택)
driver.find_elements_by_css_selector('.Outlined__Button-qqupyj-0.eAbBXA')[0].click()
time.sleep(2)

# 결제정보 타이틀까지 스크롤
scrolllist1 = driver.find_element_by_class_name('PurchaseInfo__Title-sc-1hkn4jd-1.fgJUxE')
driver.execute_script("arguments[0].scrollIntoView(true);", scrolllist1)
time.sleep(2)

# 결제 취소 버튼 선택
driver.find_element_by_css_selector('.FloatingButton__Button-zus21a-4.giUjCo').click()
time.sleep(5)

# 한번 더 결제 취소 버튼 선택
driver.find_element_by_css_selector('.FloatingButton__Button-zus21a-4.giUjCo').click()
time.sleep(2)

# 확인 버튼 선택
driver.find_element_by_css_selector('.Button-bqxlp0-0.Dialog__StyledButton-sc-16kwpqb-7.erqVDZ').click()
time.sleep(3)

# 마이 버튼 선택
driver.find_elements_by_css_selector('.GlobalNavigationBar__IconWrapper-og74wb-11.bXkqmJ')[3].click()
time.sleep(2)


#-------------------------------------------------------------------------------------------
# 상세페이지 진입 (날짜 조율형)
driver.get("https://staging.frip.co.kr/products/162514")
time.sleep(2)

#스크롤 맨 아래로 내렸다 맨위로 올리는 함수
scrolls()

# 참여하기 선택
driver.find_element_by_css_selector('.Button-bqxlp0-0.cKPTge.Button__StyledSubmitButton-sc-1dkzbac-0.eIJDxV').click()
time.sleep(3)

# 다음달 > 버튼 선택
driver.find_element_by_css_selector('.Navigator__IconArrowRight-mpcfrj-0.fLGRFD').click()
time.sleep(3)

# 3번째 날짜 선택
driver.find_elements_by_css_selector('.CalendarDay__CalendarDayBg-sc-1wu1mgi-1.dVIQcN')[2].click()
time.sleep(3)

# 시간 선택
driver.find_element_by_css_selector('.sc-fznyAO.CWQMf').click()
time.sleep(3)

# 아이템 선택
driver.find_elements_by_css_selector('.sc-fznyAO.CWQMf')[2].click()
time.sleep(3)

# 옵션 타이틀까지 스크롤
scrolllist1 = driver.find_element_by_class_name('ProductOptionPage__Title-sc-1jhikr6-3.hKCubr')
driver.execute_script("arguments[0].scrollIntoView(true);", scrolllist1)
time.sleep(3)

# 다음 버튼 선택
driver.find_element_by_css_selector('.sc-fzoXWK.hnKkAN').click()
time.sleep(5)

# # 추가정보1 입력창 찾아서 답변 입력
# driver.find_elements_by_css_selector('.Text__Textarea-odx25q-0.gdXJEj')[0].send_keys('추가질문 입력 테스트 길게 짤게')
# time.sleep(2)

# # 추가정보2 입력창 찾아서 답변 입력
# driver.find_elements_by_css_selector('.Text__Textarea-odx25q-0.gdXJEj')[1].send_keys('원투쓰립ㅈㄷㄱ쇼ㅛㅑㅕㅐㅑㅕㅑㅐㅐㅑㅁㄴ아ㅠㅜㄴ머ㅏ어휴ㅣㅏㅁㄴ크ㅜㅌ츄ㅡㅜㅠㅊㅌㅋ!@#$%^&qwerytyuiiopolkjhgfdfdsa;')
# time.sleep(2)

# # 다음 버튼 선택
# driver.find_element_by_css_selector('.Button-bqxlp0-0.cKPTge').click()
# time.sleep(2)

# 옵션 타이틀까지 스크롤
scrolllist2 = driver.find_elements_by_class_name('PageTitle__PurchasePageTitle-ex62ss-0.jcPaBR')[2]
driver.execute_script("arguments[0].scrollIntoView(true);", scrolllist2)
time.sleep(3)

# 에너지 전체 사용 버튼 선택
driver.find_elements_by_css_selector('.InnerActionButton-io567l-0.cVMMHP')[3].click()
time.sleep(3)

# 에너지까지 스크롤
scrolllist3 = driver.find_element_by_class_name('SubTitle-eeu9i7-0.AmountHeldSubTitle__Wrapper-ldhy4b-0.kTpLsm')
driver.execute_script("arguments[0].scrollIntoView(true);", scrolllist3)
time.sleep(3)

# 이번 프립은 누구랑 하시나요?? 선택
i=0
while  i < 4 :
    if i == 0 :
        driver.find_elements_by_class_name('CrewCollection__Chip-leein5-4.sTDkW')[i].click()
        time.sleep(1)
        driver.find_elements_by_class_name('CrewCollection__Chip-leein5-4.sTDkW')[i].click()
        time.sleep(1)
        i = i+1
    else :
        driver.find_elements_by_class_name('CrewCollection__Chip-leein5-4.sTDkW')[i].click()
        time.sleep(1)
        i = i+1

# 결제하기 버튼 선택
driver.find_element_by_css_selector('.Button-bqxlp0-0.cKPTge').click()
time.sleep(6)

# 확인 버튼 선택
driver.find_element_by_css_selector('.Button-bqxlp0-0.dKEMjR').click()
time.sleep(2)

# 구매한 상품의 결제 상세 내역 선택 (결제 내역에 첫번째 결제 상세 내역 선택)
driver.find_elements_by_css_selector('.Outlined__Button-qqupyj-0.eAbBXA')[0].click()
time.sleep(2)

# 결제정보 타이틀까지 스크롤
scrolllist1 = driver.find_element_by_class_name('PurchaseInfo__Title-sc-1hkn4jd-1.fgJUxE')
driver.execute_script("arguments[0].scrollIntoView(true);", scrolllist1)
time.sleep(2)

# 결제 취소 버튼 선택
driver.find_element_by_css_selector('.FloatingButton__Button-zus21a-4.giUjCo').click()
time.sleep(5)

# 한번 더 결제 취소 버튼 선택
driver.find_element_by_css_selector('.FloatingButton__Button-zus21a-4.giUjCo').click()
time.sleep(2)

# 확인 버튼 선택
driver.find_element_by_css_selector('.Button-bqxlp0-0.Dialog__StyledButton-sc-16kwpqb-7.erqVDZ').click()
time.sleep(3)

# 마이 버튼 선택
driver.find_elements_by_css_selector('.GlobalNavigationBar__IconWrapper-og74wb-11.bXkqmJ')[3].click()
time.sleep(3)

# 프로필 버튼 선택
driver.find_element_by_css_selector('.UserInfo__Nickname-bt0psx-3.hewsYu').click()
time.sleep(3)
driver.back()
time.sleep(3)

# 에너지 버튼 선택
i = 0 
while i < 4 :
    if i == 0 or i == 1 :
        # 쿠폰 or 에너지 진입
        driver.find_elements_by_css_selector('.UserProperty__Value-xpx7mx-1.yiVA-d')[i].click()
        time.sleep(2)
        # 입력창 선택해서 잘못된 쿠폰코드 입력
        driver.find_element_by_css_selector('.TextField__Input-sc-1l9o56e-2.gGztpV').send_keys('asjkdh12')
        time.sleep(2)
        # 확인 버튼 선택
        driver.find_element_by_css_selector('.Outlined__Button-qqupyj-0.kpRdoO').click()
        time.sleep(2)
        driver.back()
        time.sleep(2)
        i = i+1 
    else :
        # 후기 or 피드 진입
        driver.find_elements_by_css_selector('.UserProperty__Value-xpx7mx-1.yiVA-d')[i].click()
        time.sleep(2)
        driver.back()
        time.sleep(2)
        i = i+1

driver.refresh()
time.sleep(3)

# 배지 영역 선택
driver.find_element_by_css_selector('.FripBadge__Container-sc-1symmx5-0.juuNtL').click()
time.sleep(2)
# 배지 첫 진입 팝업 확인 선택
driver.find_element_by_css_selector('.Dialog__Button-sc-1kekiyi-3.kTpwga').click()
time.sleep(2)
scrolls()
driver.back()
time.sleep(2)

# 결제 내역 
driver.find_elements_by_css_selector('.TableRow__ContentWrapper-j0fs67-0.jfwBqf')[0].click()
time.sleep(2)
driver.back()
time.sleep(2)

# 친구초대 
driver.find_elements_by_css_selector('.TableRow__ContentWrapper-j0fs67-0.jfwBqf')[1].click()
time.sleep(2)
# 나의 초대코드 까지 스크롤
scrolllist5 = driver.find_element_by_class_name('MyInvitationCode__Title-b21wr4-1.kEzmUu')
driver.execute_script("arguments[0].scrollIntoView(true);", scrolllist5)
time.sleep(3)
# 초대코드 복사 버튼 선택
driver.find_element_by_class_name('CopyInvitationCodeButton__Button-lgen25-0.TDSgM').click()
time.sleep(3)
# # 여기 버튼 선택
# driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[5]/button').click()
# time.sleep(5)
# # 초대 코드 입력란 선택해서 코드 입력 후 엔터
# driver.find_element_by_css_selector('.Form__Input-sc-1quypp7-1.koBbgS').send_keys('asjkdh12')
# time.sleep(2)
# action.key_down(Keys.ENTER).perform()
# time.sleep(3)
driver.back()
time.sleep(2)
# # 새로고침
# driver.refresh()
# time.sleep(3)

# 공지사항
driver.find_elements_by_css_selector('.TableRow__ContentWrapper-j0fs67-0.jfwBqf')[2].click()
time.sleep(2)
driver.find_elements_by_css_selector('.NoticeEntity__Title-sc-1x9h6uc-2.ipMFPV')[0].click()
time.sleep(2)
driver.back()
time.sleep(2)

# FAQ
driver.find_elements_by_css_selector('.TableRow__ContentWrapper-j0fs67-0.jfwBqf')[3].click()
time.sleep(2)
driver.find_elements_by_css_selector('.FAQEntity__TitleWrapper-cpxlp5-0.ldvBHS')[0].click()
time.sleep(2)
driver.back()
time.sleep(2)

# 고객센터 문의
driver.find_elements_by_css_selector('.TableRow__ContentWrapper-j0fs67-0.jfwBqf')[4].click()
time.sleep(2)
driver.find_element_by_css_selector('.New__Button-sc-17rcq7-7.ebDrPW').click()
time.sleep(2)
driver.back()
time.sleep(2)

# 호스트 지원, 제휴 및 제한 선택 후 새창 닫기 
i=5
while i < 7 :
    driver.find_elements_by_css_selector('.TableRow__ContentWrapper-j0fs67-0.jfwBqf')[i].click()
    time.sleep(2)
    # 새 창 선택 > 새창 종료 > 기존창 선택 함수
    new_tabs()
    i = i+1

# 설정
driver.find_elements_by_css_selector('.TableRow__ContentWrapper-j0fs67-0.jfwBqf')[7].click()
time.sleep(3)
driver.back()
time.sleep(2)

# 약관 및 정책
driver.find_elements_by_css_selector('.TableRow__ContentWrapper-j0fs67-0.jfwBqf')[8].click()
time.sleep(3)
i=0
while i < 3 :
    driver.find_elements_by_css_selector('.TableRow__ContentWrapper-j0fs67-0.jfwBqf')[i].click()
    time.sleep(3)
    #스크롤 맨 아래로 내렸다 맨위로 올리는 함수
    scrolls()
    time.sleep(2)
    driver.back()
    time.sleep(2)
    i = i+1

driver.back()
time.sleep(3)

# 로그아웃 하기
driver.find_element_by_css_selector('.GlobalNavigationBar__LogoutButton-og74wb-5.jfHerU').click()
time.sleep(3)