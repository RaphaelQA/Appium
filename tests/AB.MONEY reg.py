from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from random_email_password import random_email, random_password, record_male
from tests.seecrets import my_App2

mail = random_email()
pas = random_password()
record_male(mail)


value = '//android.widget.ImageView[@content-desc="Account"]'
desired_cap = {
    'deviceName': 'emulator-5554',
    'platformName': 'Android',
    'app': my_App2
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
touch = TouchAction(driver)
# Время Ожидания показа элементов на экране, чтобы не упал тест при загрузке приложения, например
driver.implicitly_wait(30)
# Начало записи
# driver.start_recording_screen()
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

# Почта
Email = driver.find_element(by=AppiumBy.XPATH, value='//*[@bounds="[66,459][1014,591]"]')
Email.click()
Email.send_keys(mail)
# Создать пароль
Password = driver.find_element(by=AppiumBy.XPATH, value='//*[@bounds="[66,762][1014,894]"]')
Password.click()
Password.send_keys(pas)
# Повторить пароль
Password_repeat = driver.find_element(by=AppiumBy.XPATH, value='//*[@bounds="[66,938][1014,1070]"]')
Password_repeat.click()
Password_repeat.send_keys(pas)
# Посмотреть пароли
see_pass1 = driver.find_element(by=AppiumBy.XPATH, value='//*[@bounds="[882,762][1014,894]"]').click()
see_pass2 = driver.find_element(by=AppiumBy.XPATH, value='//*[@bounds="[882,938][1014,1070]"]').click()
# Прячем клавиатуру
driver.hide_keyboard()
checkbox = driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[4]').click()
# Создание аккаунта
driver.find_element(by=AppiumBy.XPATH, value='(//android.view.View[@content-desc="Создать аккаунт"])[2]').click()
# Permission
per = driver.find_element(by=AppiumBy.ID, value='com.android.permissioncontroller:id/permission_allow_button')
if per:
    per.click()
driver.wait_activity('per.click()', 1)
# Continue button
Continue_button = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Заполнить профиль ✌🏼"]').click()

touch.long_press(x=617, y=1864).move_to(x=621, y=1213).release().perform()

calendar = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Выберите дату"]').click()

