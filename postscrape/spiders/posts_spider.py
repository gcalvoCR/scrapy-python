import scrapy

class PostsSpider(scrapy.Spider):
    # This name is important because it is called in the command
    name = 'post'

    # first link to scrape
    start_urls = [
        'https://www.zyte.com/blog/page/1/',
    ]

    # We could use this url as well to practice
    # start_urls = [
    #     'https://books.toscrape.com/catalogue/page-1.html'
    # ]


    # The parse method is the only method required
    # It handles the response of the request
    def parse(self, response):
        # We grab the element using the css method.
        for post in response.css('div.oxy-post'):
            yield {
                'title': post.css('.oxy-post-title::text')[0].get(),
                'author': post.css('.oxy-post-meta-author::text')[0].get(),
            }
        # We grab the next page to scrape
        next_page = response.css('a.next.page-numbers::attr(href)').get()
        
        # We make sure there's another page
        if(next_page is not None):
            # to add pages to scrape we join them
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

        # We could store the whole html with a block of code similar to the following one
        # page = response.url.split('/')[-2]
        # if page == 'blog':
        #     page ='1'
        # filename = 'post-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
