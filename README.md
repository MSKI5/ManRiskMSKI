# 🎯 Sistem Manajemen Risiko KPPN

Sistem manajemen risiko online terpusat untuk KPPN yang mengumpulkan, menganalisis, dan memantau risiko operasional dari lima seksi berbeda.

## ✨ Fitur Utama

- ✅ **Multi-User Multi-Section**: MSKI, Bank, PD, Vera, Subbagian Umum
- ✅ **26 Indikator Risiko**: IKU, Non-IKU, Mandatory
- ✅ **Kalkulasi Otomatis**: Frekuensi (1-5) × Dampak (1-5) = Risiko (1-25)
- ✅ **Matriks Risiko Visual**: 5 kategori warna (Biru, Hijau, Kuning, Jingga, Merah)
- ✅ **Tracking P26 & R26**: Monitoring penurunan risiko per quarter
- ✅ **Real-time Updates**: Sistem update otomatis saat ada perubahan data
- ✅ **Export & Laporan**: Excel, PDF, CSV, ZIP
- ✅ **Dokumen Pendukung**: Upload bukti perubahan risiko
- ✅ **Quarter-Based Locking**: Edit hanya pada bulan yang ditentukan
- ✅ **Audit Trail Lengkap**: Semua perubahan tercatat

## 📋 26 Indikator Risiko

### IKU (13 indikator)
```
1a-CP-01: Satker tidak valid dalam mengisi capaian output (PIC: MSKI) | P26: 14, R26: 10
1a-CP-02: Rendahnya nilai kualitas pelaksanaan anggaran (PIC: MSKI) | P26: 19, R26: 16
1a-CP-03: Satker terlambat menyampaikan pertanggungjawaban UP/TUP (PIC: MSKI) | P26: 19, R26: 15
2a-CP-01: Edukasi dan komunikasi yang tidak optimal (PIC: MSKI) | P26: 13, R26: 10
2a-CP-02: Respon pertanyaan/konsultasi tidak tepat waktu (PIC: MSKI, Subbagian Umum) | P26: 16, R26: 15
3a-CP-01: TKD tidak disalurkan tepat waktu (PIC: Seksi Bank) | P26: 16, R26: 15
3b-N-01: Waktu pengajuan SPM tidak sesuai RPD (PIC: MSKI, PD) | P26: 17, R26: 13
3b-N-02: Penyelesaian SP2D lebih dari 1 jam (PIC: PD) | P26: 17, R26: 13
3b-N-03: Bertambahnya jumlah retur (PIC: PD) | P26: 22, R26: 16
3b-N-04: Penyelesaian retur tidak tepat waktu (PIC: Vera) | P26: 14, R26: 10
4a-N-01: Keterlambatan LPJ bendahara (PIC: Vera) | P26: 16, R26: 15
4a-N-02: Terdapat satuan kerja terlambat tutup periode (PIC: Vera) | P26: 16, R26: 15
6a-CP-01 s/d 04: Pengelolaan Keuangan, BMN, Pengadaan, Arsip (4 indikator)
```

### Non-IKU (10 indikator)
```
2b-N-01, 3c-N-01, 5a-N-01, 5b-N-01, 5c-N-01, 6b-N-01
+ 3 indikator organisasi (Kehumasan, Website, Moral Hazard)
```

### Mandatory (3 indikator)
```
Persepsi negatif masyarakat, Ownership pegawai, Perilaku korupsi, Kebocoran data
```

## 📊 Matriks Risiko (Standar Warna)

```
┌─────────────────────────────────────────────────────────┐
│          DAMPAK (Besaran)                              │
│    1(Minimal) | 2(Rendah) | 3(Sedang) | 4(Tinggi) | 5  │
├─────────────────────────────────────────────────────────┤
│5(Sangat)  │   7   │   12    │   17    │   22    │ 25  │
│4(Sering)  │   4   │    9    │   14    │   19    │ 24  │
F│3(Sedang)  │   3   │    8    │   13    │   18    │ 23  │
R│2(Jarang)  │   2   │    6    │   11    │   16    │ 21  │
E│1(Jarang)  │   1   │    5    │   10    │   15    │ 20  │
└─────────────────────────────────────────────────────────┘

KATEGORI:
🟦 BIRU (1-3):      Risiko Rendah - Monitoring rutin
🟩 HIJAU (5-8):     Risiko Sedang Rendah - Monitoring berkala
🟨 KUNING (10-14):  Risiko Sedang - Perlu mitigasi
🟧 JINGGA (16-20):  Risiko Tinggi - Mitigasi segera
🟥 MERAH (21-25):   Risiko Sangat Tinggi - Prioritas utama
```

## 👥 User & Role

