#!/usr/bin/env python3

import paho.mqtt.client as mqtt


# This is the Publisher
class Publisher:
    _topic = "topic/init"

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._client.disconnect()

    def __init__(self, topic: str, hostname: str = "localhost", port: int = 1883):
        self._client = mqtt.Client()
        self._client.connect(hostname, port, 60)
        self._topic = topic

    def send_message(self, message):
        self._client.publish(self._topic, message)


if __name__ == "__main__":
    with Publisher("topic/test") as p:
        p.send_message("hi whats the context for you, are you connected?")
