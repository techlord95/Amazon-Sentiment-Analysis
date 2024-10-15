from requests_html import HTMLSession
from amazoncaptcha import AmazonCaptcha
import json
import time
import random
import csv

class Reviews:
    def __init__(self,asin) -> None:
        self.asin=asin
        self.session=HTMLSession()
        # self.url=f"https://www.amazon.in/Stardust-Storage-Powered-Mediatek-Display/product-reviews/{self.asin}/B0CMTTRN8M/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber="
        # self.url=f"https://www.amazon.in/realme-Feather-Segment-Charging-Slimmest/product-reviews/{self.asin}/B0CKN56PQ8/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber="
        # self.url=f"https://www.amazon.in/iQOO-Stellar-Snapdragon-Segment-Included/product-reviews/{self.asin}/B07WHSR1NR/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber="
        # self.url=f"https://www.amazon.in/OnePlus-Nord-Pastel-128GB-Storage/product-reviews/{self.asin}/B0BY8JZ22K/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber="
        # self.url=f'https://www.amazon.in/iQOO-MediaTek-Dimesity-Processor-Smartphone/product-reviews/{self.asin}/B07WGPJPR3/ref=cm_cr_arp_d_paging_btm_next_?ie=UTF8&reviewerType=all_reviews&pageNumber='
        # self.url=f'https://www.amazon.in/realme-Cosmic-Display-SUPERVOOC-Charger/product-reviews/{self.asin}/B0C78869XJ/ref=cm_cr_arp_d_paging_btm_next_?ie=UTF8&reviewerType=all_reviews&pageNumber='
        # self.url=f"https://www.amazon.in/Samsung-Segments-Smartphone-Octa-Core-Processor/product-reviews/{self.asin}/B0BZCWLJHK/ref=cm_cr_arp_d_paging_btm_next_?ie=UTF8&reviewerType=all_reviews&pageNumber="
        # self.url=f'https://www.amazon.in/Samsung-Segments-Smartphone-Octa-Core-Processor/product-reviews/{self.asin}/B0BZCR6TNK/ref=cm_cr_arp_d_paging_btm_next_?ie=UTF8&reviewerType=all_reviews&pageNumber='
        # self.url=f"https://www.amazon.in/Nokia-Powered-Snapdragon%C2%AE-Virtual-Upgrades/product-reviews/{self.asin}/B0CVL9MSCK/ref=cm_cr_arp_d_paging_btm_next_?ie=UTF8&reviewerType=all_reviews&pageNumber="
        # self.url=f'https://www.amazon.in/realme-Display-Premium-Leather-SUPERVOOC/product-reviews/{self.asin}/B0C788SHHC/ref=cm_cr_arp_d_paging_btm_next_?ie=UTF8&reviewerType=all_reviews&pageNumber='
        self.url=f'https://www.amazon.in/OnePlus-Nord-Shadow-Storage-256GB/product-reviews/{self.asin}/B0B3CZ7P4V/ref=cm_cr_arp_d_paging_btm_next_?ie=UTF8&reviewerType=all_reviews&pageNumber='
  
        self.user_agents=[
    'Mozilla/5.0 (iPad; CPU OS 14_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/122.0 Mobile/15E148 Safari/605.1.15',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/121.0.6167.171 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/94.0.992.31 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0 (Edition beta',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.14',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Mobile/15E148 Safari/604.',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Mobile/15E148 Safari/604.',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.2277.112',
    'Mozilla/5.0 (Linux; Android 10; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36 OPR/76.2.4027.73374',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    # Add more User-Agents if you want
]

    def pagination(self,page):
        headers={'User-Agent':random.choice(self.user_agents)}
        link=self.url.replace('btm_next_2','btm_next_'+str(page))
        r=self.session.get(link)
        # r=self.session.get(self.url+str(page))
        if r.status_code == 503:  # Amazon shows a CAPTCHA page
            captcha = AmazonCaptcha.fromdriver(r)
            solution = captcha.solve()
            if solution == 'Not solved':
                print('Failed to solve CAPTCHA')
                return False
            else:
                print('CAPTCHA solution:', solution)
                # Here you should use the solution to bypass the CAPTCHA.
                # This depends on how Amazon uses the CAPTCHA in their system.
                # You might need to send a POST request with the solution or use it in some other way.
        elif not r.html.find('div[data-hook=review]'):
            return False 
        else:
            return r.html.find('div[data-hook=review]')
        
    def parse(self,reviews):
        total=[]
        for review in reviews:
            title=review.find('a[data-hook=review-title]',first=True).text
            rating=review.find('i[data-hook=review-star-rating] span',first=True).text
            body=review.find('span[data-hook=review-body] span',first=True).text.replace('\n','').strip()

            data={
                'title':title,
                'rating':rating,
                'body':body[:50]
            }
            total.append(data)
        return total
    
    # def save(self,results):
    #     with open(self.asin+'-reviews.json','w') as f:
    #         json.dump(results,f)
    def save(self, results):
        try:
            with open(self.asin + '-reviews.json', 'r') as f:
                existing_data = json.load(f)
        except FileNotFoundError:
            existing_data = []
            existing_data.extend(results)
        with open(self.asin + '-reviews.json', 'w') as f:
            json.dump(existing_data, f)

    
    # def save(self, results):
    #     with open(self.asin + '-reviews.csv', 'w', newline='') as f:
    #         writer = csv.writer(f)
    #         writer.writerows(results)
        

if __name__=='__main__':
    amazon=Reviews('B0B3CZ7P4V')
    results=[]
    for x in range(1,20):
        print('getting page',x)
        time.sleep(8)
        reviews=amazon.pagination(x)
        if reviews is not False:
            results.append(amazon.parse(reviews))
        else:
            print('no more pages')
            break
    amazon.save(results)
