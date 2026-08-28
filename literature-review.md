# Literature Review — OCR Timbangan Industrial & Seven-Segment Display

> Cakupan: 2018–2026 (26 Agt 2026). Semua referensi **diverifikasi DOI/URL-nya** (lihat `references.md`).
> Fokus: pembacaan otomatis display digital (7-segment/LED), khususnya yang relevan **timbangan industrial** (bukan sekadar meter utilitas).

---

## 📊 Tabel Ringkasan (18 jurnal/paper terverifikasi)

| # | Paper | Tahun | Domain | Metode | Hasil kunci |
|---|---|---|---|---|---|
| 1 | **Li & Bai — *Symmetry*** | 2026 | Meter listrik | YOLOv10n (+RCSOSA, SimAM) + EasyOCR + semantic rules | mAP50 0.932, 116 FPS; desimal hilang = error 100× |
| 2 | **PRISMA SLR — *Array*** | 2026 | Meter air (SLR) | PRISMA review, 44 studi | 61,5% ≥95% (terkontrol) tapi hanya 4,5% field-deploy |
| 3 | **Reyes-Reyes et al. — *IEEE Access*** | 2025 | **Timbangan digital (babi)** | GroundingDINO segmen + CNN klasifikasi digit | baca berat error 20,2 g @ ±44 kg; <50 ms |
| 4 | **EDPNet — *Sensors* (MDPI)** | 2025 | Meter digital | Efficient DB (EfficientNetV2-s) + PARSeq | EPNet recognition 90,0%; light, +0,2% SOTA |
| 5 | **Low et al. — *ITM Web Conf*** | 2024 | 7-segment umum | DBNet (deteksi) + PARSeq (rekognisi) | PARSeq **56,97%** akurasi di 7Seg; gagal di glare |
| 6 | **Haseeb et al. — *VFAST*** | 2024 | Meter listrik | KNN/DT/SVM/RF/CNN | CNN sampai **98%** di meter asli |
| 7 | **Peng et al. — *Measurement*** | 2023 | Meter digital | FFT blur-detect + DeblurGAN + YOLOv5 + CRNN | missing-rate ~1%; PSNR 26,56 |
| 8 | **Imran et al. — *CMC*** | 2023 | Meter listrik (outdoor) | YOLO + Faster-RCNN | 98% (rata-rata per digit); robust variasi lapangan |
| 9 | **Lightweight single-pass — *Electr. Imaging*** | 2023 | 7-segment in-the-wild | VGG16 + digit head (sintetik) | sintetik 100% → **nyata 92%**; 97,8% single-frame |
| 10 | **Carvalho et al. — *Appl. Sci.*** | 2023 | Meter (edge) | DL untuk perangkat edge | real-time pada device terbatas |
| 11 | **Xu et al. — *J. Phys. Conf. Ser.*** | 2020 | **Timbangan elektronik (pendidikan)** | YOLOv3 + DeepLabV3+ + projection seg + SVM | akurasi tinggi; adaptif lighting/rotasi |
| 12 | **Kanagarathinam & Sekar — *Energy Reports*** | 2019 | Meter listrik | Dataset publik 7-segment (YUVA EB) | fondasi dataset tujuh-segment meter |
| 13 | **Laroca et al. — *J. EI*** | 2019 | Meter (AMR klasik) | Faster R-CNN / Fast-YOLO + CRNet/CRNN | 97,30% counter; 99,56% digit detection |
| 14 | **Elrefaei et al. — *J. Med. Eng. Tech.*** | 2019 | 7-segment medis | Retinex + MSER + HOG + NN (sintetik) | **93%** akurasi digit asli via training sintetik |
| 15 | **Wannachai et al. — *LNICST*** | 2020 | Display mesin manufaktur | CNN (camera + ISS framework) | interpretasi 91,1%; real-time |
| 16 | **Cascade R-CNN — *ECTI-CON*** | 2022 | Display mesin (industri) | Cascade R-CNN end-to-end | Precision/recall/F1 = 0,999 |
| 17 | **CNN-GO — *GTSD*** | 2022 | Instrumen industri | CNN + IoT device + overlapping scan | baca display 7-seg instrumen |
| 18 | **Zhang, Yan & Ye — *CEA*** | 2024 | Instrumen digital (mobile) | Lightweight YOLOv7 + pruning | 98,44% akurasi sistem; param −99,67%; 10,7 ms |

> ⚠️ **Catatan metodologi:** angka ≥95–98% (baris 6, 8, 12, 13) semua **dilatih & diuji pada data METEK ASLI** (2.300–12.500 gambar). Tidak ada yang mencapai itu dengan **training sintetik**. Ini justru membuktikan diagnosa PPT: *sintetik plateau, perlu data nyata*.

---

## 📖 Anotasi per Kelompok

