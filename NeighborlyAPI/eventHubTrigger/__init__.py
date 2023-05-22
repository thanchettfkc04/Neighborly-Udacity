import json
import logging
import azure.functions as func


def main(event: func.EventHubEvent):
    result = json.dumps({
        'id': event.id,
        'data': event.get_json(),
        'topic': event.topic,
        'subject': event.subject,
        'event_type': event.event_type,
    })


    logging.info('Python EventHub trigger processed an event: %s', result)



