from selenium import webdriver
import time
from geopy.geocoders import ArcGIS

def webscrape_and_fillcsv():
    firefox_profile = webdriver.FirefoxProfile() 
    firefox_profile.set_preference('intl.accept_languages', 'en')


    browser = webdriver.Firefox(firefox_profile=firefox_profile)


    url = "https://www.google.com/maps/search/iran+waterfalls"


    browser.get(url)


    list = browser.find_elements_by_class_name("section-result-title")
    waterfalls = []
    for a in list:
        waterfalls.append(a.text.lower())
    final_waterfalls = dict.fromkeys(waterfalls)
    with open("waterfalls.txt", 'a') as f:
        f.write("NAME,STATE,HEIGHT,LATITUDE,LONGITUDE\n")
        for waterfall in final_waterfalls:
            url = "https://www.google.com/search?&q={}".format(waterfall.replace(" ", "+"))
            browser.get(url)
            time.sleep(6)

            try:
                address = browser.find_element_by_xpath("//span[@class='LrzXr']")
                list_of_addresses = address.text.split(',')
                geolocator = ArcGIS()
                geolocation = geolocator.geocode(address.text)
                f.write("{},{},{},{},{}\n".format(waterfall, str([s for s in list_of_addresses if "Province" in s]).replace("[", "").replace("]", "").replace("'", ""),100,geolocation.latitude,geolocation.longitude))
            except:
                pass