### A. Masalah desimal & nilai eksak (paling relevan untuk berat)
- **[1] Li & Bai (2026, *Symmetry*)** — inti paper ini: **desimal yang terlewat** (123.45 → 12345) memperbesar error **100×**. Solusi: *domain-specific format rules* (standar GB/T). → Untuk timbangan, nilai berat = nilai komersial yang harus eksak; ini padanan langsung masalahmu. **Klaim orisinalmu:** semantic format *berat* (kg + titik desimal + indikator stabil) belum ada yang menangani.

### B. Bukti gap controlled→field (fondasi narasi paper)
- **[2] SLR *Array* 2026** — "the gap is not algorithmic but structural". 61,5% ≥95% hanya di kondisi terkontrol, 4,5% sampai deployment. → Persis keadaan PPT: akurasi tes/pipeline bagus, tapi lapangan tidak.
- **[9] Lightweight 2023** — training sintetik: digit 100% (train) → 92% (nyata). Bukti empiris langsung **sim-to-real drop**. → basis klaim "sintetik tidak cukup".

### C. Domain-analog terdekat: baca timbangan digital
- **[3] Reyes-Reyes et al. (2025, *IEEE Access*)** — membaca **nilai berat dari layar timbangan digital** (peternakan babi): GroundingDINO segmentasi → CNN klasifikasi digit → susun nilai. Error 20,2 g @ 44 kg. **Ini domain-analog terbukti paling dekat** dengan proyekmu, tapi: *tidak menangani desimal eksak, tanpa constraint audit/offline, bukan timbangan industrial logistik.*
- **[11] Xu et al. (2020)** — timbangan elektronik untuk ujian kimia: YOLOv3 + DeepLabV3+ + SVM. Membuktikan OTK/segmentasi popular untuk timbangan, tapi metode lama (pra-CNN-CTC).

### D. SOTA meter digital (arahan metode)
- **[4] EDPNet (2025)** — text-detection (DB) + PARSeq itu kombinasi SOTA saat ini; light (EfficientNetV2-s).
- **[5] Low (2024), [7] Peng (2023), [8] Imran (2023)** — konfirmasi Tesseract/OCR generik gagal pada 7-segment; deep CNN + post-processing diperlukan. PARSeq hanya 56,97% di 7Seg.
- **[10] Carvalho (2023)** — dekat dengan constraint **edge/offline** proyekmu.

### E. Fondasi dataset & metode klasik
- **[12] Kanagarathinam & Sekar (2019)** — dataset *YUVA EB* (7-segment energy meter) yang dipakai banyak paper; benchmark umum.
- **[13] Laroca (2019)** — *automatic meter reading* klasik (CNN), rujukan baseline.
- **[14] Elrefaei (2019)** — membuktikan **training sintetik bisa** mencapai 93% akurasi digit riil *jika* data sintetik merepresentasikan kondisi nyata → argumen "reconquer synthetic data ataupun butuh data nyata".

### F. Industri/manufaktur (pendekatan paling dekat ke "display instrumen di lapangan")
- **[15] Wannachai (2020)** — CNN baca display 7-seg **mesin manufaktur** via kamera, 91,1% — konteks industri nyata (vibrasi, refleksi, perubahan frame).
- **[16] Cascade R-CNN (2022)** — end-to-end 7-seg pada mesin industri, F1=0,999.
- **[17] CNN-GO (2022)** — sistem embedded/IoT baca instrumen industri dari foto.
- **[18] Zhang et al. (2024)** — YOLOv7 ringan utk instrumen digital **di mobile**, 98,44%, 10,7 ms — dekat dengan kendala edge/on-device proyekmu.

> **Jujur soal "OCR khusus timbangan":** ada beberapa paper baca layar *timbangan*, tapi **konteks non-transaksi** — Reyes-Reyes (IEEE Access 2025, timbangan peternakan), Xu et al. (2020, timbangan ujian kimia), visual-weighing dump truck. **Tidak ada** paper peer-review untuk **timbangan industri/logistik transaksi komersial** dengan kendala `desimal-eksak + no-manual-input/audit + offline/edge + confidence-gate ≥95%` → ini gap & klaim orisinalmu.

---

## ➡️ Implikasi untuk judul & paper-mu
1. **Kosong di timbangan industrial** → wilayah klaim orisinal (domain & constraint), bukan sekadar "re-metode".
2. **Desimal/format-berat belum diselesaikan** untuk timbangan → komponen kebaruan (3 baris paper seperti *Symmetry* 2026 baru mulai di meter).
3. **Sim-to-real gap** adalah masalah lintas-domain yang belum terpecahkan untuk timbangan → arahkan *hybrid cloud-bootstrap* sebagai kontribusi.
4. **Constraint sistem** (no manual input, offline, confidence-gate 95%) nyaris tak dibahas di paper → angkat sebagai pembeda.
