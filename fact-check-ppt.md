# Fact-Check Klaim PPT "Analisa Timbang" terhadap Literatur

> Memverifikasi setiap klaim teknis pada slide **ANALISA TIMBANG · Mobile OCR PWA** (1 Mei 2026).
> Status: ✅ terbukti benar · ⚠️ terbukti sebagian · ❌ keliru (tidak ditemukan).

---

## Ringkasan Verdict

| Klaim PPT | Verdict | Bukti literatur |
|---|---|---|
| Tesseract (OCR generik) gagal pada 7-segment, ~50–65% | ✅ Benar | PARSeq terbaik cuma 56,97% (Low 2024, ITM WC); banyak dokumentasi Tesseract gagal (2 s/d SO) |
| Custom CNN training sintetik plateau (~50–60%) | ✅ Benar | Sintetik→nyata drop: 100%→92% (Lightweight 2023); plateau literatur pada data sintetik |
| **Tidak ada model publik yang capai 95%** pada display 7-segment industrial | ✅ Benar (dengan catatan) | Yang 97–98% justru pada data meter ASLI (Imran 2023, Haseeb 2024); tidak ada untuk sintetik & khusus timbangan |
| Butuh **data nyata** untuk tembus 95% | ✅ Benar | SLR Array 2026: controlled-accuracy ≠ field-accuracy; data asli adalah penentu (Reyes-Reyes 2025, Imran 2023) |
| Transfer learning (pretrained) buruk (catastrophic forgetting 19%) | ⚠️ Sebagian | Catastrophic forgetting = fenomena nyata; tapi Low 2024 justru menemukan transfer learning membantu pada data kecil → hasil bisa beda tergantung setup. **Klaim-agak-kuat** |
| Strategi hybrid (cloud-bootstrap → local CNN) valid | ✅ Benar | Pola domain-adaptation + generative augmentation validated (Symmetry 2026 refs [15][16]); hybrid = arah wajar |
| Confidence gate ≥95% + no-manual-input menjaga audit | ✅ Benar (konsep) | Garis besar jarang diteliti (gap #4); relevan & defensibel berdasarkan SLR |

---

## ✅ Detail yang terbukti benar

### 1. OCR generik (Tesseract) gagal pada 7-segment
- **Low et al. (2024)** — bahkan *state-of-the-art* PARSeq hanya **56,97%** akurasi di dataset 7Seg; terburuk di kondisi **glare**; desimal "bleeding" jadi pungsi salah. Ini jauh di bawah target 95% PPT.
- Banyak laporan praktisi (StackOverflow, wetr) mengonfirmasi Tesseract butuh preprocessing ekstrem & tetap rapuh.

### 2. Training sintetik plateau
- **Lightweight (2023)**: model yang dilatih sintetik → akurasi digit turun dari 100% (train) ke **92%** (nyata); itupun single-frame & bukan nilai akhir.
- **Reyes-Reyes (2025)**: berhasil justru karena adaptasi dengan data + fine-tuning.

### 3. "Data nyata > data sintetik" 
- **SLR *Array* (2026)** menegaskan: 61,5% studi capai ≥95% saat terkontrol, tapi **hanya 4,5% yang benar-benar deploy lapangan**. → Faktor penentu = kondisi-field & data-asli, bukan sekadar arsitektur.
- Paper berakurasi tinggi (98%) semuanya pakai ribuan gambar meter asli.

## ⚠️ Catatan (sedikit koreksi halus)
- **Transfer learning "19% catastrophic forgetting"** di PPT: hasil khusus setup-mu (1k sintetik). Literatur (Low 2024) menunjukkan transfer-learning bisa *membantu* pada data kecil — hasil bergantung pada backbone, ukuran data, LR. Sebaiknya kata-kata di paper tidak mengklaim "transfer learning buruk" secara umum, tapi "transfer learning dari OCR dokumen **tidak mencukupi** untuk 7-segment LED timbangan" — itu terbukti.
- Angka "500 nyata → 80–90%"; "1.000 nyata → 92–96%" adalah **estimasi**, bukan dari literatur (PPT sudah menandai sebagai estimasi). Saat memakai di paper, beri label *proyeksi* atau tunjukkan data-nya.

## ❌ Tidak ada klaim yang "keliru total"
Semua klaim substantif PPT sejalan dengan literatur. Satu-satunya perbaikan adalah **nuansa pada klaim transfer learning** & **pelabelan estimasi**.

---

## 💡 Manfaat fact-check untuk paper
- Perkuat **latar belakang** ("mengapa akurasi 95% susah") dengan data terukur (56,97% PARSeq; 4,5% field-deploy).
- Hindari klaim berlebihan di **abstract** (jangan tulis "transfer learning terbukti gagal"; tulis "OCR generik tidak cukup").
- Jadikan **sim-to-real gap** sebagai *research question* yang jelas, bukan sekadar cerita.
