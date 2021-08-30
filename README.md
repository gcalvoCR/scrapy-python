# scrapy python

This repo explores the functionality of scrapy python.

For this practice I use 2 links:
- `https://www.zyte.com/blog/page/1/`
- `https://books.toscrape.com/catalogue/page-1.html`


## Initial steps
- Set up a virtual environment (instructions for MAC):
  - `python3 -m venv venv` to create the env
  - `source venv/bin/activate` to activate the env

- Install scrapy
 - `pip install scrapy` 

- Start a scrapy project
 - `scrapy startproject postscrape`

- Create a spider by creating a new file, in this case `posts_spider.py`

- To run scrapy
 - `scrapy crawl <name of crawler defined in file>`  

- To open the shell cmd
 - `scrapy shell https://www.zyte.com/blog/page/1/`
- to grab specific elements
 - `response.css('name')`


- Other commands

``` python
response.css('title').get() # to get the actual element
response.css('h3::text').get() # to get the text of the first h3 that if finds.
response.css('h3::text')[1].get() # to get the second element.
response.css('h3::text').getall() # to retrieve all texts of h3s
```


