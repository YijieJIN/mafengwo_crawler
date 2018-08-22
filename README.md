## Project: Spider on Mafengwo
* Python scripts:
  * [getCityList.py](https://raw.githubusercontent.com/YijieJIN/mafengwo_crawler/master/getCityList.py)
  * [getCityInfo.py](https://raw.githubusercontent.com/YijieJIN/mafengwo_crawler/master/getCityInfo.py)
  * [visualize.py](https://raw.githubusercontent.com/YijieJIN/mafengwo_crawler/master/visualize.py)
 
* Folders:
  * data: all data fetched from [目的地旅游攻略 - 马蜂窝](http://www.mafengwo.cn/mdd/)
  * figures: all images in `.png` format and in `.html` format (with a little bit interactions)
  
* Contents
  In this project, we crawled information about visitor numbers, foods and most popular spots of cities in China on Mafengwo. 
  In `getCityList.py`, we firstly get the urls of 22 regions. After that, we crawled over the pages of the 22 regions to get visitor numbers and urls of cities in the regions and store them into a csv file (total.csv). 
  In `getCityInfo.py`, we get the infomation about most popular foods and spots in each city with `get_city_food` and `get_city_url` respectively.
  
  
* Figures:
  * Heatmap for visitor numbers.
    ![Heatmap](https://github.com/YijieJIN/mafengwo_crawler/blob/master/figures/Visitors'_numbers_in_cities_of_China.png?raw=true) 
	</br>
  * Most visited 10 cities
    ![Top_10_visited_cities.png](https://github.com/YijieJIN/mafengwo_crawler/blob/master/figures/Top_10_visited_cities.png?raw=true)
	</br>
  * Most liked 10 kinds of foods
    ![Top_10_popular_foods.png](https://raw.githubusercontent.com/YijieJIN/mafengwo_crawler/master/figures/Top_10_popular_foods.png)
	</br>
  * Wordcloud for popular foods
    ![city_food_wordcloud.png](https://github.com/YijieJIN/mafengwo_crawler/blob/master/figures/city_food_wordcloud.png?raw=true)
  * Most popular 10 spots
    ![Top_10_popular_spots.png](<https://github.com/YijieJIN/mafengwo_crawler/blob/master/figures/Top_10_popular_spots.png?raw=true>)
	</br>
  * Wordcloud for popular spots
    ![city_spot_wordcloud.png](https://github.com/YijieJIN/mafengwo_crawler/blob/master/figures/city_spot_wordcloud.png?raw=true)
----------------------------------------------
* Packages:
  * Parse HTML:
    ```python
	from bs4 import BeautifulSoup
	from selenium import webdriver
	import requests
	```
  * Data preprocessing:
    ```python
	import pandas as pd 
	import csv
	```
  * Visualization:
    ```python
	from pyecharts.datasets.coordinates import search_coordinates_by_keyword
	from pyecharts import Geo, Bar, WordCloud
	```
  * Others:
    ```python
	import time
	```
* Functions:
  * getCityList.py
    	`def requestUrl(url):` return `bsObj`
	`def openUrl(url):` use webdriverto open a url </br>
	`def get_region_urls(url):` return `region_names`, `region_urls` </br>
	`def get_cities_url(region_urls):` get urls and visitor numbers of cities into a csv file. </br>
	`def append_cities_url(filename):` append municipalities to total.csv </br>
	`def get_city_name(bsObj):` get name of a single city </br>
	`def get_city_url(bsObj):` get url of a single city </br>
	`def get_city_visitor_num(bsObj):` get visitor number of a single city </br>
	`def appendIntoFile(info, filename):` write rows into csv file </br>
	</br>
  * getCityInfo.py
    	`def get_city_code(filename):` each city has a special code, this function is used to get codes of cities. </br>
	`def get_city_food(filename):` get top10 foods with number of travel notes mentioned them for cities. </br>
	`def get_city_spot(filename):` get top10 spots with number of travel notes mentioned them for cities. </br>
	</br>
  * visualize.py
    	`def read(filename):` read a csv file into an array
	`def checkExistence(row):` check whether the geological coordinates of a city exists in the library.
	`def trim(filename):` trim the cities whose coordinates are not in the library.
	`def trim2(list):` trim the numbers whose numerical values are below 10000.
	`def toHeatmap(filename):` draw a heatmap
	`def sort(filename):` sort the array by its second column.
	`def toBar_cityVisitors(filename):` draw a bar chart about top10 visited  cities.
	`def toBar(filename, title, legend, html_name):` draw a bar chart (about top10 foods and top10 spots)
	`def toWordCloud(filename, html_name):` draw a wordcloud (about top50 foods and top50 spots)
