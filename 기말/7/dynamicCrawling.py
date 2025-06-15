# -*- coding: utf-8 -*-"https://www.coffeebeankorea.com/store/store.asp
#%%
from bs4 import BeautifulSoup
import urllib.request
import datetime
from selenium import webdriver
import pandas as pd
import time


CoffeeBean_url = 'https://www.coffeebeankorea.com/store/store.asp'
wd=webdriver.Chrome()
result=[]
for i in range(1,20):
    wd.get(CoffeeBean_url)
    time.sleep(1)
    
    try:
        wd.execute_script('storePop2(%d)' %i)
        time.sleep(1)
        html = wd.page_source
        soupCB=BeautifulSoup(html, 'html.parser')
        store_name_h2 = soupCB.select('div.store_txt>h2')
        store_name = store_name_h2[0].string
        print(store_name)
        store_info=soupCB.select('div.store_txt > table.store_table > tbody>tr> td ')
        store_address_list = list(store_info[2])
        store_address = store_address_list[0]
        store_phone = store_info[3].string
        result.append([store_name]+[store_address]+[store_phone])    
        
        
    except:
        print('error')
        continue

print("CoffeeBean store crawling")



CB_tbl=pd.DataFrame(result,columns=('store','address','phone'))
CB_tbl.to_csv('CoffeBean.csv', encoding='cp949', mode='w',index=True)
wd.close()


    

#matizCoverLayer0Content > div > div > div.store_txt > table > tbody:nth-child(1) > tr:nth-child(1) > td