| Role | Akses | Tugas |
|------|-------|-------|
| **Admin** | Kelola semua data, verify, export | Monitoring keseluruhan |
| **MSKI User** | Input Q1-Q4 untuk risiko MSKI | Isi frekuensi, dampak, bukti |
| **Bank User** | Input Q1-Q4 untuk risiko Bank | Isi frekuensi, dampak, bukti |
| **PD User** | Input Q1-Q4 untuk risiko PD | Isi frekuensi, dampak, bukti |
| **Vera User** | Input Q1-Q4 untuk risiko Vera | Isi frekuensi, dampak, bukti |
| **Subbagian Umum User** | Input Q1-Q4 untuk risiko mereka | Isi frekuensi, dampak, bukti |

## 📅 Jadwal Input Data

```
📌 Quarter 1 (Q1):    Maret (01-31)       ✓ Edit hingga Mei
📌 Quarter 2 (Q2):    Juni (01-30)        ✓ Edit hingga Agustus
📌 Quarter 3 (Q3):    September (01-30)   ✓ Edit hingga November
📌 Quarter 4 (Q4):    Desember (01-31)    ✓ Edit hingga Februari

Pengisian di luar bulan yang ditentukan akan ditolak sistem.
```

## 🛠️ Tech Stack

### Backend
- **Framework**: Flask 2.3 (Python)
- **Database**: PostgreSQL 15 (Supabase)
- **Authentication**: JWT (JSON Web Token)
- **ORM**: SQLAlchemy
- **Server**: Gunicorn + Nginx
- **API**: RESTful
- **Password**: bcrypt

### Frontend
- **Framework**: Vue.js 3 (Composition API)
- **Build Tool**: Vite
- **State Management**: Pinia
- **Styling**: Tailwind CSS + Bootstrap 5
- **Charts**: Chart.js (Risk Matrix)
- **HTTP Client**: Axios
- **Form**: VeeValidate + Yup
- **Hosting**: GitHub Pages / Vercel

### Infrastructure
- **Database**: Supabase PostgreSQL
- **Storage**: Cloud Storage (untuk dokumen)
- **Deployment**: Docker, GitHub Actions
- **Version Control**: Git + GitHub

## 📦 Struktur Project

```
ManRiskMSKI/
├── 📁 backend/
│   ├── app.py                      # Main Flask application
│   ├── models.py                   # SQLAlchemy models (26 indikator)
│   ├── config.py                   # Configuration
│   ├── requirements.txt             # Python dependencies
│   ├── Dockerfile                   # Docker configuration
│   ├── 📁 routes/
│   │   ├── auth.py                # Login, register, JWT
│   │   ├── dashboard.py           # Dashboard & summary
│   │   ├── risiko.py              # Risk CRUD operations
│   │   ├── matriks.py             # Risk matrix & visualization
│   │   ├── laporan.py             # Reports & export
│   │   └── admin.py               # Admin functions
│   ├── 📁 services/
│   │   ├── risk_calculator.py     # Otomatis hitung risiko
│   │   ├── matrix_mapper.py       # Mapping ke kategori warna
│   │   ├── document_handler.py    # Upload & manage dokumen
│   │   └── export_handler.py      # Export Excel/PDF
│   └── 📁 utils/
│       ├── validators.py
│       ├── decorators.py
│       └── helpers.py
│
├── 📁 frontend/
│   ├── src/
│   │   ├── 📁 components/         # Reusable Vue components
│   │   │   ├── RiskForm.vue       # Form input frekuensi & dampak
│   │   │   ├── MatrixVisual.vue   # Matriks risiko 5x5
│   │   │   ├── RiskTable.vue      # Tabel data risiko
│   │   │   ├── ChangeTracker.vue  # Tracking perubahan Q1->Q2->Q3->Q4
│   │   │   ├── DocumentUpload.vue # Upload bukti pendukung
│   │   │   ├── Navbar.vue
│   │   │   └── Sidebar.vue
│   │   ├── 📁 views/              # Page components
│   │   │   ├── LoginPage.vue
│   │   │   ├── DashboardPage.vue
│   │   │   ├── InputDataPage.vue  # Form pengisian 26 indikator
│   │   │   ├── LihatDataPage.vue  # Lihat & edit data
│   │   │   ├── AnalisisPerubahan.vue # P26 -> R26 tracking
│   │   │   ├── LaporanPage.vue
│   │   │   └── AdminPage.vue
│   │   ├── 📁 store/              # Pinia store
│   │   │   ├── auth.js
│   │   │   ├── risiko.js
│   │   │   ├── matrix.js
│   │   │   └── ui.js
│   │   ├── 📁 utils/
│   │   │   ├── api.js             # API client (Axios)
│   │   │   ├── validators.js
│   │   │   └── helpers.js
│   │   ├── 📁 assets/
│   │   │   ├── logo.svg
│   │   │   └── styles/
│   │   ├── App.vue
│   │   └── main.js
│   ├── public/
│   ├── dist/                       # Build output untuk GitHub Pages
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── .env.example
│
├── 📁 database/
│   ├── schema.sql                 # Create tables (26 indikator)
│   ├── initial_data.sql           # Initial data & matrix mapping
│   └── migrations/
│
├── 📁 docs/
│   ├── PANDUAN_PENGGUNA.md        # User guide (Lengkap!)
│   ├── PANDUAN_ADMIN.md           # Admin guide
│   ├── API_DOCS.md                # API documentation
│   ├── DEPLOYMENT.md              # Deploy ke Supabase + GitHub Pages
│   ├── FAQ.md                     # Frequently Asked Questions
│   └── TROUBLESHOOTING.md
│
├── 📁 tests/
│   ├── test_auth.py
│   ├── test_risiko.py
│   └── test_export.py
│
├── docker-compose.yml              # Local development setup
├── nginx.conf                      # Nginx configuration
├── .env.example                    # Environment template
├── .gitignore
├── SETUP_GUIDE.md                 # Setup & deployment guide
└── LICENSE
```

