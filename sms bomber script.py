from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def main():
    #setting the web browser we will be using
    val1 = input("Enter your phone number: ")
    print("Press ctrl+c to quit and stop messaging")
    browser = webdriver.Chrome(executable_path = 'chromedriver.exe')
    browser.get("https://mytoolstown.com/smsbomber/#bestsmsbomber")
    try:
        while browser.current_url != "https://mytoolstown.com/smsbomber/success.php":
            if browser.current_url != "https://mytoolstown.com/smsbomber/#bestsmsbomber":
                browser.get("https://mytoolstown.com/smsbomber/#bestsmsbomber")
            browser.implicitly_wait(100)
            WebDriverWait(browser,200)
            number = browser.find_element_by_id("mobno")
            number.send_keys(val1)
            count = browser.find_element_by_id("count")
            count.send_keys("10")
            speed = browser.find_element_by_xpath("/html/body/div[3]/b/div[2]/div[2]/div/div[2]/form/div[3]/div/div/div[3]/label").click()
            send = browser.find_element_by_xpath("/html/body/div[3]/b/div[2]/div[2]/div/div[2]/form/div[3]/center/input[2]").click()
            try:
                WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/center/div/div[1]/div[2]/img")))
            finally:
                browser.get("https://mytoolstown.com/smsbomber/#bestsmsbomber")
    except KeyboardInterrupt:
        browser.close()
        browser.quit()
        pass

#calling main function
if __name__ == '__main__':
    main()


