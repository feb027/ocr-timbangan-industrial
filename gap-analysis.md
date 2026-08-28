# Analisis Gap Riset

> Berasal dari literature review (14 paper, `literature-review.md`). Gap ini membenarkan **judul** yang dirumuskan.

---

## 🧩 Gap 1 — OCR khusus *timbangan industrial transaksi komersial* kosong
- Ada riset baca layar timbangan tapi **konteks non-transaksi**: Reyes-Reyes (IEEE Access 2025, timbangan peternakan), Xu et al. (2020, timbangan elektronik ujian), visual-weighing dump truck (ResNet, ~60%).
- Mayoritas literatur OCR 7-segment: **meter utilitas** (listrik/air/gas) & **alat medis**.
- Literatur IoT "jembatan timbang" Indonesia baca berat dari **loadcell (hardware)**, BUKAN dari **foto layar** — jadi tidak tumpang tindih dengan pendekatan kamera/OCR.
- Solusi timbangan industrial yang ada bersifat **komersial tertutup** (A.N.LAB 7-SeG OCR, MFCVISION/Gemini, aplikasi internal) — bukan metode terpublikasi yang bisa direplikasi.
- → **Kosong spesifik**: timbangan industri/logistik untuk *transaksi komersial* dengan kendala `desimal eksak (nilai berat = uang) + no-manual-input (audit) + offline/edge + confidence-gate ≥95%`. Paper terdekat (Reyes-Reyes) tanpa desimal eksak & tanpa kendala sistem.

## 🧩 Gap 2 — *Semantic format-berat* (desimal, kg, indikator stabil, tare) belum ditangani
- **Li & Bai (*Symmetry* 2026)** baru mulai: desimal hilang = error 100×, pakai *format rules* (standar GB/T meter).
- **Belum ada** yang memformalkan **konteks timbangan**: angka berat itu *nilai komersial* (transaksi jual-beli), ada indikator stabil ("L"), satuan kg, titik desimal yang bisa bergeser sesuai kapasitas timbangan.
- → Komponen kebaruan: **koreksi semantik format-berat** sebagai post-processing berdomain.

## 🧩 Gap 3 — *Sim-to-real gap* untuk timbangan belum terpecahkan
- **Lightweight 2023**: sintetik 100% → nyata 92%. **SLR *Array* 2026**: controlled-fit ≠ field-fit (4,5% deploy).
- PPT-mu menemukan plateau yang sama (sintetik ~50–60%).
- **Belum ada** paper yang mengusulkan + mengevaluasi *pipeline* khusus untuk menutup ini pada **timbangan** (mis. hybrid cloud-bootstrap → local CNN, sesuai rekomendasi PPT).

## 🧩 Gap 4 — Constraint *sistem-level* diabaikan
- Mayoritas paper melaporkan **hanya metrik akurasi model**, bukan pipeline yang
  `no-manual-input (audit integrity) + offline/edge + confidence-gate ≥95% + bukti foto`.
- → Pembeda kuat: muatan sistem (audit trail, offline, confidence gating) yang nyaris tak dijamah riset.

---

## 🎯 Rumusan tujuan / obyek / metode paper

| Komponen | Isi |
|---|---|
| **Metode** | OCR deep learning (CNN/CRNN-CTC) + **koreksi semantik format-berat** + strategi **hybrid cloud-bootstrap → local CNN** |
| **Tujuan** | Mencapai pembacaan nilai berat ≥95% akurasi pada kondisi lapangan (nyata), dan **menutup kesenjangan data sintetis→nyata** |
| **Obyek** | Display timbangan industrial 7-segment/LED, konteks operasional logistik (operator, offline, audit) |

---

## 📌 Research Questions (RQ) yang bisa dijawab paper
- **RQ1:** Seberapa besar penurunan akurasi saat model dilatih data sintetik diuji pada display timbangan nyata?
- **RQ2:** Apakah koreksi semantik format-berat (desimal/kgg/indikator-stabil/tare) memperbaiki akurasi nilai akhir vs model raw?
- **RQ3:** Apakah strategi hybrid (cloud-bootstrap → local CNN) mampu menutup sim-to-real gap menuju ≥95% di lapangan?
- **RQ4:** Bagaimana confidence-gate + no-manual-input menjaga integritas audit pada operasi nyata?
