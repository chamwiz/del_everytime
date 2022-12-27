from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

id = "test"
pw = "test"
# 삭제한 게시글 수
deleteCount = 0

# 에브리타임 로그인
driver = webdriver.Chrome()
driver.get("https://everytime.kr/login")
driver.find_element(By.XPATH,"//input[@name='userid']").send_keys(id)
driver.find_element(By.XPATH,"//input[@name='password']").send_keys(pw)
driver.find_element(By.XPATH,"//input[@type='submit']").click()

while True:
    try:
        # 내가 쓴 글 페이지 들어가기
        driver.get("https://everytime.kr/myarticle")
        # 상단 게시글 들어가기
        driver.implicitly_wait(10)
        driver.find_elements(By.CLASS_NAME,"article")[0].click()
        # 삭제 버튼 누르기
        driver.implicitly_wait(10)
        driver.find_element(By.CLASS_NAME,'del').click()
        # 팝업 확인
        driver.implicitly_wait(10)
        Alert(driver).accept()
        deleteCount += 1
    except:
        print("{}개의 게시글이 삭제됐습니다.".format(deleteCount))
        break

driver.quit()
