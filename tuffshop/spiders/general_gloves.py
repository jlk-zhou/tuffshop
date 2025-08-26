import scrapy
from scrapy.loader import ItemLoader
from tuffshop.items import TuffshopItem


class GeneralGlovesSpider(scrapy.Spider):
    name = "general_gloves"
    allowed_domains = ["tuffshop.co.uk"]

    def start_requests(self): 
        # # Locate javascript files
        # base_dir = Path(__file__).resolve().parents[2]
        # wait_path = base_dir / "scripts" / "waitForElements.js"  
        
        # # Load waiting for elements to render script
        # with open(wait_path, "r") as f: 
        #     wait_script = f.read() 

        # Return the page only after all products are loaded
        url = "https://tuffshop.co.uk/ppe-safety/work-safety-gloves/general-work-gloves.html?product_list_limit=all"
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36", 
            "upgrade-insecure-requests": 1, 
            "sec-fetch-user": "?1", 
            "sec-fetch-site": "same-origin", 
            "sec-fetch-mode": "navigate", 
            "sec-fetch-dest": "document", 
            "sec-ch-ua-platform": "macOS", 
            "sec-ch-ua-mobile": "?0", 
            "sec-ch-ua": '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"', 
            "priority": "u=0, i", 
            "cookie": '_fbp=fb.2.1756025384907.461028446252063931;_ga=GA1.1.1452309863.1756025385;_ga_J3KQPF0TD1=GS2.1.s1756086185$o6$g1$t1756086248$j57$l0$h725720487$dsxbGTVF5QO-Y0in45c1tye-TjWtsWQOWjg;_gcl_au=1.1.894262764.1756025384;_gcl_aw=GCL.1756025411.Cj0KCQjw8KrFBhDUARIsAMvIApYXkdAqTUdtLCHxayLhvuynn8VR_N0DL725-C6N1zYH7dJRJReUDU4aArcUEALw_wcB;_gcl_gs=2.1.k1$i1756025378$u24239679;analytics_cookies=0;cookie_closed=1;cookie_declined=1;form_key=GCBqIHaW8vLGdjLT;functional_cookies=0;marketing_cookies=0;PHPSESSID=5alaaub7f33sgnfngq7as02uvv;required_cookies=1;sf_id=6deaa157-60ce-4fe6-a46a-7b839e6f763b;sf_session_id.89ae=cdfdccdf-194f-4f6c-a33a-8b6a7a8b4d09.1756025385.7.1756086432.1756046301.06aaa733-1804-4781-b3e9-71dee288b68f;sf_session_ses.89ae=*;twk_uuid_64943bea94cf5d49dc5f3957=%7B%22uuid%22%3A%221.7xaQFHFFYoahmhKPDEOBnqzeG7sTBiyng7gNPubpPju3QWF7HQzJWZyI4WhLPlXLDovsKfpZgUXNaokkh1wvoesYJdXRJysqKKsYKyeUDBTLA52gtXC8LiB7%22%2C%22version%22%3A3%2C%22domain%22%3A%22tuffshop.co.uk%22%2C%22ts%22%3A1756086254100%7D;form_key=GCBqIHaW8vLGdjLT;mage-cache-sessid=true;mage-cache-storage={};mage-cache-storage-section-invalidation={};mage-messages=;private_content_version=872238c8dc81c23af5cfae832bcbf2de;product_data_storage={};recently_compared_product={};recently_compared_product_previous={};recently_viewed_product={};recently_viewed_product_previous={};section_data_ids={%22amfacebook-pixel%22:1756086258};TawkConnectionTime=0;twk_idm_key=NhsMlq3fjCsPrWN-Gj6Ct;', 
            "cache-control": "max-age=0", 
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-CN;q=0.6,zh;q=0.5", 
            "accept-encoding": "gzip, deflate, br, zstd", 
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
        }
        yield scrapy.Request(url, headers=headers, meta={
            "playwright": True
        })

    def parse(self, response): 
        # Yield a TuffshopItem class for every product card available
        for product in response.css(".item.product.product-item"): 
            l = ItemLoader(item=TuffshopItem(), selector=product)
            l.add_css("name", ".product-item-link::text")
            l.add_css("price", ".price-including-tax .price::text")
            l.add_css("price_notax", ".price-excluding-tax .price::text")
            l.add_xpath("url", './/a[@class="overlay-link"]/@href')
            l.add_xpath("image_url", './/img[@class="product-image-photo"]/@src')

            if not product.css(".stock.unavailable"): 
                l.add_value("in_stock", "Yes")
            else:   
                l.add_value("in_stock", "No")
                
            yield l.load_item()