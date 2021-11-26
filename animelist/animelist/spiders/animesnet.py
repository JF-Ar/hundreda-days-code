import scrapy


class AnimesnetSpider(scrapy.Spider):
    name = 'animesnet'
    start_urls = ['https://myanimelist.net/topanime.php?limit=0']

    def parse(self, response):
        for animes in response.css('td.title.al.va-t.word-break > div'):
            yield{
                'anime': animes.css('div.di-ib.clearfix > h3 ::text').get(),
                'nota': response.css('td.score.ac.fs14 > div > span::text').get(),
                'eps': animes.css('.information.di-ib.mt4::text')[0].get(),
                'ano': animes.css('.information.di-ib.mt4::text')[1].get(),
                'membros': animes.css('.information.di-ib.mt4::text')[2].get()
            }
