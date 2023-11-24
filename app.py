from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)

api = Api(app)

CORS (app)

# inisiasi variabel kosong disini bertipe dictonary
identitas = {}



class ContohResource(Resource):
    # ini methode GET dan Post
    def get(self):
        # response = {"msg": "Halo, Selamat Datang"}
        return identitas
    
    def post(self):
        nama = request.form['nama']
        umur = request.form["umur"]
        identitas["nama"] = nama
        identitas["umur"] = umur
        response = {"msg" : "Data berhasil masuk"}
        return response



    # setup resource
api.add_resource(ContohResource, "/api", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5003)

