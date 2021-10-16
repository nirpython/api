from flask import Flask, request, jsonify, render_template
from bs4 import BeautifulSoup
from proxycrawl import CrawlingAPI,ScraperAPI

app = Flask(__name__,template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    NAME = request.form['name']
    EMAIL= request.form['email']
    WMOBILE = request.form['wmob']
    org = request.form['Org']
    DESIGNATION = request.form['Desi']
    WCITY = request.form['Wcity']

    my_dict=[]

    RE = (NAME).replace(" ", "+") + "+" + (org).replace(" ", "+") + "+" + EMAIL + "+" + WMOBILE + "+" + (
        DESIGNATION).replace(" ", "+") + "+" + WCITY
    print(RE)
    url = "https://www.google.com/search?q=" + RE
    url1 ="https://www.bing.com/search?q=" + RE
    url2="https://in.search.yahoo.com/search;_ylt=AwrxwXqLZGphOGsACwS7HAx.;_ylc=X1MDMjExNDcyMzAwMwRfcgMyBGZyA3NmcARmcjIDc2ItdG9wBGdwcmlkAzNyMTBxWUQ5U19DejJ3VkE0ZjJ3OUEEbl9yc2x0AzAEbl9zdWdnAzEwBG9yaWdpbgNpbi5zZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDMARxc3RybAMxBHF1ZXJ5Ay4EdF9zdG1wAzE2MzQzNjI1ODc-?p="+RE
    scraper_api = ScraperAPI({'token': 'UrxFELzNzFo3xf7qJQa8yA'})
    response = scraper_api.get(url)
    res = response['json']['searchResults']
    data2 = res[0]

    my_dict.append(data2)
    scraper_api = ScraperAPI({'token': 'UrxFELzNzFo3xf7qJQa8yA'})
    response = scraper_api.get(url1)
    res = response['json']['searchResults']
    data1 = res[0]
    my_dict.append(data1)

    scraper_api = ScraperAPI({'token': 'UrxFELzNzFo3xf7qJQa8yA'})
    response = scraper_api.get(url2)
    res = response['json']['content']
    data3 = res
    my_dict.append(data3)



    return render_template("after.html",data2=my_dict)




if __name__ == '__main__':
    app.run(port=8342,debug=True)