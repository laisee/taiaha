import redis
import time

r = redis.StrictRedis(
    host='50.30.35.9',
    password='9a822a92a0060c0ac8ab7c0bcd167a31',
    port=3097,
    db=0)

p = r.pubsub()
p.subscribe('BTCUSD:Rate')

while True:
    message = p.get_message()
    if message:
        print "Subscriber: %s" % message['data']
    time.sleep(1)
