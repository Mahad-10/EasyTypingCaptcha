from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions


# Driver for Firefox
def createFirefoxDriver():
    options = FirefoxOptions()
    # options.add_argument("--headless")
    # driver = webdriver.Firefox(executable_path='geckodriver.exe', options=options)
    driver = webdriver.Firefox(options=options)
    print('driver created')
    return driver


# Driver for Chrome
def createChromeDriver():
    options = ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
    return driver


def openWebsiteLoginPage(driver):
    sleep(1)
    print('opening website')
    driver.get('https://www.easytypingjob.com/login')


def fillCredentials(driver):
    sleep(1)
    print('filling form')
    username = 'Bilal aarbi'
    password = 'masadrb'
    login_button = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/form/button")

    try:
        username_text = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.NAME, "username"))
        )
        password_text = driver.find_element_by_name('password')

        username_text.send_keys(username)
        password_text.send_keys(password)

        login_button.click()
        # try:
        #     print('login')
        #     login_button = WebDriverWait(driver, 10).until(
        #         EC.presence_of_element_located(
        #             (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/form/button"))
        #     )
        #     login_button.click()
        #
        # except Exception as e:
        #     print('Login Button not found', e)

    except Exception as e:
        print('Username Field not found', e)


def earnMoney(driver):
    try:
        earn_money_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[3]/div[2]/div/div[1]/ul[2]/li[3]/a"))
        )
        earn_money_button.click()
        try:
            captcha = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.ID, "CaptchaDiv"))
            )
            captcha_text = captcha.text
            print(captcha_text)

            try:
                captcha_input = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.ID, "CaptchaInput"))
                )
                captcha_input.send_keys(captcha_text)
                try:
                    submit_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located(
                            (By.XPATH, "/html/body/div[3]/div[4]/div/div/div/div[2]/div/div/form/div[2]/input"))
                    )
                    submit_button.click()
                    print('button submitted')

                except Exception as e:
                    print('Earn Money Button not found', e)

            except Exception as e:
                print('Captcha input not found', e)

        except Exception as e:
            print('Captcha not found', e)

    except Exception as e:
        print('Earn Money Button not found', e)


if __name__ == '__main__':
    driver = createFirefoxDriver()
    openWebsiteLoginPage(driver)
    fillCredentials(driver)
    while True:
        earnMoney(driver)
        print('done')
