import uuid
#import rsa
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
  pass

def generate_key():
  return uuid.uuid1()

print(generate_key())
