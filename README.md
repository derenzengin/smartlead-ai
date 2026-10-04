SmartLead AI — Yapay Zekâ Destekli Lead Toplama Asistanı
SmartLead AI, web sitenize gelen ziyaretçilerle yapay zekâ aracılığıyla doğal sohbetler gerçekleştiren ve potansiyel müşterilerin iletişim bilgilerini (lead) güvenli bir şekilde toplayarak veritabanına kaydeden, ölçeklenebilir bir backend altyapısıdır.

🚀 Projenin Amacı ve Temel Özellikleri
🤖 Yapay Zekâ Destekli Sohbet Botu: Groq API (Llama modeli) altyapısını kullanarak ziyaretçilerin sorularını anında, akıllıca ve doğal bir dille yanıtlar.

📋 Otomatik Lead Toplama: Potansiyel müşterilerin ad, telefon, e-posta ve mesaj bilgilerini diyalog akışı içerisinde eksiksiz toplar.

🛡️ Güvenli Veritabanı Yönetimi: Verileri SQLite altyapısında saklar; SQL Injection saldırılarına karşı tam korumalı parametrik sorgular kullanır.

🧩 Modüler ve Sürdürülebilir Mimari: Sorumlulukların Ayrılığı (Separation of Concerns) ilkesine uygun olarak tasarlanmıştır (database.py, ai_service.py, routes.py).

🌐 Wix Velo ve Dış Sistem Entegrasyonu: Ön yüzde Wix veya herhangi bir modern web arayüzü ile RESTful API üzerinden sorunsuz haberleşir.

🏗️️ Proje Dosya Yapısı (Hedef Mimari)
Plaintext
Smartlead_ai/
├── run.py                 # Uygulamayı başlatan giriş noktası (Entry Point)
├── config.py              # Ortam ve uygulama yapılandırma ayarları
├── requirements.txt       # Proje bağımlılıkları ve kütüphaneler
├── .env                   # Gizli anahtarlar ve çevre değişkenleri (Git'e eklenmez)
├── .gitignore             # Git tarafından izlenmeyecek dosyalar
└── app/
    ├── __init__.py        # Uygulama fabrikası (create_app)
    ├── database.py        # SQLite veritabanı işlemleri ve CRUD fonksiyonları
    ├── routes.py          # HTTP API uç noktaları (Endpoints)
    ├── templates/         # HTML şablonları (Gerekli arayüzler için)
    └── services/
        └── ai_service.py  # Groq AI servis entegrasyonu ve sohbet mantığı
🔑 Groq API Anahtarı Nasıl Alınır?
Yapay zekâ modelini aktif hale getirmek için ücretsiz bir Groq API anahtarına ihtiyacınız vardır:

console.groq.com adresine gidin ve ücretsiz bir hesap oluşturun.

Giriş yaptıktan sonra sol menüde yer alan "API Keys" sekmesine tıklayın.

"Create API Key" butonuna basın, anahtarınıza bir isim verin ve oluşturun.

gsk_ ile başlayan API anahtarınızı güvenli bir yere kopyalayın. (Bu anahtar güvenlik nedeniyle tekrar gösterilmez, kaybetmeniz durumunda yenisini oluşturmanız gerekir).

🛠️ Kurulum ve Yerel Çalıştırma
1. Depoyu Klonlayın
Bash
git clone https://github.com/stastegy-spec/Smartlead_ai.git
cd Smartlead_ai
2. Sanal Ortam (Venv) Oluşturun ve Aktif Edin
Windows:

DOS
python -m venv venv
venv\Scripts\activate
Mac / Linux:

Bash
python3 -m venv venv
source venv/bin/activate
3. Bağımlılıkları Yükleyin
Bash
pip install -r requirements.txt
4. .env Dosyasını Oluşturun
Proje kök dizininde .env adında bir dosya oluşturun ve içerisine aşağıdaki değişkenleri tanımlayın:

Kod snippet'i
SECRET_KEY=gizli_ve_guvenli_bir_anahtar
GROQ_API_KEY=gsk_sizin_groq_api_anahtariniz
5. Sunucuyu Başlatın
Bash
python run.py
Sunucu varsayılan olarak http://localhost:5000 adresinde çalışmaya başlayacaktır.

☁️ Render.com Üzerinden Canlıya Alma (Deploy)
Projeyi internet üzerinden erişilebilir hale getirmek ve Wix sitenize bağlamak için Render platformunu kullanabilirsiniz:

render.com adresine gidin ve GitHub hesabınızla giriş yapın.

Kontrol panelinde sağ üstteki "New +" butonuna tıklayıp "Web Service" seçeneğini belirleyin.

GitHub depolarınız arasından Smartlead_ai projesini seçin ve "Connect" butonuna basın.

Yapılandırma ayarlarını aşağıdaki gibi doldurun:

Name: Projenize bir isim verin (Örn: smartlead-ai)

Environment: Python 3

Build Command: pip install -r requirements.txt

Start Command: gunicorn run:app

Environment Variables (Çevre Değişkenleri) bölümüne gidin ve şu iki gizli anahtarı ekleyin:

GROQ_API_KEY ➔ gsk_... (Groq'tan aldığınız anahtar)

SECRET_KEY ➔ karmaşık-ve-güvenli-bir-metin

En altta yer alan "Create Web Service" butonuna tıklayarak dağıtımı başlatın.

Dağıtım tamamlandığında size [https://siteniz-adi.onrender.com](https://siteniz-adi.onrender.com) şeklinde canlı bir URL verilecektir. Wix Velo kodlarınızdaki fetch istek adresini bu yeni URL ile güncellemeyi unutmayın!
