import scrapy


class AnimesnetSpider(scrapy.Spider):
    name = 'animesnet'
    start_urls = ['https://myanimelist.net/topanime.php?limit=0']

    def parse(self, response):
        for anime in response.css('td.title.al.va-t.word-break'):
            yield{
                'Titulo' : anime.css('div.di-ib.clearfix > h3 ::text').get(),
                'Nota': response.css('td.score.ac.fs14 > div > span::text').get(),
                'Eps': anime.css('.information.di-ib.mt4::text')[0].get(),
                'Ano': anime.css('.information.di-ib.mt4::text')[1].get(),
                'Membros': anime.css('.information.di-ib.mt4::text')[2].get(),
                'Assista': anime.xpath('//a[@class="hoverinfo_trigger fl-l ml12 mr8"]/href').get(),
                'Image': anime.xpath('//a[@class="hoverinfo_trigger fl-l ml12 mr8"]/img/@data-src').get()
            }