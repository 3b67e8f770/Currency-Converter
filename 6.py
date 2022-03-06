#!/usr/bin/env python3
import requests
import json


def main():
    currency1 = input()
    rates = {}
    url = "http://www.floatrates.com/daily/"+currency1.lower()+".json"
    x = requests.get(url)
    y = x.json()
    if currency1.upper() == "USD":
        rates["USD"] = 1
    else:
        USD = y['usd']['rate']
        rates["USD"] = USD
    if currency1.upper() == "EUR":
        rates["EUR"] = 1
    else:
        EUR = y['eur']['rate']
        rates["EUR"] = EUR
    while True:
        currency2 = input()
        if currency2 == "":
            break
        how_much = float(input())
        print("Checking the cache...")
        if currency2.upper() in rates.keys() or currency2.lower() in rates.keys():
            print("Oh! It is in the cache!")
        else:
            rates[currency2] = y[currency2.lower()]['rate']
            print("Sorry, but it is not in the cache!") 
        _x=how_much * float(y[currency2.lower()]['rate'])
        _x = int(_x * 100) / 100
        _y=currency2
        print(f"You received {_x} {_y}.")
            
    
if __name__=="__main__":
    main()
