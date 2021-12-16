from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

btn_troll = '.trollface.btn.btn-primary' #class
num_value = 'input_value' # id
area = 'answer' # id
btn_sub = '.btn.btn-primary' # class
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))



try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    btn_troll = browser.find_element(By.CSS_SELECTOR, btn_troll)
    btn_troll.click()

    #Меняем вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    num_value = browser.find_element(By.ID, num_value)
    num = num_value.text
    x = calc(num)
    print(x)

    area = browser.find_element(By.ID, area)
    area.send_keys(x)

    btn_sub = browser.find_element(By.CSS_SELECTOR, btn_sub)
    btn_sub.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
