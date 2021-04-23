from selenium import webdriver
import csv

if __name__ == '__main__':
    url = 'https://kgieworld.moneydj.com/z/zg/zgb/zgb0.djhtm'
    brokers = []
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        # executable_path 輸入 web driver 執行檔的位置
        driver = webdriver.Chrome(chrome_options=options, executable_path='chromedriver')
        driver.set_page_load_timeout(60)
        driver.get(url)
        
        for i in range(0, 5):
            element = driver.find_element_by_name('sel_Broker')
            options = element.find_elements_by_tag_name('option')
            file_name = options[i].text
            print(file_name)
            options[i].click()

            with open(file_name + '.csv', 'w', encoding='utf-8') as f:
                buys = driver.find_elements_by_tag_name('tbody')[3]
                sells = driver.find_elements_by_tag_name('tbody')[4]
                f.write(buys.text.replace(',', '').replace(' ', ','))
                f.write('\n')
                f.write(sells.text.replace(',', '').replace(' ', ','))
    finally:
        driver.quit()  # 關閉瀏覽器, 結束 webdriver process