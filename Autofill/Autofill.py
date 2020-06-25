from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support.ui import  Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

MSuname = ""                                   #Microsoft email
MSpwd = ""                                     #Microsoft pwd

sakecmail = ""
register_no = ""

stars = 4                                      #no from 1 to 5
sat = 2                                        #no from 1 to 5 very statisfied to not satisfied

q10 = 1                                        #Yes or no qn 1 for yes 2 for no
q11 = 1

feedback1 = "YES "                             #change if you want for 1st feedback qn
feedback2 = "More topics......"                #add something
rate1 = 7

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get("https://bit.ly/fb_day9")

uname = driver.find_element_by_id('i0116')
uname.send_keys(MSuname)
uname.send_keys(Keys.ENTER)
time.sleep(2)
pw = driver.find_element_by_id('i0118')
time.sleep(1)
pw.send_keys(MSpwd)

time.sleep(5)
pw.send_keys(Keys.ENTER)
time.sleep(1)
sbutton = driver.find_element_by_id('idSIButton9')
sbutton.click()

email = driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div/div/div/input')
email.send_keys(sakecmail)

reg_no = driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[3]/div/div/div/input')
reg_no.send_keys(register_no)

branch = driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[3]/div[2]/div[3]/div/table/tbody/tr/td[2]')
branch.click()

classbox = driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div/div/span')
classbox.click()
cname = driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div/ul/li[3]')
cname.click()

divbox = driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[5]/div[2]/div[3]/div/div/div/span')
divbox.click()
division = driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[5]/div[2]/div[3]/div/div/ul/li[3]')
division.click()

star1 = driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[6]/div[2]/div[3]/div/div/div/div/div[1]/span['+ str(stars) +']')
star1.click()

star2 = driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[7]/div[2]/div[3]/div/div/div/div/div[1]/span['+ str(stars) +']')
star2.click()

star3 = driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[8]/div[2]/div[3]/div/div/div/div/div[1]/span['+ str(stars) +']')
star3.click()

time.sleep(4)
table1 = driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[9]/div[2]/div[3]/div/table/tbody/tr[1]/td['+ str(sat+1) +']/label/input')
table1.click()

table2 = driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[9]/div[2]/div[3]/div/table/tbody/tr[2]/td['+ str(sat+1) +']/label/input')
table2.click()

table3 = driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[9]/div[2]/div[3]/div/table/tbody/tr[3]/td['+ str(sat+1) +']/label/input')
table3.click()

fb1 = driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[10]/div[2]/div[3]/div/div/div')
fb1.click()
fboption1 = driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[10]/div[2]/div[3]/div/div/ul/li['+ str(q10)+']')
fboption1.click()

fb2 = driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[11]/div[2]/div[3]/div/div/div')
fb2.click()
fboption2 = driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[11]/div[2]/div[3]/div/div/ul/li['+str(q11)+']')
fboption2.click()

txt = driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[12]/div[2]/div[3]/div/div/div/textarea')
txt.send_keys(feedback1)

txt2 = driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[13]/div[2]/div[3]/div/div/div/textarea')
txt2.send_keys(feedback2)

rate = driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[14]/div[2]/div[3]/div/div/table/tbody/tr/td['+str(rate1+1)+']/div')
rate.click()

time.sleep(4)