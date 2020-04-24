from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import csv

def main():
    
    
    driver = wd.Firefox(executable_path=r'C:\Users\Sammy\Desktop\WebScraper\geckodriver.exe')
    driver.set_page_load_timeout(30)
    driver.get('https://www.dph.illinois.gov/covid19/covid19-statistics')
    #all_element = driver.findElement(By.linkText("All").click()
    all_element = driver.find_element_by_xpath('//html//body//div[1]//div[4]//div//article//div//div//div//ul[3]//li[42]//a').click()
    table_element = driver.find_element_by_id('detailedData')
    table_text=table_element.text
    print(table_text)
    #print(all_element)



    with open('data.csv','w',newline='') as csvfile:
              wr = csv.writer(csvfile)
              #headers
               
              for row in table_element.find_elements_by_css_selector('tr'):
                      wr.writerow([d.text for d in row.find_elements_by_css_selector('td')])

    
if __name__ == "__main__":
    main()
