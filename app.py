from services import registry, signal
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Route signal de trade
@app.route("/canTrade")
def canTrade():
    if(signal.canTrade()):
        return "true"
    else:
        return "false"

# Route pour pouvoir lire le fichier d'événements
@app.route("/getEvents")
def getEvents():
    return signal.loadData()

# Route pour pouvoir lire le registre
@app.route("/getRegistry")
def getRegistry():
    return registry.loadRegistry()


if __name__ == "__main__":
    app.run(host='0.0.0.0')