# Analisis Gap Riset

> Berasal dari literature review (14 paper, `literature-review.md`). Gap ini membenarkan **judul** yang dirumuskan.

---

## 🧩 Gap 1 — OCR khusus *timbangan industrial* nyaris kosong di literatur
- Mayoritas riset OCR 7-segment: **meter utilitas** (listrik/air/gas) & **alat medis**.
- Solusi timbangan yang ada sifatnya **komersial tertutup** (A.N.LAB 7-SeG OCR, MFCVISION/Gemini, aplikasi internal), atau **aplikasi pabrikan** (RS-232/USB/Ethernet dari timbangan modern), **bukan metode yang dipublikasi & bisa direplikasi**.
- Paper akademik terdekat: **Reyes-Reyes 2025** (timbangan peternakan) — tapi konteksnya beda: tanpa desimal eksak, tanpa audit, bukan timbangan logistik/komersial industrial.

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
