from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the webdriver
driver = webdriver.Chrome()

# Navigate to the URL
driver.get("https://secretstaging.plainvanilla.co/")

# Maximize the window
driver.maximize_window()

# Find and click on the login button
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Log In']")))
login_button.click()

# Enter the username and password
username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user_email")))
username_field.send_keys("doug_test@spglobal.com")

password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user_password")))
password_field.send_keys("Welcome@2023")

# Click the login button
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Log in']")))
login_button.click()

# Verify if we're on the right page
expected_text = "Select Entity"
WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//p[@class='f-32 pb-3']"), expected_text))

# Wait for the Contracts page to load and verify that it contains the text "Contracts"
contracts_page_text = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Select Entity")
)

# Verify the test result
if contracts_page_text:
    print("Test passed!")
else:
    print("Test failed.")

# Close the browser
driver.quit()