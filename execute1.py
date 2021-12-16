from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


number = 'input_value'
input = 'answer'
chekbox1 = 'robotCheckbox'
radio1 = 'robotsRule' #id, выбор кнопки
button = 'btn-primary'
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    numInput = browser.find_element(By.ID, number)
    numX = numInput.text
    x = calc(numX)

    area_input = browser.find_element(By.ID, input)
    browser.execute_script("return arguments[0].scrollIntoView(true);", area_input)
    area_input.send_keys(x)

    chekbox_robot = browser.find_element(By.ID, chekbox1)
    chekbox_robot.click()

    radio_robot = browser.find_element(By.ID, radio1)
    radio_robot.click()

    submit = browser.find_element(By.CLASS_NAME, button)
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

