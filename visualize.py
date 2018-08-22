from pyecharts.datasets.coordinates import search_coordinates_by_keyword
from pyecharts import Geo, Bar, WordCloud
import pandas as pd
import time

def read(filename):
    '''
    Read the csv file into a NumPy array.\n
    :param: filename\n
    :return: array\n
    '''
    df=pd.read_csv(filename, sep=',',header=None)
    arr = df.values
    return arr

def checkExistence(row):
    '''
    Check whether the geological coordinates of the cities are in the library.\n
    :param row: a row of cities.\n
    :return list1: a list of cities whose coordinates are in the library.\n
    '''
    try:
        result = search_coordinates_by_keyword(row[0])
    except:
        pass
    city_name = ""
    if len(result) >= 1:
        city_name = list(result)[0]
    city_url = row[1]
    city_visitor_num = row[2]
    if city_name == None:
        return None
    else:
        list1 = [city_name, city_url, city_visitor_num]
        return list1

def trim(filename):
    '''
    Trim the cities whose coordinates are not in the library.\n
    :param: filename.\n
    :return: a list of cities with coordinates in the library.
    '''
    arr = read(filename)
    data = []
    for i in range(len(arr)):
        list = checkExistence(arr[i])
        if list[0] != "":
            data.append(list)
    return data
    
def trim2(list):
    '''
    Trim the numbers whose numerical values are below 10000.\n
    :param: list.\n
    :return: a trimmed list.\n
    '''
    trimmed = []
    for i in range(len(list)):
        if list[i][2] >= 10000:
            trimmed.append(list[i])
    return trimmed

def toHeatmap(filename):
    '''
    Draw a heatmap.
    '''
    arr = read(filename)
    data = []
    for i in range(len(arr)):
        t = (checkExistence(arr[i])[0], checkExistence(arr[i])[2])
        if t[0] != "":
            data.append(t)
    geo = Geo(
        "Visitors' numbers in cities of China",
        "most popular cities for travellers",
        title_color="#fff",
        title_pos="center",
        width=1000,
        height=600,
        background_color="#404a59",
    )
    attr, value = geo.cast(data)
    geo.add(
        "",
        attr,
        value,
        type="heatmap",
        is_visualmap=True,
        visual_range=[0, 60000],
        visual_text_color="#fff",
    )
    geo.render("visitors_num.html")
    print("Heatmap Finished!")

def sort(filename):
    '''
    Sort the array by its second column.
    :param: filename
    :return: a sorted array
    '''
    arr = trim(filename) 
    arr = trim2(arr)
    arr_tup = tuple(arr)
    arr_sorted = sorted(arr_tup, key=lambda element: element[2], reverse=True)
    return arr_sorted[:10]

def toBar_cityVisitors(filename):
    '''
    Draw a bar chart of top 10 cities according to visitors' number.
    '''
    list = sort(filename)
    attrs = []
    y = []
    for i in range(len(list)):
        attrs.append(list[i][0].replace("市", ""))
        y.append(list[i][2])
    bar = Bar("Top 10 visited cities")
    bar.add("visitor number", attrs, y, is_stack=True)
    bar.render("top10_visitor.html")
    print("Top 10 visited cities bar chart drawed!")

def toBar(filename, title, legend, html_name):
    '''
    Draw a bar chart.\n
    :param: filename.\n
    :param: title: the title of the bar chart.\n
    :param: legend: the type of the data.\n
    :param: html_name: the name of the HTML file generated.
    '''
    arr = read(filename)
    arr_tup = tuple(arr)
    arr_sorted = sorted(arr_tup, key=lambda element: element[1], reverse=True)[:10]
    attr = [arr_sorted[i][0] for i in range(len(arr_sorted))]
    value = [arr_sorted[i][1] for i in range(len(arr_sorted))]
    bar = Bar(title)
    bar.add(legend, attr, value, is_stack=True)
    bar.render(html_name)
    print("%s bar chart finished!" % title)

def toWordCloud(filename, html_name):
    '''
    Draw a wordcloud.\n
    :param: filename.\n
    :param: html_name: the name of the HTML file generated.
    '''
    arr = read(filename)
    arr_tup = tuple(arr)
    arr_sorted = sorted(arr_tup, key=lambda element: element[1], reverse=True)
    name = [arr_sorted[i][0] for i in range(len(arr_sorted))][:50]
    value = [arr_sorted[i][1] for i in range(len(arr_sorted))][:50]
    wordcloud = WordCloud(width=1300, height=620)
    wordcloud.add("", name, value, word_size_range=[30,100], shape='diamond')
    wordcloud.render(html_name)
    print(html_name.replace(".html", "")+" finished!")


def main():
    start_time = time.time()
    toHeatmap("total.csv")
    toBar_cityVisitors("total.csv")
    toBar("city_food.csv", "Top 10 popular foods", "food name", "top10_food.html")
    toBar("city_spot.csv", "Top 10 popular spots", "spot name", "top10_spot.html")
    toWordCloud("city_spot.csv", "city_spot_wordcloud.html")
    toWordCloud("city_food.csv", "city_food_wordcloud.html")
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()