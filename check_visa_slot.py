from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Set up Selenium WebDriver (assuming Chrome)
driver = webdriver.Chrome()
driver.get("<the visa slot website link>")

# Find the correct element containing the number of visa slots
visa_slots_element = driver.find_element_by_xpath("//div[@class='cards']//div[contains(text(),'Visa Slots Available')]/following-sibling::div")

# Get the number of visa slots
visa_slots = int(visa_slots_element.text)

# Check if visa slots are not 0
if visa_slots != 0:
    # Email Configuration
    sender_email = "<your email>"
    receiver_email = "<reciaver email>"
    password = "<your password>"
    
    # Create message container
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = "Visa Slots Available Alert!"
    
    # Email body
    body = f"Visa slots are available! There are currently {visa_slots} slots available on www.visaslots.info."
    message.attach(MIMEText(body, 'plain'))
    
    # Connect to Gmail SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    
    # Login to Gmail
    server.login(sender_email, password)
    
    # Send email
    server.sendmail(sender_email, receiver_email, message.as_string())
    
    # Close SMTP connection
    server.quit()

# Close the Selenium WebDriver
driver.quit()
