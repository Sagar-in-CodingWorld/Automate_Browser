from selenium import webdriver;
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
import customtkinter as ctk

from selenium.webdriver.common.action_chains import ActionChains

import pygame
pygame.init()
sound=pygame.mixer.Sound('eagle.mp3')
errorSound=pygame.mixer.Sound('error.mp3')

URL = "http://reciprocal.wbhealth.gov.in/Login.aspx"
SCHEDULE_URL = "http://reciprocal.wbhealth.gov.in/ScheduleDateForUser.aspx"
I=10



driver = webdriver.Chrome()
#driver.implicitly_wait(10)
driver.maximize_window()
driver.get(URL)

Num = driver.find_element(By.ID,'txtUser')
Pass = driver.find_element(By.ID,'txtPassword')

#GUI WORK
def send_user_data():
    global CAP
    global user
    global password
    user = ID.get()
    password = PASSWORD.get()
    CAP = captcha_entry.get()
    
    print(user,password,CAP)
    window.destroy()



window = ctk.CTk()
window.title("User Input Window")
window.configure(bg="#A6E3E9")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

ScreenWidth = window.winfo_screenwidth()
ScreenHeight = window.winfo_screenheight()

WinWidth= int(ScreenWidth/2)
WinHeight= int(ScreenHeight/2)

#find the center position
CenterX = int((ScreenWidth - WinWidth)/2)
CenterY = int((ScreenHeight - WinHeight)/5)
window.geometry(f"{WinWidth}x{WinHeight}+{CenterX}+{CenterY-70}")

label1=ctk.CTkLabel(master=window,text="ENTER THE USER_ID")
label1.place(x=100,y=30)
ID=ctk.CTkEntry(master=window,width=200)
ID.place(x=100,y=55)
#ID.focus_set()

label2=ctk.CTkLabel(master=window,text="ENTER THE PASSWORD")
label2.place(x=100,y=100)
PASSWORD=ctk.CTkEntry(master=window,width=200)
PASSWORD.place(x=100,y=125)
#PASSWORD.focus_set()

label3=ctk.CTkLabel(master=window,text="ENTER THE CAPTCHA HERE")
label3.place(x=100,y=190)
captcha_entry=ctk.CTkEntry(master=window,width=100)
captcha_entry.place(x=100,y=215)
#captcha_entry.focus_set()

b1=ctk.CTkButton(master=window,text="Submit Captcha",command = send_user_data,width = 500,height=100)
b1.place(x=100,y=270)

window.mainloop()

Num.send_keys(user)
Pass.send_keys(password)

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
      
      "//select/option[text()='05-Mar-2024']",
      "//select/option[text()='06-Mar-2024']",
      "//select/option[text()='07-Mar-2024']",
      "//select/option[text()='12-Mar-2024']",
      "//select/option[text()='13-Mar-2024']",
      "//select/option[text()='14-Mar-2024']",
      "//select/option[text()='19-Mar-2024']",
      "//select/option[text()='20-Mar-2024']",
      "//select/option[text()='21-Mar-2024']",
      "//select/option[text()='27-Mar-2024']",
      "//select/option[text()='28-Mar-2024']"
      
     ]
#measure the length of the date list
date_len = len(xx)
#select value from dropdown
i=0
loop_condition = True
while ( loop_condition ):

    if(i == date_len):
        #print('PEAK')
        for i in range (1,date_len+1):
            # <<<<<<<<<<<<<  main contain  >>>>>>>>>>>
            print("BACKWARD LOOP ",end='')
            time.sleep(0.4)
            try :
                wait = WebDriverWait(driver, 10)
                element = wait.until(EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_ddlDate")))
                #BACKWARD LOOP
                driver.find_element(By.XPATH,xx[(-1)*i]).click()
                ScanSlot = int(driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_lblAlreadySched").text)
                print('{',xx[(-1)*i],'}',"ScanSlot value is ",ScanSlot)
                #print(ScanSlot)
                if(ScanSlot < 120):
                    

                    #pygame.init()
                    #sound=pygame.mixer.Sound('eagle.mp3')
                    #for j in range(0,5):
                    sound.play()
                    
                    driver.find_element(By.ID,'ctl00_ContentPlaceHolder1_btnSave').click()
                    print(" ###############  Available Slot   ############")
                    loop_condition = False
                    break
                
                #print("Working Normally")
            except:
                print("EXCEPT block working \n Some Error Occured when Searching for Schedule Date \n")
                pygame.mixer.Sound('exception.mp3').play()
                driver.get(SCHEDULE_URL)
                #loop_condition = False
                break
            
        #print("Finished Backward Loop")
        i=0
    # Forward Loop
    print("FORRWARD LOOP ",end='')
    time.sleep(0.4)
    try :
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_ddlDate")))
        #FORWARD LOOP
        driver.find_element(By.XPATH,xx[i]).click()
        #i=i+1
        
        '''target_element = driver.find_element_by_id("ctl00_ContentPlaceHolder1_lblAlreadySched")

        sss = ActionChains(driver).double_click(target_element).perform()'''

        ScanSlot = int(driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_lblAlreadySched").text)
        print('{',xx[i],'}',"ScanSlot value is ",ScanSlot)
        i=i+1
        
        if(ScanSlot < 120):
            

            #pygame.init()
            #sound=pygame.mixer.Sound('eagle.mp3')
            #for j in range(0,5):
            sound.play()
            
            driver.find_element(By.ID,'ctl00_ContentPlaceHolder1_btnSave').click()
            print(" ###############  Available Slot   ############")
            loop_condition = False
            #break
        
        #print("Working Normally")
    except:
        print("EXCEPT block working \n Some Error Occured when Searching for Schedule Date \n")
        pygame.mixer.Sound('exception.mp3').play()
        driver.get(SCHEDULE_URL)
        #loop_condition = False
        
    
    


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
errorSound.play()
time.sleep(120)

driver.quit()
