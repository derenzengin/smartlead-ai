import os 
 
from flask import Flask, jsonify
from flask_cors import CORS
 
from config import DevelopmentConfig
from app.database import init_db
from app.routes import pages, api


def create_app():
    app = Flask(__name__)

    # Ayarlari yukle
    app.config.from_object(DevelopmentConfig)

    # Veritabanini hazirla
    init_db(app)

    # Sayfa ve API route'larini kaydet
    app.register_blueprint(pages)
    app.register_blueprint(api, url_prefix="/api")

    # Sunucunun calisip calismadigini kontrol eden route
    @app.route("/health")
    def health():
        return jsonify({
            "basari": True,
            "durum": "aktif",
            "mesaj": "SmartLead AI calisiyor."
        })

    return app