import redis
r = redis.Redis(host='localhost', port=6379, db=0)
sub = r.pubsub()
sub.subscribe("test_channel")
for item in sub.listen():
    print(item)