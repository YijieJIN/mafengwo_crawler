# Project: Spider on Mafengwo
**This project is based on another project on github, I just rewrite the scripts.**
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
