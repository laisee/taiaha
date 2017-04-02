'''
Module for retrieving data from MAS site
'''
import settings
import string
import redis
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


    def Read(cls,key):
        conn = redis.Redis(
            host='50.30.35.9',
            password='9a822a92a0060c0ac8ab7c0bcd167a31',
            port=3097,
            db = 0)
        if conn:
            print "reading %s " % (key)
            return conn.get(key)

    def Write(cls,key, value):
        conn = redis.Redis(
            host='50.30.35.9',
            password='9a822a92a0060c0ac8ab7c0bcd167a31',
            port=3097,
            db = 0)
        if conn:
            print "writing %s to %s " % (value, key)
            conn.set(key,value)

q = QuoineExchange()
pairs = q.Pairs()
Do = True
PrevSum = 0.00
while Do == True:
    Sum = 0.00
    print "\n++++++++++++++++\n"
    for pair in pairs:
        rate = q.Rate(pair["id"])
        print(pair["currency_pair_code"], "[",pair["id"], "] ",float(1.00/rate["exchange_rate"]))
        Sum += float(rate["exchange_rate"])

    print("Sum %s vs Prev %s " % (Sum, PrevSum))
    if Sum != PrevSum:
        PrevSum = Sum
        print("\n\nExchange Rates changed!!!!\n\n")
        for pair in pairs:
            rate = q.Rate(pair["id"])
            stored_rate = q.Read(pair["currency_pair_code"])
            if stored_rate and rate["exchange_rate"] != 1.00/float(stored_rate):
                print "Updating %s rate from %s to %s" % (pair["currency_pair_code"],stored_rate,1.00/rate["exchange_rate"])
                q.Write(pair["currency_pair_code"],1.00/rate["exchange_rate"])
    time.sleep(10)
