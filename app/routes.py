from flask import Blueprint, render_template, request, jsonify

from app.database import lead_ekle, tum_leadler
from app.services.ai_service import ai_service, AIServiceError


# Normal web sayfalari
pages = Blueprint("pages", __name__)

# API islemleri
api = Blueprint("api", __name__)


@pages.route("/")
def index():
    return render_template("index.html")


@pages.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@api.route("/sohbet", methods=["POST"])
def sohbet():
    data = request.get_json(silent=True) or {}
    mesaj = data.get("mesaj")

    if not mesaj:
        return jsonify({
            "basari": False,
            "hata": "Mesaj alani zorunludur."
        }), 400

    try:
        cevap = ai_service.yanit_uret(mesaj, [])

        return jsonify({
            "basari": True,
            "cevap": cevap
        })

    except AIServiceError:
        return jsonify({
            "basari": False,
            "hata": "Yapay zeka servisine su anda ulasilamiyor."
        }), 503


@api.route("/leads", methods=["POST"])
def lead_kaydet():
    data = request.get_json(silent=True) or {}

    isim = data.get("isim")
    telefon = data.get("telefon")
    mesaj = data.get("mesaj", "")

    if not isim or not telefon:
        return jsonify({
            "basari": False,
            "hata": "Isim ve telefon alanlari zorunludur."
        }), 400

    try:
        lead_ekle(isim, telefon, mesaj)

        return jsonify({
            "basari": True,
            "mesaj": "Lead basariyla kaydedildi."
        }), 201

    except Exception:
        return jsonify({
            "basari": False,
            "hata": "Lead kaydedilirken bir hata olustu."
        }), 500


@api.route("/leads", methods=["GET"])
def leadleri_getir():
    try:
        leads = tum_leadler()

        return jsonify({
            "basari": True,
            "leads": leads
        })

    except Exception:
        return jsonify({
            "basari": False,
            "hata": "Leadler getirilirken bir hata olustu."
        }), 500