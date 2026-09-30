import os
from flask import Flask, jsonify
from flask_cors import CORS  # CORS kütüphanesini içeri aktardık

from config import DevelopmentConfig
from app.database import init_db
from app.routes import pages, api

def create_app():
    app = Flask(__name__)
    
    # ---------------------------------------------------------
    # CORS İzni: Wix sitenizin API ile sorunsuz haberleşebilmesi için eklendi
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    # ---------------------------------------------------------

    # Ayarları yükle
    app.config.from_object(DevelopmentConfig)

    # Veritabanını hazirla
    init_db(app)

    # Sayfa ve API route'larini kaydet
    app.register_blueprint(pages)
    app.register_blueprint(api, url_prefix="/api")

    # Sunucunun calisip calismadigini kontrol eden route (Eksiksiz olarak eklendi)
    @app.route("/health")
    def health():
        return jsonify({
            "basari": True,
            "durun": "aktif",
            "mesaj": "SmartLead AI calisiyor."
        })

    return app