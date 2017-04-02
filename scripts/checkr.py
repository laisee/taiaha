import redis
import time

rate = 0.00
while True:
    try:
        conn = redis.Redis(
            host='50.30.35.9',
            password='9a822a92a0060c0ac8ab7c0bcd167a31',
            port=3097,
            db = 0)
        latest = float(conn.get("BTCPHP"))
        print 'Got Record:', latest, " vs cached value ", rate 
        if float(latest) != rate:
           print "BTC/PHP rate changed from %s to %s " % (rate,latest)
           rate = latest 
    except Exception as ex:
        print 'Error:', ex
    print "Sleeping ...\n"
    time.sleep(10)
