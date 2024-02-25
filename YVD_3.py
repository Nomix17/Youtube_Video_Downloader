import re
import os
import time
import pytube
import requests
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Checking if the device is windows or unix like os (cause I will need that to clear the terminal)
if os.name == 'nt':
    clear = 'cls'
else:
    clear = "clear"
os.system(clear)
# Saving the download path if it's the first time working with the script and importing it if it's not
try:
    with open("YVD_download_path.txt",'r') as file:
        download_folder = file.readline()
except:
    download_folder = input('input the path for the download folder: ')
    with open('YVD_download_path.txt','w') as file:
        file.write(download_folder)

os.system(clear)
url = input('URL: ')
os.system(clear)

def getting_source_code(url):
    #scarping the source code of the youtube video from getvideohd.com
    try:
        if '=' not in url:
            Url = f"https://getvideohd.com/v/{url.split('/')[-1]}"
        else:
            Url = "https://getvideohd.com/v/"+url.split('&')[0].split('=')[-1]
    except:
        Url = "https://getvideohd.com/v/"+url.split('=')[-1]
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    drive = webdriver.Chrome(option)
    drive.get(Url)
    time.sleep(2)
    WebDriverWait(drive,10).until(ec.element_to_be_clickable((By.CSS_SELECTOR,"a")))
    source_link_html = drive.find_elements(By.CSS_SELECTOR,"a[class='group relative flex flex-row items-center justify-center bg-blue-500 hover:bg-blue-700 text-white disabled:text-gray-400 font-semibold py-3 px-4 rounded shadow focus:outline-none focus:shadow-outline']")
    # Listing the qualitys of the video so the user can Choose
    if source_link_html:
        for indexs,element in enumerate(source_link_html):
            print(f'{indexs}-{element.text}')
        index= int(input('What resolution you want to download the video with?(the number): '))#you should input the number in the begging of your favorite resolution 
        source_link = source_link_html[index].get_attribute('href')
        return source_link
    else:
        print('Somthing went wong')
        return None

def title_name(url):#getting the name of the video
    originale_tilte = pytube.YouTube(url).title
    file_name = re.sub(r"[^a-zA-Z0-9\-_ ]",' ',originale_tilte)# removing the characters that cannot be in the file name
    return file_name

def downloading_effect():
    while True:
        for i in ['','.','..','...']:
            os.system(clear)
            print(f'downloading{i}')
            time.sleep(1)

def download_from_source(name,source_link):# finaly saving the video in the download folder
    if source_link:
        Thread(target=downloading_effect,daemon=True).start()
        with open(f'{download_folder}/{name}.mp4','wb') as file:
            file.write(requests.get(source_link).content)
    os.system(clear)
    print('Done')

if __name__ == '__main__':
    download_from_source(title_name(url) , getting_source_code(url))