import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new instance of the webdriver class:
driver = webdriver.Chrome()

# Navigate to the Indeed job search page:
driver.get("https://www.indeed.com/jobs")

# Enter your search criteria and click the "Search" button
search_bar = driver.find_element(By.CSS_SELECTOR, "input[name='q']")
search_bar.send_keys("back end developer")

location_bar = driver.find_element(By.CSS_SELECTOR, "input[name='l']")
location_bar.clear()
location_bar.send_keys("")

search_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
search_button.click()

# Wait for the search results to load
time.sleep(5)

# Iterate through the job listings and apply to each one that matches your criteria:
job_listings = driver.find_elements(By.CLASS_NAME, "jobsearch-SerpJobCard")

for job_listing in job_listings:
    job_title = job_listing.find_element_by_class_name("title").text
    company_name = job_listing.find_element_by_class_name("company").text

    # Check if the job title and company name match your criteria
    if "junior back end developer" in job_title.lower() and "Cerritos, CA" in company_name:
        # Switch to the frame that contains the "Apply" button
        driver.switch_to.frame("jobsearch_IndeedApplyButton")

        # Find the "Apply" button and click on it
        apply_button = driver.find_element_by_class_name("jobsearch-IndeedApplyButton")
        apply_button.click()

        # Switch back to the main frame
        driver.switch_to.default_content()

        # You can add code here to fill out the job application form and submit it
        # ...

        # Go back to the job search page
        driver.back()

# Close the web browser:
driver.quit()
