from pymongo import MongoClient
import json
from bson import ObjectId   
import base64

mongouri = "mongodb://user:pass@localhost:27017/"
db_name = "postgredata"
collection_name = "movie"

client = MongoClient(mongouri)



from confluent_kafka import Consumer, KafkaError, KafkaException

conf = {'bootstrap.servers': 'localhost:9092',
        'group.id': 'movie',
        'auto.offset.reset': 'smallest'}

consumer = Consumer(conf)
running = True


def get_float(number):
    decoded_bytes = base64.b64decode(number['value'])
    result = float(''.join(str(ord(char)) for char in decoded_bytes.decode("utf-8")))
    return result if number['scale'] ==0 else result/10
def msg_process(msg,db):
    data = json.loads(msg.value().decode('utf-8'))
    status = 'after'
    if data['payload']['op']=='d':
        status = 'before'
    data_dict = {
        'id': data['payload'][status]['id'],
        'title': data['payload'][status]['title'],
        'year': data['payload'][status]['year'],
        'director': data['payload'][status]['director'],
        'rating': get_float(data['payload'][status]['rating']),
    }
    if data['payload']['op']=='c':
        db[collection_name].insert_one(data_dict)
        print('created')
    elif data['payload']['op']=='r':
        print('readed')
    elif data['payload']['op']=='u':
        db[collection_name].update_one({'id': data_dict['id']},{'$set':data_dict})
        print('updated')
    elif data['payload']['op']=='d':
        db[collection_name].delete_one({'id':data_dict['id']})
        print('deleted')
    
def basic_consume_loop(consumer, topics):
    try:
        db = client[db_name]
        if collection_name not in db.list_collection_names():
            db.create_collection(collection_name)

        consumer.subscribe(topics)

        while running:
            msg = consumer.poll(timeout=1.0)
            if msg is None or msg.value() is None: continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                msg_process(msg,db)
    finally:
        # Close down consumer to commit final offsets.
        consumer.close()
        client.close()


def shutdown():
    running = False

basic_consume_loop(consumer,['postgres.public.movies'])