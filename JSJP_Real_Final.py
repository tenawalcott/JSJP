from selenium import webdriver


def main():
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--headless")
    chromeOptions.add_argument('--no-sandbox')
    chromeOptions.add_argument('User-Agent="Chrome/88.0.4324.104"')
    drive = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chromeOptions)
    nums = []
    for num in nums:
        num = num[0]
        submit(num, drive)
    drive.close()


def submit(num, drive):
    try:
        drive.get(
            "https://zsfx.bnu.edu.cn/uc/wap/login?redirect=https%3A%2F%2Fzsfx.bnu.edu.cn%2Fsite%2FdailyReport%2FreportAll%3Fappid%3D6")
        input = drive.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/input')
        input.send_keys(num)
        input = drive.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/input')
        input.send_keys(num)
        drive.find_element_by_xpath('//*[@id="app"]/div[3]').click()
        while True:
            try:
                drive.execute_script('window.scrollTo(0, 4000)')
                drive.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/span[1]')
            except:
                continue
            break
        button = drive.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/span[1]")
        drive.execute_script("arguments[0].click();", button)
    except:
        print("False"+num)


if __name__ == "__main__":
    main()
