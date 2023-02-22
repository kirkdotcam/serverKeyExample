from flask import Flask,jsonify, request
import uuid
import requests

app = Flask(__name__)
key_generated = False
key_received = False
opto_key = ""
tes_key = ""

def generate_key():
  if (key_generated == False):
    return uuid.uuid1()
  return None

@app.route("/")
def home():
  return jsonify({"msg":"ok"})

@app.route("/evilprinter")
def evilprinter():
  return jsonify({
    "keygen":key_generated,
    "kerec":key_received,
    "opto_key":opto_key,
    "tes_key": tes_key
    })

if (__name__ =="__main__"):
 
  res = requests.get("http://localhost:5000/keygen").json()
  
  res_key = res.get("key")
  if res_key is not None:
    tes_key = res_key

  opto_key = generate_key()
  print(opto_key)
  res = requests.post("http://localhost:5000/receivekey", data={"key":f"{opto_key}"})
  print(res)
  key_generated = True 	
  app.run(debug=False, port=5001)
