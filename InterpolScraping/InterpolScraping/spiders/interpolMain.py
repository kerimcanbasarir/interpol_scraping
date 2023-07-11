import json
import scrapy
from InterpolScraping.items import InterpolscrapingItem
import random


class InterpolmainSpider(scrapy.Spider):

    name = "interpolMain"
    allowed_domains = ["interpol.int"]
    start_urls = ["https://ws-public.interpol.int/notices/v1/red?page=1"]

    USER_AGENTS = [
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9",
        "Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:40.0) Gecko/20100101 Firefox/40.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/7.1.8 Safari/537.85.17",
        "Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4",
        "Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F69 Safari/600.1.4",
        "Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.5.17 (KHTML, like Gecko) Version/8.0.5 Safari/600.5.17",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:40.0) Gecko/20100101 Firefox/40.0",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
        "Mozilla/5.0 (X11; CrOS x86_64 7077.134.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.156 Safari/537.36"
    ]

    def start_requests(self):
        for url in self.start_urls:
            user_agent = random.choice(self.USER_AGENTS)
            yield scrapy.Request(url, callback=self.parse, headers={'User-Agent': user_agent})


    def parse(self, response, **kwargs):

        # Yanıt verisini JSON formatında yükler
        data = json.loads(response.body)

        # Toplam suçlu sayısını alır
        notices = data["_embedded"]["notices"]

        for notice in notices:
            for link_name, link in notice["_links"].items():

                if link_name == "self":
                    detail_links = link["href"]
                    user_agent = random.choice(self.USER_AGENTS)
                    yield scrapy.Request(detail_links, callback=self.parse_details, headers={'User-Agent': user_agent})

                elif link_name == "images":
                    photo_links = link["href"]
                    user_agent = random.choice(self.USER_AGENTS)
                    yield scrapy.Request(photo_links, callback=self.parse_photo, headers={'User-Agent': user_agent})

        yield from self.get_next_page(data)

    def get_next_page(self, data):
        next_page_link = data["_links"].get("next", {}).get("href")
        if next_page_link:
            user_agent = random.choice(self.USER_AGENTS)
            yield scrapy.Request(next_page_link, callback=self.parse, headers={'User-Agent': user_agent})


    def parse_photo(self, response):

        data = json.loads(response.body)

        if "_embedded" in data and "images" in data["_embedded"]:
            images = data["_embedded"]["images"]
            if images:
                photo_url = images[0]["_links"]["self"]["href"]
                user_agent = random.choice(self.USER_AGENTS)
                yield scrapy.Request(photo_url, callback=self.save_photo, headers={'User-Agent': user_agent})


    def save_photo(self, response):
        filename = response.url.split("/")[-1] + ".jpg"
        with open(filename, "wb") as f:
            f.write(response.body)
        self.log(f"Fotoğraf kaydedildi: {filename}")


    def parse_details(self, response):

        # Detay sayfasının yanıt verisini JSON formatında yükler
        data = json.loads(response.body)

        # InterpolscrapingItem nesnesi oluşturur
        item = InterpolscrapingItem()

        # Detayları ilgili alanlara ekler
        item['entity_id'] = data.get('entity_id')
        item['name'] = data.get('name')
        item['forename'] = data.get('forename')
        item['weight'] = data.get('weight')
        item['date_of_birth'] = data.get('date_of_birth')
        item['languages_spoken_ids'] = data.get('languages_spoken_ids')
        item['nationalities'] = data.get('nationalities')
        item['sex_id'] = data.get('sex_id')
        item['country_of_birth_id'] = data.get('country_of_birth_id')
        item['distinguishing_marks'] = data.get('distinguishing_marks')
        item['eyes_colors_id'] = data.get('eyes_colors_id')
        item['hairs_id'] = data.get('hairs_id')
        item['place_of_birth'] = data.get('place_of_birth')

        yield item

