#!/usr/bin/env python3

import paho.mqtt.client as mqtt


class Subscriber:
    _client = None
    _topic = ""

    def _on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.subscribe(self._topic)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._client.disconnect()

    def __init__(self, on_message_callback, topic: str, hostname: str = "localhost", port: int = 1883):
        client = mqtt.Client()
        print(hostname)
        client.connect(hostname, port, 60)
        client.on_connect = self._on_connect
        client.on_message = on_message_callback
        self._client = client
        self._topic = topic

    def subscribe(self):
        self._client.loop_forever()


if __name__ == '__main__':
    def on_message(client, userdata, msg):
        print(len(msg.payload))

    with Subscriber(on_message, 'topic/video') as s:
        s.subscribe()
