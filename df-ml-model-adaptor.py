import requests
from flask import Flask, request

@app.route("/webhook", methods=['GET', 'POST'])

def receive_message():
    return "This is it"