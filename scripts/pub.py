import redis
import random
import time

queue = redis.StrictRedis(
    host='50.30.35.9',
    password='9a822a92a0060c0ac8ab7c0bcd167a31',
    port=3097,
    db=0)
channel = queue.pubsub()

for i in range(1000): 
    evt = '{ "CurrencyPair": "BTCUSD", "Rate":%s,"Timestamp":%s }' % (random.uniform(1.0, 1.05)* 1000.00, int(time.time()))
    queue.publish("BTCUSD:Rate", evt)
    print "published %s " % evt 
    sleep = random.randint(0,10)
    time.sleep(sleep)
