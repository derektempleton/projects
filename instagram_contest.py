# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 10:37:45 2018

@author: derek
"""

from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
import random, time

  

def get_insta_commentators(url):
    # Launch the browser and go to Instagram post url
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get(url)
   
    # Expand/Load more comments by click button
    button_xpath = '/html/body/span/section/main/div/div/article/div[2]/div[1]/ul/li[2]/button'
    python_button = python_button = driver.find_element_by_xpath(button_xpath)
    print('*' * 50)
    print('DOWNLOADING ALL COMMENTS')
    print('*' * 50)
    for x in range(0,10):
        try:
            python_button.click()
            time.sleep(0.5)
        except:
            print('.')
    
    # Get all comments from post
    comment_names = []
    for a in driver.find_elements_by_xpath('.//a'):
        if len(a.get_attribute('title')) > 0:
            #print(a.get_attribute('title'))
            comment_names.append(a.get_attribute('title'))
    return comment_names

#%%
lib_url = 'https://www.instagram.com/p/Bm_th0UFEov/?taken-by=liberaljewellery'
liberal_commentators = get_insta_commentators(lib_url)

sao_url = 'https://www.instagram.com/p/Bm_ppZ-lV5Y/?taken-by=sao_miguel'
sao_commentators = get_insta_commentators(sao_url)
#%%
print('*' * 50)
print('RESULTS OF THE CONTEST')
print('*' * 50)
comment_names = sao_commentators + liberal_commentators
unique_users = list(set(comment_names))
unique_users.remove('liberaljewellery')
unique_users.remove('sao_miguel')


print('There were ' + str(len(comment_names)) + ' total comments on the post.')
print('Thank you to the ' + str(len(unique_users)) + ' users that entered the contest!')

time.sleep(7)

print('*' * 50)
print('THANK YOU TO ALL OF OUR CONTEST PARTICIPANTS')
print('*' * 50)

time.sleep(7)
for u in unique_users:
    print(u)
    time.sleep(0.1)
print('*' * 50)
print('SHUFFLING THE CONTEST ENTRIES')
print('*' * 50)
for x in range(0,5):
    print('.')
    time.sleep(1)

print('AND THE WINNER IS: ')
time.sleep(2)
print('\n',random.choice(unique_users))
#print('\n ** Contest winner subject to verification of contest rules')
    
    
#%%

