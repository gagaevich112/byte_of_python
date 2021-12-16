
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

cheked_test = 'robotsRule'

try:
    link = 'http://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)


    robots_radio = browser.find_element(By.ID, cheked_test) #people_radio = browser.find_element(By.ID, cheked_test) #
    people_checked = robots_radio.get_attribute("checked") #Найдём атрибут "checked" с помощью встроенного метода get_attribute и проверим его значение:
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()





finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

