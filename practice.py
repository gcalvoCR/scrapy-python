start_urls = [
    'https://www.zyte.com/blog/page/4/',
    'https://www.zyte.com/blog/page/2/',
    'https://www.zyte.com/blog/page/3/'
]

for item in start_urls:
    t = item.split('/')[-2]
    print(f'page {t}')
    print(len(item.split('/')))
   