from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

btn_book = 'book'#id
priceBook = 'price'#id
numX = 'input_value'#id
area_input = 'answer'#id
submit = 'solve'#id
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    btn_book = browser.find_element(By.ID, btn_book) #находит кнопку book
    # ждет появления нужной цены и кликает на кнопку
    priceBook = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, priceBook), '100'))
    btn_book.click()
    #находит цифру, скролит к ней и считает
    numX = browser.find_element(By.ID, numX)
    browser.execute_script("return arguments[0].scrollIntoView(true);", numX)
    numX=numX.text
    x = calc(numX)

    area_input = browser.find_element(By.ID, area_input)
    area_input.send_keys(x)

    submit = browser.find_element(By.ID, submit)
    submit.click()






finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()