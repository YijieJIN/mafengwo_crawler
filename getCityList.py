from bs4 import BeautifulSoup 
from selenium import webdriver
import requests
import time
import csv

def requestUrl(url):
    '''
    Get the HTML file in the page.\n
    :param url: the URL of current page.\n
    :return: bsObj: a soup object
    '''
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"
    headers = {
        "User-Agent": user_agent
    }
    r = requests.get(url, headers=headers)
    r.encoding = "utf-8"
    html = r.text
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj

def openUrl(url):
    '''
    Open an URL with webdriver\n
    :param: url\n
    :return: driver
    '''
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(url)
    return driver

def get_region_urls(url):
    '''
    Get URLs of all regions\n
    :param url: the URL of current page.\n
    :return region_url: a list storing URLs of all regions.
    ''' 
    bsObj = requestUrl(url)
    regions_tag = bsObj.find("div", {"class": "hot-list clearfix"}).find_all("dt")
    
    region_names = []
    region_urls = []
    for region in regions_tag:
        link = region.find_all("a")
        if len(link) == 0:
            pass
        else:
            try:
                for i in range(len(link)):
                    url = link[i]["href"]
                    name = link[i].string
                    full_url = "http://www.mafengwo.cn"+str(url)
                    region_names.append(name)
                    region_urls.append(full_url)
                    
            except:
                pass
    return region_names, region_urls

def get_cities_url(region_urls):
    '''
    Get the URLs and names of cities in different provinces.\n
    :param region_urls: the list of URLs of all provinces.\n
    :return: city_name_list, city_url_list: the names and urls of all cities in all provinces.
    The two lists are all two-dimensional.
    '''
    for i in range(len(region_urls)):
        url = region_urls[i].replace('travel-scenic-spot/mafengwo', 'mdd/citylist')
        driver = openUrl(url)
        while True:
            try:
                time.sleep(2)
                bsObj = BeautifulSoup(driver.page_source, "html.parser")

                city_name = get_city_name(bsObj)
                city_url = get_city_url(bsObj)
                city_visitor_num = get_city_visitor_num(bsObj)

                appendIntoFile([city_name, city_url, city_visitor_num], "total.csv")
                print(city_name)
                print(city_url)
                print(city_visitor_num)
                driver.find_element_by_class_name('pg-next').click()
            except:
                break
        driver.close()

def append_cities_url(filename):
    '''
    Append municipalities to total.csv
    :param filename: total.csv
    '''
    row1 = ["北京", "http://www.mafengwo.cn/travel-scenic-spot/mafengwo/10065.html", "65406"]
    row2 = ["天津", "http://www.mafengwo.cn/travel-scenic-spot/mafengwo/10320.html", "32817"]
    row3 = ["重庆", "http://www.mafengwo.cn/travel-scenic-spot/mafengwo/10208.html", "30918"]
    row4 = ["上海", "http://www.mafengwo.cn/travel-scenic-spot/mafengwo/10099.html", "63611"]
    with open(filename, "a", newline="") as csvFile:
        csvWriter = csv.writer(csvFile, delimiter=",")
        csvWriter.writerow(row1)
        csvWriter.writerow(row2)
        csvWriter.writerow(row3)
        csvWriter.writerow(row4)

def get_city_name(bsObj):
    '''
    Get name for a single city.
    '''
    name_tags = bsObj.find_all("a", {"data-type": "目的地"})
    city_name = [name_tags[i].find("div", {"class": "title"}).text.replace('\n','').split()[0] for i in range(len(name_tags))]
    return city_name

def get_city_url(bsObj):
    '''
    Get URL of a single city.
    '''
    url_tags = bsObj.find_all("div", {"class": "img"})
    city_url_tag = [url_tags[i].find("a") for i in range(len(url_tags))]
    city_url = []
    for i in range(len(city_url_tag)):
        url_temp = city_url_tag[i]["href"]
        full_url = "http://www.mafengwo.cn"+url_temp
        city_url.append(full_url)
    return city_url

def get_city_visitor_num(bsObj):
    '''
    Get the number of visitors who have visited the city.
    :param bsObj
    :return number: the number of visitors
    '''
    number = bsObj.find_all("div", {"class": "nums"})
    number = [number[i].text.replace('\n','').split()[0] for i in range(len(number))]
    number = [number[i].replace('人去过','') for i in range(len(number))]
    return number

def appendIntoFile(info, filename):
    with open(filename, "a", newline="") as csvFile:
        csvWriter = csv.writer(csvFile, delimiter=",")
        for j in range(len(info[0])):
            row_temp = [info[i][j] for i in range(len(info))]
            csvWriter.writerow(row_temp)

def main():
    url = "http://www.mafengwo.cn/mdd/"
    region_names, region_urls = get_region_urls(url)
    get_cities_url(region_urls)

if __name__ == "__main__":
    main()