from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import Select 

from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import *

from selenium.webdriver.common.action_chains import ActionChains


URL = "http://reciprocal.wbhealth.gov.in/Login.aspx"
I=10

Id = '9007156131'
Password = 'Moumita@22'
driver = webdriver.Chrome()
#driver.implicitly_wait(10)
driver.maximize_window()
driver.get(URL)

Num = driver.find_element(By.ID,'txtUser')
Pass = driver.find_element(By.ID,'txtPassword')

#GUI WORK
def send_captcha():
    global CAP
    CAP = captcha_entry.get()
    window.destroy()
window = Tk()
window.title("Captcha Input Window")
window.configure(bg="#A6E3E9")

ScreenWidth = window.winfo_screenwidth()
ScreenHeight = window.winfo_screenheight()

WinWidth= int(ScreenWidth/2)
WinHeight= int(ScreenHeight/3)

#find the center position
CenterX = int((ScreenWidth - WinWidth)/2)
CenterY = int((ScreenHeight - WinHeight)/5)
window.geometry(f"{WinWidth}x{WinHeight}+{CenterX}+{CenterY}")
label=Label(window,text="Enter the captcha you can see on the browser")
label.place(x=10,y=30)
captcha_entry=Entry(window,width=100)
captcha_entry.place(x=10,y=50)
captcha_entry.focus_set()
b1=Button(window,text="Submit Captcha",command = send_captcha ,width = 20,bg='green')
b1.place(x=10,y=100)

window.mainloop()




Num.send_keys(Id)
Pass.send_keys(Password)

'''cap = int(input("enter the captcha here"))#To take the captcha input'''
driver.find_element(By.ID,'txtcaptcha').send_keys(CAP)#inserting the captcha 
#time.sleep(3)
driver.find_element(By.ID,'btnLogin').click()
driver.find_element(By.LINK_TEXT,"Home").click()
driver.find_element(By.LINK_TEXT,"Schedule Date").click()

#select value from list....

#Find id of option
'''x = driver.find_element(By.ID,'')
drop = Select(x)

#Select by Index
drop.select_by_index(2)'''
xx = [
      "//select/option[text()='01-Feb-2024']",
      "//select/option[text()='05-Feb-2024']",
      "//select/option[text()='06-Feb-2024']",
      "//select/option[text()='07-Feb-2024']",
      "//select/option[text()='08-Feb-2024']",
      "//select/option[text()='12-Feb-2024']",
      "//select/option[text()='13-Feb-2024']",
      "//select/option[text()='15-Feb-2024']",
      "//select/option[text()='19-Feb-2024']",
      "//select/option[text()='20-Feb-2024']",
      "//select/option[text()='21-Feb-2024']",
      "//select/option[text()='22-Feb-2024']",
      "//select/option[text()='26-Feb-2024']",
      "//select/option[text()='27-Feb-2024']",
      "//select/option[text()='28-Feb-2024']",
      "//select/option[text()='05-Mar-2024']",
      "//select/option[text()='06-Mar-2024']",
      "//select/option[text()='07-Mar-2024']",
      "//select/option[text()='12-Mar-2024']",
      
      ]
      
#select value from dropdown
for i in xx:
    time.sleep(1)
    try :       
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_ddlDate")))
        driver.find_element(By.XPATH,i).click()
        
        '''target_element = driver.find_element_by_id("ctl00_ContentPlaceHolder1_lblAlreadySched")

        sss = ActionChains(driver).double_click(target_element).perform()'''

        ScanSlot = int(driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_lblAlreadySched").text)
        #selected_value = ScanSlot.click()
        print(ScanSlot)
        if(ScanSlot == 120):
            driver.find_element(By.ID,'ctl00_ContentPlaceHolder1_btnSave').click()
            print("Available Slot")
            
            break
        #print("Scanslot + 9 is equals to ",ScanSlot+9)
        
        #print(ScanSlot.get_attribute('value'))
        print("Working Normally")
    except(error) :
        print("EXCEPT block working \n Some Error Occured when Searching for Schedule Date \n",error)
        break
        #driver.send_keys(Keys.ALT)
        #driver.execute_script("window.history.go(-1)")
    '''timeout = 5
    try:
        element_present = EC.presence_of_element_located((By.ID, 'ctl00_liveStage'))
        WebDriverWait(driver, timeout).until(element_present)
        driver.find_element(By.XPATH,i).click()
        time.sleep(1)
    except TimeoutException:
        print("Timed out waiting for page to load")
        '''
    
    #if((driver.execute_script("return document.readyState")) == 'complete'):
        #driver.find_element(By.XPATH,i).click()
    #print(driver.execute_script("return document.readyState"))

    #WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

    #time.sleep(1)


'''driver.find_element(By.XPATH,"//select/option[text()='15-Jan-2024']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//select/option[text()='17-Jan-2024']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//select/option[text()='18-Jan-2024']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//select/option[text()='22-Jan-2024']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//select/option[text()='24-Jan-2024']").click()
driver.find_element(By.XPATH,"//select/option[text()='29-Jan-2024']").click()
driver.find_element(By.XPATH,"//select/option[text()='25-Jan-2024']").click()
driver.find_element(By.XPATH,"//select/option[text()='25-Jan-2024']").click()
driver.find_element(By.XPATH,"//select/option[text()='25-Jan-2024']").click()
driver.find_element(By.XPATH,"//select/option[text()='25-Jan-2024']").click()
driver.find_element(By.XPATH,"//select/option[text()='25-Jan-2024']").click()
driver.find_element(By.XPATH,"//select/option[text()='25-Jan-2024']").click()
driver.find_element(By.XPATH,"//select/option[text()='25-Jan-2024']").click()
driver.find_element(By.XPATH,"//select/option[text()='25-Jan-2024']").click()
driver.find_element(By.XPATH,"//select/option[text()='25-Jan-2024']").click()
driver.find_element(By.XPATH,"//select/option[text()='25-Jan-2024']").click()
driver.find_element(By.XPATH,"//select/option[text()='25-Jan-2024']").click()
'''
#driver.send_keys(Keys.ALT + Keys.ARROW_LEFT)
#driver.back()
time.sleep(3)

driver.quit()
