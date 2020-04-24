from selenium import webdriver as wd
import csv

def main():
                                        #CHANGE TO YOUR DRIVER PATH -- GECKO DRIVER IS MOZILLA
    driver = wd.Firefox(executable_path=r'C:\Users\Sammy\Desktop\CovidDataScraper\WebScraper\geckodriver.exe')
    driver.set_page_load_timeout(30)
    driver.get('https://www.dph.illinois.gov/covid19/covid19-statistics')
    
    #all_element = driver.findElement(By.linkText("All").click()
    all_element = driver.find_element_by_xpath('//html//body//div[1]//div[4]//div//article//div//div//div//ul[3]//li[43]//a').click()

    table_element = driver.find_element_by_id('detailedData')
    table_text=table_element.text
    print(table_text)
    
    #write to csv (may take some time)
    with open('data.csv','w',newline='') as csvfile:

        wr = csv.writer(csvfile)
        #find table
        for row in table_element.find_elements_by_css_selector('tr'):
            #find rows
            wr.writerow([data.text for data in row.find_elements_by_css_selector('td')])
    
if __name__ == "__main__":
    main()
