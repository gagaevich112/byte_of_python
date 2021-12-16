from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

number1 = 'num1'
number2 = 'num2'
select_drop = 'custom-select'
button = '.btn.btn-default'


try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)


    numX = browser.find_element(By.ID,number1)
    numberX = numX.text #ыбираем значение первого числа

    numY = browser.find_element(By.ID, number2)
    numberY = numY.text # выбираем значени второго числа

    numberZ = int(numberX) + int(numberY)

    selectX = Select(browser.find_element(By.CLASS_NAME, select_drop))
    selectX.select_by_value(str(numberZ))

    buttonX = browser.find_element(By.CSS_SELECTOR, button)
    buttonX.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()