# 📖 Panduan Pengguna - Sistem Manajemen Risiko KPPN

## Daftar Isi
1. [Login](#login)
2. [Dashboard](#dashboard)
3. [Input Data Risiko](#input-data-risiko)
4. [Tracking Perubahan Risiko](#tracking-perubahan-risiko)
5. [Lihat Data Lengkap](#lihat-data-lengkap)
6. [FAQ](#faq)

## Login

1. Buka: https://app.kppn.local/
2. Masukkan username dan password
3. Klik "Login"
4. Akan diarahkan ke Dashboard

**Lupa Password?**
- Klik "Lupa Password"
- Masukkan email
- Cek email untuk reset link

## Dashboard

### Tampilan Utama
- **Status Pengisian**: Indikator progress Q1-Q4
- **Ringkasan Risiko**: Chart risiko per kategori warna
- **Data Terbaru**: Perubahan risiko terbaru
- **Quick Actions**: Tombol untuk input data, lihat laporan

### Menu Utama
- **Input Data**: Isi risiko untuk quarter yang sedang berjalan
- **Lihat Data**: Lihat semua data risiko yang sudah diinput
- **Analisis**: Lihat perubahan risiko quarter ke quarter
- **Laporan**: Download laporan lengkap
- **Setting**: Edit profil dan preferensi

## Input Data Risiko

### Step 1: Buka Form Input
```
Menu Utama > Input Data > Pilih Quarter
```

**Catatan**: Form hanya bisa dibuka pada bulan yang ditentukan:
- Q1: Maret
- Q2: Juni
- Q3: September
- Q4: Desember

### Step 2: Isi Data untuk 26 Indikator

Untuk setiap indikator, isi:

#### **A. Frekuensi Kejadian (Skala 1-5)**
```
1 = Jarang (< 1x setahun)
2 = Jarang (1-3x setahun)
3 = Sedang (4-6x setahun)
4 = Sering (7-12x setahun)
5 = Sangat Sering (> 12x setahun)

Klik tombol atau ketik angka 1-5
```

#### **B. Dampak/Besaran Risiko (Skala 1-5)**
```
1 = Minimal (Kerugian < Rp 10 juta)
2 = Rendah (Kerugian Rp 10-100 juta)
3 = Sedang (Kerugian Rp 100 juta - 1 miliar)
4 = Tinggi (Kerugian Rp 1-10 miliar)
5 = Sangat Tinggi (Kerugian > Rp 10 miliar)

Klik tombol atau ketik angka 1-5
```

#### **C. Sistem Auto-Calculate**
Sistem otomatis menghitung:
```
Nilai Risiko = Frekuensi × Dampak

Contoh:
Frekuensi 3 × Dampak 4 = Risiko 12 (Kategori KUNING)
```

#### **D. Matriks Risiko Visual**
Sistem menampilkan matriks 5×5 untuk visualisasi:
```
🟦 BIRU (1-3):      Risiko Rendah
🟩 HIJAU (5-8):     Risiko Sedang Rendah
🟨 KUNING (10-14):  Risiko Sedang
🟧 JINGGA (16-20):  Risiko Tinggi
🟥 MERAH (21-25):   Risiko Sangat Tinggi
```

### Step 3: Isi Alasan Perubahan (Jika bukan Q1)

Jika nilai risiko berubah dari quarter sebelumnya, wajib isi:
```
"Alasan Perubahan Nilai Risiko"
Contoh:
- "Dilakukan edukasi intensif ke satker, sehingga error entry berkurang"
- "Implementasi sistem validasi otomatis di aplikasi"
- "Penambahan staff operasional"
```

### Step 4: Upload Bukti Pendukung

Upload dokumen pendukung perubahan risiko:
```
File yang diizinkan:
- PDF, DOC, DOCX (laporan, memo)
- XLS, XLSX (data, hasil audit)
- PNG, JPG (screenshot dashboard, bukti aktivitas)
- ZIP (kumpulan dokumen)

Ukuran maksimal: 25 MB per file

Contoh file:
- Laporan_Edukasi_Satker.pdf
- Hasil_Audit_Quality_Control.xlsx
- Screenshot_Sistem_Validasi.png
```

### Step 5: Review Data

Sebelum submit, review semua data:
```
✓ Semua 26 indikator sudah diisi
✓ Nilai frekuensi & dampak benar
✓ Alasan perubahan jelas dan terukur
✓ Bukti pendukung sudah diupload
```

### Step 6: Kirim Final

```
Klik tombol "KIRIM FINAL"
Status berubah: Draft → Submitted
Admin akan verify dan approve
```

**Catatan Penting**:
- Data yang sudah "KIRIM FINAL" masih bisa di-edit
- Perubahan setelah submit akan dicatat di Audit Log
- Hanya admin yang bisa approve data

## Tracking Perubahan Risiko

### Lihat Perubahan Q1 → Q2 → Q3 → Q4

```
Menu > Analisis Perubahan
```

### Tampilan:
```
┌─────────────────────────────────────────────┐
│ Analisis Perubahan Q1 → Q2                  │
├─────────────────────────────────────────────┤
│                                             │
│ Indikator: Nilai Kinerja Pelaksanaan..     │
│                                             │
│ Q1: 14 (Kuning) → Q2: 10 (Hijau) ✓ TURUN   │
│                                             │
│ [MATRIKS VISUAL]                            │
│ Tampil pergerakan dari Kuning ke Hijau     │
│                                             │
│ Alasan: "Edukasi satker dilakukan..."      │
│ Bukti: Laporan_Edukasi.pdf (2.3 MB)        │
│                                             │
│ Tracking P26 → R26:                        │
│ P26 (Initial): 14                          │
│ Q1: 14 → Q2: 10 → Q3: 8 → Q4: 10          │
│ R26 (Target): 10 ✓ TERCAPAI DI Q2         │
│                                             │
└─────────────────────────────────────────────┘
```

### P26 & R26 Penjelasan:
```
P26 (Nilai Risiko Awal):
  = Nilai risiko pada periode baseline
  = Target awal yang ingin dicapai
  
R26 (Nilai Residual Harapan):
  = Target penurunan risiko setelah mitigasi
  = Nilai yang diharapkan tercapai
  
Target: P26 → R26 (turun)
Contoh: 14 → 10 (turun 4 poin)
```

## Lihat Data Lengkap

### Tabel Data Risiko
```
Menu > Lihat Data

Tampilan:
┌─────┬──────────────┬─────┬─────┬─────┬─────┬─────┬─────┬────────┐
│ # │ Indikator    │ PIC │ Q1 │ Q2 │ Q3 │ Q4 │P26 │R26 │ Status │
├─────┼──────────────┼─────┼─────┼─────┼─────┼─────┼─────┼────────┤
│ 1 │ 1a-CP-01     │MSKI │ 14 │ 10 │ 08 │ 07 │ 14 │ 10 │ ✓ OK   │
│ 2 │ 1a-CP-02     │MSKI │ 19 │ 18 │ 17 │ 15 │ 19 │ 16 │ ✓ OK   │
│..  │ ...          │ ... │ .. │ .. │ .. │ .. │ .. │ .. │ ...    │
└─────┴──────────────┴─────┴─────┴─────┴─────┴─────┴─────┴────────┘

Warna baris sesuai kategori risiko Q4 terbaru
Klik baris untuk lihat detail & bukti pendukung
```

### Edit Data
```
Klik tombol "EDIT" pada data yang ingin diubah
Ubah nilai frekuensi/dampak
Update alasan perubahan & bukti
Klik "SIMPAN"

Catatan: Data tetap bisa di-edit hingga quarter berikutnya dimulai
```

## FAQ

### Q: Kapan saya bisa mengisi data Q2?
A: Data Q2 hanya bisa diisi pada bulan Juni. Di bulan lain, form akan tertutup.

### Q: Apakah saya bisa edit data yang sudah "KIRIM FINAL"?
A: Ya, bisa. Tombol "EDIT" akan tetap tersedia hingga quarter berikutnya.

### Q: Bagaimana jika lupa upload bukti pendukung?
A: Bukti pendukung bersifat wajib. Form tidak bisa submit jika kosong.

### Q: Berapa ukuran file maksimal yang bisa diupload?
A: Maksimal 25 MB per file. Jika lebih besar, compress terlebih dahulu.

### Q: Apa bedanya P26 dan R26?
A: P26 = nilai risiko awal, R26 = target setelah mitigasi. Tujuannya P turun ke R.

### Q: Bagaimana kalau nilai risiko malah naik di Q2?
A: Isi alasan kenapa naik (misal: bertambah aktivitas, kendala teknis, dll) dan upload buktinya.

### Q: Siapa yang bisa lihat data risiko saya?
A: Admin dan PIC seksi Anda. Data bersifat internal dan confidential.

### Q: Apakah ada laporan bulanan?
A: Laporan otomatis dibuat per quarter. Admin bisa export kapan saja.

---

**Butuh bantuan?**  
Email: support@kppn.local  
Telepon: [nomor support]  
Jam kerja: Senin-Jumat 08:00-16:00 WIB
