import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 

driver_path = "C:\\Users\\hakan\\OneDrive\\Masaüstü\\selenium\\chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)
action = ActionChains(driver) 

driver.get("https://www.instagram.com")
driver.maximize_window() 
driver.implicitly_wait(20)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(nicknamae)

driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)

driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
time.sleep(10)
driver.get("https://www.instagram.com/taylorswift/followers/")
time.sleep(5)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div/div[2]').click()
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[2]/div/div[2]/button').click()
time.sleep(2)
def followUser():
    followButton = browser.find_element_by_tag_name("button")
    if followButton.text == "Takip Et":
        followButton.click()
        time.sleep(2)
    else:
        print("Zaten takiptesin")    
    
       

          







    

    
        
        

      
        
     


        
    


    
        

    


    







