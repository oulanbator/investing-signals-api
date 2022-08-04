from services import registry, signal, settings
from utilities import constants, utils
from flask import Flask, request
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

# Route pour obtenir l'heure du serveur
@app.route("/getServerTime")
def getServerTime():
    return utils.getTimeNow()

# Route pour obtenir l'heure modifiée avec décalage horaire
@app.route("/getModifiedTime")
def getModifiedTime():
    return utils.getModifiedTimeNow()

# Route pour définir le décalage horaire
@app.route("/setDecalage")
def setDecalage():
    key = constants.DECALAGE_HORAIRE
    value = request.args.get("value")
    if (value.isnumeric()):
        settings.addSetting(key, int(value))
        return "Décalage mis à jour"
    else:
        return "Erreur : mauvaise valeur ?"

    

if __name__ == "__main__":
    app.run(host='0.0.0.0')
