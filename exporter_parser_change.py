def zipkin_transport_handler(message):
    global zipkin_producer
    if zipkin_transport == 'kafka':
        if event_acknowledgement == False:
            future = zipkin_producer.send(zipkin_topic, message)
        else:
            future = zipkin_producer.send(zipkin_topic, message)
            record_metadata = future.get(timeout=10)
            logger.info("Successfully written into kafka : topic= : " + record_metadata.topic)
