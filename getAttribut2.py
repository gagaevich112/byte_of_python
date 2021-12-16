
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

box = 'treasure'
input1 = 'answer' # id, поле для ввода
chekbox1 = 'robotCheckbox' #id, выбор чек бокса
radio1 = 'robotsRule' #id, выбор кнопки
submit = '.btn.btn-default' #css selector кнопка
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, box)
    box_cheked = x_element.get_attribute("valuex")
    #print("value of x_element: ", box_cheked)
    x = calc(box_cheked)

    field = browser.find_element(By.ID, input1)
    field.send_keys(x)

    chekbox_robot = browser.find_element(By.ID, chekbox1)
    chekbox_robot.click()

    robots_radio = browser.find_element(By.ID, radio1)
    robots_radio.click()

    button = browser.find_element(By.CSS_SELECTOR, submit)
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
