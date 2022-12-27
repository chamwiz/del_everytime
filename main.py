from selenium import webdriver
from selenium.webdriver.common.by import By

id = "test"
pw = "test"

# 에브리타임 로그인
driver = webdriver.Chrome()
driver.get("https://everytime.kr/login")
driver.find_element(By.XPATH,"//input[@name='userid']").send_keys(id)
driver.find_element(By.XPATH,"//input[@name='password']").send_keys(pw)
driver.find_element(By.XPATH,"//input[@type='submit']").click()
print()
# 내가 쓴 글 페이지 들어가기

# 상단 게시글 들어가기

# 삭제 버튼 누르기

# 팝업 확인
