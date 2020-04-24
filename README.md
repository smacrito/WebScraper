# WebScraper

### Summary
This program scrapes the covid-19 data from the [Illinois page](http://www.dph.illinois.gov/covid19/covid19-statistics) that displays the case data on a zip per zip basis. It triggers JavaScript elements within the page to trigger a query, then uses the HTML table to create a CSV that can later be used for a visual table or any other sort of data analytics.

### Usages

- Creating tables from CSV data
- Data analytics for Illinois COVID-19 cases
- The function that triggers gets the website, as well as triggers the onClick function can be used on any other website with similar functions, by respectively replacing these variables to fit the particular website's needs.

### Instructions

#### Dependencies

 - selenium
 - csv

**Example**

pip install selenium

**Notes**

 - Be sure to have your WebDriver located in the same path as the
   program.
 - Replace `driver = wd.Firefox(executable_path=r'C:\X\X\X\X\WebScraper\geckodriver.exe')` with the path to your WebDriver.

#### Known Bugs

 - The "all" onClick element on the Illinois page randomly changes xPaths, which are used to identify it due to the lack of CSS or HTML identifiers. 
-- A fix to this may be to find  the element by name, "All", but there are other elements on the page that may conflict with that function.
 

