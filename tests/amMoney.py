from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from tests.seecrets import my_App, E_mail, Password

value = '//android.widget.ImageView[@content-desc="Account"]'
desired_cap = {
    'deviceName': 'emulator-5554',
    'platformName': 'Android',
    'app': my_App
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(10)

"""Баннеры"""
first_banner = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Ok, next"]')
first_banner.click()

second_banner = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Awesome  😇"]')
second_banner.click()

third_banner = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Let’s go 🚀"]')
third_banner.click()

forty_button = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Login"]')
forty_button.click()

"""Авторизация"""
# Почта
Email = driver.find_element(by=AppiumBy.XPATH, value="//*[@text='Enter your email']")
Email.click()
Email.send_keys(E_mail)
# Пароль, ищем по тексту, так как Класс-нейм одинаковый
password = driver.find_element(by=AppiumBy.XPATH, value="//*[@text='Enter your password']")
password.click()
password.send_keys(Password)
# Кнопка, посмотреть пароль
see = driver.find_element(by=AppiumBy.XPATH, value="//*[@bounds='[882,756][1014,888]']")
see.click()
driver.wait_activity('see.click()', 2)  # Ожидание поставил, чтобы посмотреть как оно работает
# Кнопка Логин
login = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Login ✌️"]')
login.click()

"""Главная страница"""
# Приветственная фраза
name = driver.find_element(by=AppiumBy.XPATH, value="//*[@bounds='[882,756][1014,888]']").get_attribute("text")
# driver.wait_activity('name', 2)
print(name)
# assert name == "Привет, раф 🌙", "Текст невалиден"
# meditation = driver.find_element(by=AppiumBy.XPATH,
#                                  value='//android.view.View[@content-desc="Тета-медитация (утро) 10 минут"]')
# driver.wait_activity('meditation', 2)
# print(meditation)
# assert meditation == "Тета-медитация (утро) 10 минут", "Текст невалиден"

# driver.quit()
