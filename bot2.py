# Importing necessary modules
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import ast

# WebDriver Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())

# Target URL
driver.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=281001&date=08/05/2021")

# print(driver.title)

# Printing the whole body text
s=(driver.find_element_by_xpath("/html/body").text)
driver.close()
s=s[12:-1]
s=ast.literal_eval(s)
print("Vaccines Available!!")
print("details : ")
for i in s:
    print(i["name"],"(",i["min_age_limit"],"+) : ",i["available_capacity"])
# Closing the driver

