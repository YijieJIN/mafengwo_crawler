from getCityList import requestUrl, appendIntoFile
from visualize import read, trim
from bs4 import BeautifulSoup
import requests
import time
import csv

def get_city_code(filename):
    '''
    Write the city codes in city_code.csv
    '''
    arr = trim(filename)
    city_code = []
    for element in arr:
        code_temp = element[1].replace("http://www.mafengwo.cn/travel-scenic-spot/mafengwo/", "")
        code_temp = code_temp.replace(".html", "")
        city_code.append([element[0], code_temp])
        with open("city_code.csv", "a", newline="") as csvFile:
            csvWriter = csv.writer(csvFile, delimiter=",")
            csvWriter.writerow([element[0], code_temp])
    
def get_city_food(filename):
    arr = read(filename)
    for i in range(len(arr)):
        name = []
        number = []
        url = "http://www.mafengwo.cn/cy/"+str(arr[i,1])+"/gonglve.html"
        print(url)
        bsObj = requestUrl(url)
        try:
            name_tag = bsObj.find("ol", {"class": "list-rank"}).find_all("h3")
            name = [name_tag[i].text for i in range(len(name_tag))]
        except:
            pass
        try:
            number_tag = bsObj.find("ol", {"class": "list-rank"}).find_all("span",{"class": "trend"})
            number = [number_tag[i].text for i in range(len(number_tag))]
            print(len(number))
            print("--------------------------------------------------------------")
        except:
            pass
        if len(name) == len(number) and len(number) != 0:
            print(name) 
            print(number)
            print(arr[i])
            appendIntoFile([name, number], "city_food.csv") 
        elif len(number) != 0:
            name = name[:len(number)]
            print(name) 
            print(number)
            appendIntoFile([name, number], "city_food.csv")
        print("Finished round {%s}! " % str(i), "city: "+str(arr[i]))

def get_city_spot(filename):
    arr = read(filename)
    for i in range(len(arr)):
        url = "http://www.mafengwo.cn/jd/"+str(arr[i,1])+"/gonglve.html"
        print("The %s-th url is: " % str(i+1)+url)
        bsObj = requestUrl(url)
        tag = bsObj.find_all("div", {"class": "item clearfix"})
        try:
            name = [tag[i].find("a")["title"] for i in range(len(tag))]
            number = [tag[i].find("em").string for i in range(len(tag))]
            appendIntoFile([name, number], "city_spot.csv")
        except:
            print("No name or comment number for %s." % str(arr[i,0]))
            pass
        
def main():
    start_time = time.time()
    get_city_code("total.csv")
    get_city_food("city_code.csv")
    get_city_spot("city_code.csv")
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()