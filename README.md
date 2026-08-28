# Artikel PI — OCR Timbangan Industrial
### Riset Judul + Literature Review (≥10 jurnal) + Analisis Gap + Fact-Check

> **Tugas Matakuliah Penulisan Ilmiah 1** — perumusan judul artikel & identitas author/afiliasi.
> Pengampu: Ir. Alam Rahmatulloh, S.T., M.T., MCE., IPM.
> Disusun: **28 Agustus 2026** — konteks studi literatur = 2018–2026 (fresh, difact-check).

---

## 🎯 Deliverable Utama: Judul Artikel (Bilingual)

**Versi Indonesia:**
> **"Pembacaan Otomatis Nilai Berat pada Timbangan Industri dengan OCR Deep Learning dan Koreksi Semantik Format Berat untuk Menutup Kesenjangan Data Sintetis–Nyata"**

**Versi Inggris:**
> **"Deep-Learning OCR with Weight-Format Semantic Correction for Automatic Reading of Industrial Scale Displays: Bridging the Synthetic-to-Real Gap"**

→ **Detail, justifikasi, judul alternatif, penulis & afiliasi di [`judul-artikel.md`](judul-artikel.md)**

---

## 📂 Isi Repo

| File | Isi |
|---|---|
| [`judul-artikel.md`](judul-artikel.md) | Judul (ID/EN) + justifikasi + penulis & afiliasi sesuai kaidah slide PI |
| [`literature-review.md`](literature-review.md) | **14 jurnal** terverifikasi, terkini (2018–2026), dianotasi |
| [`gap-analysis.md`](gap-analysis.md) | 3 gap riset + tujuan/obyek/metode paper |
| [`fact-check-ppt.md`](fact-check-ppt.md) | Verifikasi klaim PPT *Analisa Timbang* terhadap literatur |
| [`references.md`](references.md) | Daftar pustaka lengkap (APA-format) + DOI |

---

## ⚡ Ringkasan Eksekutif

- **Topik valid & gap nyata** (dengan nuansa: ada riset timbangan, tapi konteks **non-transaksi**; kosong untuk **timbangan industri/logistik transaksi komersial** + kendala audit/offline/desimal-eksak). Mayoritas literatur OCR 7-segment = meter utilitas & alat medis.
- **Anchor literatur terkini:**
  - ***Symmetry* (Apr 2026)** — masalah desimal hilang = error 100× (123.45→12345), solusi semantic rules.
  - ***Array* PRISMA SLR (2026)** — 61,5% ≥95% di kondisi terkontrol tapi hanya **4,5% sampai deployment lapangan**.
  - ***IEEE Access* (2025)** — *reading body weight from digital scales in pig farms* → domain-analog terdekat (baca timbangan digital via CNN, error 20,2 g).
  - ***ITM Web Conf* (2024)** — OCR terbaik (PARSeq) cuma **56,97%** di dataset 7Seg; gagal di glare.
- **Diagnosis PPT terverifikasi** (Tesseract 50–65%, sintetik plateau, perlu data nyata): sesuai literatur.
- **Judul akhir menangkap 2 klaim orisinal:** (1) koreksi semantik format-berat, (2) strategi bridge data sintetis→nyata.
