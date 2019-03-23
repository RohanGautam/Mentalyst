# import webbrowser
# import requests
# from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options
from pprint import pprint
import sys

options = Options()
options.headless = True

browser = webdriver.Firefox(options=options)

url = "https://www.google.com/search?client=ubuntu&channel=fs&q={}%3Apolitifact.com"

claim = '/html/body/div[6]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[{}]/div/div/div[2]/div[1]/span'
claimedBy = '/html/body/div[6]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[{}]/div/div/div[2]/div[2]/span'
factCheck = '/html/body/div[6]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[{}]/div/div/div[2]/div[3]/span'


def factChecker(sentence):
    # sentence="elections were hacked"
    sentence = '%20'.join(sentence.split())
    browser.get(url.format(sentence))
    time.sleep(1)
    d = {}
    count = 0
    for i in range(10):
        try:
            fact_check = browser.find_element_by_xpath(factCheck.format(i))
            claim_by = browser.find_element_by_xpath(claimedBy.format(i))
            Claim = browser.find_element_by_xpath(claim.format(i))
            # print('Claim: '+Claim.text)
            # print('Claim by: '+claim_by.text)
            # print('Verdict: '+fact_check.text)
            # print('-----------')
            d[count] = {'claim': Claim.text,
                        'claimBy': claim_by.text, 'verdict': fact_check.text}
            count += 1
        except:
            pass
    return (d)


args = sys.argv
if len(args) == 2:
    d = factChecker(args[1])
    print(d)
    sys.stdout.flush()
# pprint(factChecker('obama is african'))
