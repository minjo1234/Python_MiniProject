from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

options = webdriver.ChromeOptions()
options.add_experimental_option(
    "excludeSwitches" , ["enable-logging"])

driver = webdriver.Chrome(options=options)


try:
    driver.get('https://flight.naver.com/')

    begin_date = driver.find_element(By.XPATH , '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]')
    begin_date.click()

    day27 = driver.find_element(By.XPATH , '//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[4]/button')
    day27.click()

    day31 = driver.find_element(By.XPATH , '//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[6]/td[1]/button')
    day31.click()


    try: 
        depart_state = driver.find_element(By.XPATH , '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[1]/i').click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH ,'//*[@id="__next"]/div/div[1]/div[10]/div[2]/section/section/button[1]')))
        select_depart = driver.find_element(By.XPATH , '//*[@id="__next"]/div/div[1]/div[10]/div[2]/section/section/button[1]').click()
        select_depart2 = driver.find_element(By.XPATH , '//*[@id="__next"]/div/div[1]/div[10]/div[2]/section/section/div/button[3]').click()
    except Exception as err :
        print(err)

    try:
        domestic = driver.find_element(By.XPATH , '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]/i').click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH ,'//*[@id="__next"]/div/div[1]/div[10]/div[2]/section/section/button[1]')))
        select_domestic = driver.find_element(By.XPATH , '//*[@id="__next"]/div/div[1]/div[10]/div[2]/section/section/button[1]').click()
        select_domestic2 = driver.find_element(By.XPATH ,'//*[@id="__next"]/div/div[1]/div[10]/div[2]/section/section/div/button[2]').click()        
    except Exception as err :
        print(err)
        
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH ,'//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/button/span')))

    search = driver.find_element(By.XPATH , '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/button/span').click()

    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH ,'//*[@id="__next"]/div/div[1]/div[6]/div/div[2]/div[5]/div')))

    print(elem.text)
    
except Exception as arr :
    print(arr)