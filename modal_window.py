from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

btnMain = '.btn.btn-primary' #кнопка на первой страницы, клик для перехода
num_value = 'input_value'  #число для ввода, id
area = 'answer' # поле ввода, id
btnLast = 'button.btn-primary'
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)


    btnMain =  browser.find_element(By.CSS_SELECTOR, btnMain)
    btnMain.click()

    alert = browser.switch_to.alert
    alert.accept()

    num_value = browser.find_element(By.ID, num_value)
    numx = num_value.text
    x = calc(numx)

    area = browser.find_element(By.ID, area)
    area.send_keys(x)

    btnLast = browser.find_element(By.CSS_SELECTOR, btnLast)
    btnLast.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()



