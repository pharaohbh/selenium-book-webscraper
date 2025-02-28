from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# Set up WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the website
url = "http://books.toscrape.com/"
driver.get(url)

# Pause to allow page to load
time.sleep(3)

# Extract product titles and prices
books = driver.find_elements(By.CLASS_NAME, "product_pod")
book_data = []

for book in books:
    title = book.find_element(By.TAG_NAME, "h3").text
    price = book.find_element(By.CLASS_NAME, "price_color").text
    book_data.append([title, price])

# Save data to a CSV file
df = pd.DataFrame(book_data, columns=["Title", "Price"])
df.to_csv("books_prices.csv", index=False)

print("Data saved successfully!")

# Close the browser
driver.quit()
