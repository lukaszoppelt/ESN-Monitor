import requests
from bs4 import BeautifulSoup
import datetime
from termcolor import colored
import json
import time
from random import randrange
from disc import sendhook
from sendmail import send_mail


url = 'https://www.esn.com/products/esn-isoclear-whey-isolate'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50'

}

loop = True
c = 1
DEBUG = False
print(colored("-----------------------------------\n      ESN MONITOR by Skeletor \n-----------------------------------", 'cyan', attrs=['bold']))

def check(): 
    global loop
    global random
    while loop:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find('textarea', {'id': 'VariantsJson-4776838660193'}).get_text()
        data_json = json.loads(data)
    
        for item in data_json:
                    item = {
                        'name':item["name"],
                        'available':item["available"],
                        'url': response.url,
                        'featured_image': item["featured_image"]
                    }
                    if item["available"] or DEBUG:
                        loop = False
                        print(item["name"] + " IS BACK IN STOCK")
                        img = item["featured_image"]["src"]                  
                        sendhook(item["name"], response.url, img)
                        time.sleep(0.5)
                        #send_mail(item["name"], response.url)
                    else:           
                        loop = True
        now = datetime.datetime.now()     
        CurrentTime = now.strftime("%m-%d %H:%M:%S")   
        print(f"{CurrentTime} No Stock - trying again...")  
        time.sleep(randrange(60,120))
            
        

def main():   
    check()
    
   
    
if __name__ == '__main__':
    main()



                
                
    
    


            

