from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()
driver.get('https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl')

videos = driver.find_elements(By.ID, 'dismissible')

report = []
for video in videos:
    title = video.find_element(By.ID, 'video-title').text
    meta = video.find_element(By.ID, 'metadata-line').text
    # print(type(meta))
    views = meta.split('\n')[0]
    when = meta.split('\n')[1]

    data = {
        'title': title,
        'views': views,
        'posted on': when
    }
       
    report.append(data)       


d = pd.DataFrame(report)    
print(d)
