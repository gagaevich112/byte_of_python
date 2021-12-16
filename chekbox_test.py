

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

number = 'span#input_value'
input1 = 'answer' # id, поле для ввода
chekbox1 = 'robotCheckbox' #id, выбор чек бокса
radio1 = 'robotsRule' #id, выбор кнопки
submit = '.btn.btn-default' #css selector кнопка
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)


    x_element = browser.find_element(By.CSS_SELECTOR, number)
    x = x_element.text
    y = calc(x) #считает результат выражения

    field = browser.find_element(By.ID, input1)
    field.send_keys(y) #подставляет результат выражения

    chekbox = browser.find_element(By.ID, chekbox1)
    chekbox.click() #выбираем чекбокс

    radio = browser.find_element(By.ID, radio1)
    radio.click()

    button = browser.find_element(By.CSS_SELECTOR, submit)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()