## 🚀 Quick Start

### Setup Lokal (Development)

```bash
# Clone repository
git clone https://github.com/MSKI5/ManRiskMSKI.git
cd ManRiskMSKI

# Backend Setup
cd backend
python -m venv venv
source venv/bin/activate  # Mac/Linux
# atau venv\Scripts\activate  # Windows
pip install -r requirements.txt
cp .env.example .env
# Edit .env dengan DATABASE_URL Anda
python app.py

# Frontend Setup (di terminal baru)
cd frontend
npm install
cp .env.example .env
# Edit .env dengan API_URL backend
npm run dev
```

**Akses:**
- Frontend: `http://localhost:5173`
- Backend API: `http://localhost:5000`
- API Docs: `http://localhost:5000/api/docs`

### Deploy ke Production

Lihat: [SETUP_GUIDE.md](./SETUP_GUIDE.md) untuk detail lengkap

- **Database**: Supabase PostgreSQL
- **Backend**: Heroku / AWS EC2 / Railway
- **Frontend**: GitHub Pages / Vercel / Netlify

## 📚 Dokumentasi

| File | Isi |
|------|-----|
| [SETUP_GUIDE.md](./SETUP_GUIDE.md) | Setup & deployment lengkap |
| [docs/PANDUAN_PENGGUNA.md](./docs/PANDUAN_PENGGUAN.md) | User guide untuk 5 seksi |
| [docs/PANDUAN_ADMIN.md](./docs/PANDUAN_ADMIN.md) | Admin panel guide |
| [docs/API_DOCS.md](./docs/API_DOCS.md) | API reference |
| [docs/FAQ.md](./docs/FAQ.md) | Q&A & troubleshooting |

## 🔐 Security

- ✅ JWT Authentication (24 jam token)
- ✅ Password Hashing (bcrypt)
- ✅ HTTPS/SSL Required
- ✅ CORS Protection
- ✅ SQL Injection Prevention (SQLAlchemy ORM)
- ✅ XSS Protection
- ✅ Rate Limiting
- ✅ Audit Logging (semua action tercatat)
- ✅ Role-Based Access Control (RBAC)
- ✅ File Upload Validation

## 💾 Data Storage

```
📊 Database (PostgreSQL Supabase):
   └─ risk_assessments (Q1-Q4 data 26 indikator)
   └─ risk_change_logs (audit trail perubahan)
   └─ supporting_documents (bukti pendukung - file)
   └─ audit_logs (semua action pengguna)

📁 File Storage (Cloud):
   └─ /bukti_pendukung/2024/Q1/MSKI/...
   └─ /bukti_pendukung/2024/Q2/Bank/...
   └─ /laporan/Q1_2024.xlsx
   └─ /backup/risiko_2024_backup.sql
```

Semua dokumen tersimpan terstruktur per tahun, quarter, dan seksi.

## 📞 Support & Contact

**Untuk pertanyaan/masalah teknis:**
- Email: support@kppn.local
- WhatsApp: [nomor admin]
- Jam kerja: Senin-Jumat, 08:00-16:00 WIB

## 📈 Roadmap

- ✅ v1.0: Core system (input, tracking, matrix)
- 🔄 v1.1: Analytics & advanced reports (Q3 2024)
- 📅 v1.2: Scheduling & notifications (Q4 2024)
- 🤖 v2.0: AI-powered risk prediction (2025)

## 📜 License

Internal Use Only - KPPN  
All rights reserved © 2024

---

**Dibuat untuk**: KPPN Manajemen Risiko  
**Versi**: 1.0  
**Tanggal**: 8 Juni 2026  
**Status**: 🟢 Production Ready
