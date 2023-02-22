from flask import Flask,jsonify, request
import uuid

app = Flask(__name__)
key_generated = False
key_received = False
opto_key = ""
tes_key = ""

def generate_key():
  global key_generated
  if (key_generated == False):
    return uuid.uuid1()
  return None

@app.route("/")
def home():
  return jsonify({"msg":"ok"})

@app.route("/keygen")
def keygen():
  global key_generated
  if (key_generated == False):
    global tes_key
    tes_key = generate_key()
    key_generated = True
    return jsonify({
      "key": tes_key, 
      "msg":"key generated", 
      "source":"TES" 
      })

  return jsonify({"msg":"ok"})

@app.route("/receivekey", methods=["POST"])
def receivekey():
  global key_received
  global opto_key
  

  body = request.values
  try:
    opto_key = body["key"]
    key_received = True
    return jsonify({"msg":"ok"})
  except:
    print("key receive failure. must restart server")
    return jsonify({"msg":"key not received"})

@app.route("/evilprinter")
def evilprinter():
  return jsonify({
    "keygen":key_generated,
    "kerec":key_received,
    "opto_key":opto_key,
    "tes_key": tes_key
    })

if (__name__ =="__main__"):
  app.run(debug=True)
