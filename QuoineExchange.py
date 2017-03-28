'''
Module for retrieving data from MAS site
'''
import settings
import string
import time

from helper import get_response

class QuoineExchange(object):
    ''' Class for retrieving data from Quoine '''

    def __init__(cls):
        cls.URL = "{0:s}://{1:s}".format(settings.PROTOCOL, settings.BASE_URL)
        pass

    def Pairs(cls):
        url = "%s%s"  % (cls.URL,"/products")
        return get_response(url)

    def Rate(cls, id):
        url = "%s%s/%s"  % (cls.URL,"/products", id)
        return get_response(url)
		
q = QuoineExchange()
pairs = q.Pairs()
Do = True
Sum = 0.00
PrevSum = 0.00
while Do == True:
    for pair in pairs:
        rate = q.Rate(pair["id"])
        if pair["base_currency"] == "BTC":
            print(pair["currency_pair_code"], "[",pair["id"], "] ",float(1.00/rate["exchange_rate"]))
            Sum += float(rate["exchange_rate"])
    if PrevSum == 0.00:
        PrevSum = Sum
    print("Sum %s vs Prev %s " % (Sum, PrevSum))
    if Sum != PrevSum:
        print("\n\nExchange Rates changed!!!!\n\n")
    time.sleep(10)
 