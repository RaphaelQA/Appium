import base64
import os
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

from tests.seecrets import my_App2, E_mail, Password, my_path

value = '//android.widget.ImageView[@content-desc="Account"]'
desired_cap = {
    'deviceName': 'emulator-5554',
    'platformName': 'Android',
    'app': my_App2
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)

driver.start_recording_screen()
"""Авторизация"""
# Выбор языка
select_language = driver.find_element(by=AppiumBy.XPATH, value='//*[@bounds="[66,857][529,1325]"]')
select_language.click()

# Кнопка продолжить
Continue_button = driver.find_element(by=AppiumBy.XPATH, value='//*[@bounds="[66,1874][1014,2017]"]')
Continue_button.click()

# Баннеры
banner_1 = driver.find_element(by=AppiumBy.XPATH, value='//*[@bounds="[66,1874][1014,2017]"]').click()
banner_2 = driver.find_element(by=AppiumBy.XPATH, value='//*[@bounds="[66,1874][1014,2017]"]').click()
banner_3 = driver.find_element(by=AppiumBy.XPATH, value='//*[@bounds="[66,1874][1014,2017]"]').click()

# Авторизация
Have_account = driver.find_element(by=AppiumBy.XPATH,
                                   value='//android.view.View[@content-desc="У меня уже есть аккаунт"]')
Have_account.click()

Email = driver.find_element(by=AppiumBy.XPATH, value="//*[@bounds='[66,454][1014,586]']")
Email.click()
Email.send_keys(E_mail)
# Пароль, ищем по тексту, так как Класс-нейм одинаковый
password = driver.find_element(by=AppiumBy.XPATH, value="//*[@bounds='[66,756][1014,888]']")
password.click()
driver.wait_activity('password.click()', 1)
password.send_keys(Password)
# Кнопка, посмотреть пароль
see = driver.find_element(by=AppiumBy.XPATH, value="//*[@bounds='[882,756][1014,888]']")
see.click()
driver.wait_activity('see.click()', 2)  # Ожидание поставил, чтобы посмотреть как оно работает
# Кнопка Логин
login = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Войти"]')
login.click()
# Permission
per = driver.find_element(by=AppiumBy.ID, value='com.android.permissioncontroller:id/permission_allow_button')
if per:
    per.click()
driver.wait_activity('per.click()', 1)
# Thanks button
Thanks_button = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Спасибо"]').click()

# Аутбридинг
but_1 = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Дальше"]').click()
but_2 = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Дальше"]').click()
but_3 = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Дальше"]').click()
but_4 = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Дальше"]').click()
but_5 = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Дальше"]').click()
but_6 = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Дальше"]').click()
driver.wait_activity('but_6', 1)


touch = TouchAction(driver)

for i in range(4):
    touch.long_press(x=798, y=1117).move_to(x=751, y=200).release().perform()
    time.sleep(1)

video_raw = driver.stop_recording_screen()
video_name = driver.current_activity + time.strftime("%Y_%m_%d_%H%M%S")

filepath = os.path.join(my_path, video_name+".mp4")

with open(filepath, "wb") as f:
    f.write(base64.b64decode(video_raw))

