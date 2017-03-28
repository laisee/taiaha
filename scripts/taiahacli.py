import redis
import time

while True:
    try:
        conn = redis.Redis(
            host='50.30.35.9',
            password='9a822a92a0060c0ac8ab7c0bcd167a31',
            port=3097,
            db = 0)
        print 'INCR Counter:', conn.incr("counter")
        print 'Set Record:', conn.set("best_car_ever", "Tesla Model S")
        print 'Get Record:', conn.get("best_car_ever")
        time.sleep(10)
        print 'Delete Record:', conn.delete("best_car_ever")
        print 'Get Deleted Record:', conn.get("best_car_ever")
    except Exception as ex:
        print 'Error:', ex
    print "Sleeping ...\n"
    time.sleep(20)
