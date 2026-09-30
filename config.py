import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "smartlead-secret-key")
    DATABASE_URL = os.environ.get("DATABASE_URL", "smartlead.db")
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
    AI_PROVIDER = os.environ.get("AI_PROVIDER", "groq")
    CORS_ORIGINS = os.environ.get("CORS_ORIGINS", "*")

    BUSINESS_CONTEXT = os.environ.get(
        "BUSINESS_CONTEXT",
        """
        Sen, KÖK Architecture & Woodwork'un yapay zeka asistanisin.
        Mimari tasarim, iç mimarlik ve ahsap tasarim-uygulama
        hizmetleri hakkinda ziyaretcilere bilgi ver.
        Kibar, profesyonel ve anlasilir bir dille Turkce konus.
        Gerektiginde ziyaretciyi iletisim bilgilerini birakmaya yonlendir. 
        Eğer müşteri sorarsa senin iletişim bilgilerin, (Adres: Üsküdar, İstanbul, Kuzguncuk Mah. İcadiye Cad. No: 24), (Telefon: 0216 000 00 00), (E-posta: info@kokarchitecture.com), sadece benim yazdığım iletişim bilgilerini ver.
          """
    )


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}