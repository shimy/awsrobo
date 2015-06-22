# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import os
import sys
import boto
from boto.sqs.message import RawMessage

###### GPIO Initialization #####
GPIO.cleanup()

###### Action 00 #####
def action_00():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    p1 = GPIO.PWM(23, 50)
    p2 = GPIO.PWM(24, 50)
    p1.start(7.5)
    p2.start(7.5)

    try:
        p1.ChangeDutyCycle(7.5)
        p2.ChangeDutyCycle(7.5)
        time.sleep(0.3)
        GPIO.cleanup()

    except KeyboardInterrupt:
        GPIO.cleanup()

###### Action 01 #####
def action_01():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    p1 = GPIO.PWM(23, 50)
    p2 = GPIO.PWM(24, 50)
    p1.start(7.5)
    p2.start(7.5)

    try:
        for var in range(0, 4):
            p1.ChangeDutyCycle(9.5)
            p2.ChangeDutyCycle(9.5)
            time.sleep(0.4)
            p1.ChangeDutyCycle(5.5)
            p2.ChangeDutyCycle(5.5)
            time.sleep(0.4)

        p1.ChangeDutyCycle(7.5)
        p2.ChangeDutyCycle(7.5)
        time.sleep(0.3)
        GPIO.cleanup()

    except KeyboardInterrupt:
        GPIO.cleanup()

##### Main #####
action_00()
action_01()

"""
conn = boto.connect_sqs('ACCESS_KEY','SECRET_KEY')
queue = conn.get_queue('QUEUE_NAME')
queue.set_message_class(RawMessage)
while 1:
    messages = queue.get_messages(1)
    for message in messages:
        msg = message.get_body()
        print(msg)
        queue.delete_message(message)
        action_00()
        action_01()
"""
