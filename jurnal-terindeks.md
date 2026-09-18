# Jurnal Terindeks — Referensi Pengganti + Target Submit

**Paper:** OCR Deep Learning + Koreksi Semantik Format Berat untuk Timbangan Industri
**Diperbarui:** 18 September 2026 · **Status:** 28 referensi jurnal, semua DOI diverifikasi ke Crossref API

| Bagian | Isi | Untuk apa |
|---|---|---|
| [A](#a-tabel-referensi-28-jurnal) | 28 referensi jurnal, dipetakan ke Gap 1–4 | Ganti daftar lama di `references.md` |
| [B](#b-target-submit) | Kandidat jurnal tujuan submit | Memilih venue sebelum menulis |
| [C](#c-entri-lama-yang-dibuang) | 10 entri lama yang dibuang + alasannya | Bahan revisi & jaga-jaga saat ditanya dosen |
| [D](#d-koreksi-data-entri-lama) | 4 kesalahan data pada entri lama | Perbaiki sebelum sitasi |
| [E](#e-daftar-pustaka-siap-copy-paste) | Daftar pustaka APA-7 bernomor 1–28 | Copy ke Word / Mendeley / Zotero |
| [F](#f-verifikasi) | Cara cek ulang DOI | `python3 scripts/verify_refs.py` |

> **Masalah daftar lama:** 8 dari 18 entri bukan artikel jurnal (prosiding konferensi / book series),
> 2 entri jurnal non-internasional, 1 DOI salah-tunjuk, 1 penulis salah. Rincian di [bagian C](#c-entri-lama-yang-dibuang) & [D](#d-koreksi-data-entri-lama).

---

## A. Tabel referensi (28 jurnal)

Nomor di tabel = nomor sitasi di seluruh file dan di [bagian E](#e-daftar-pustaka-siap-copy-paste).

### A1. Nilai eksak & desimal — Gap 2

| No | Penulis & tahun | Jurnal (penerbit) | Fungsi di paper |
|---|---|---|---|
| 1 | Huang dkk. (2024) | Mathematics (MDPI) | **Anchor kebaruan:** koreksi formal digit yang hilang pada pembacaan instrumen |
| 2 | Li & Bai (2026) | Symmetry (MDPI) | Desimal hilang = error 100×; solusi *format rules* |
| 3 | Wang dkk. (2023) | Measurement Science and Technology (IOP) | Nilai skala sebagai *prior* semantik saat membaca instrumen |
| 4 | Peng dkk. (2024) | Sensors (MDPI) | SOTA ringan pembacaan meter real-time |

### A2. Domain pembacaan display/instrumen — Gap 1

| No | Penulis & tahun | Jurnal (penerbit) | Fungsi di paper |
|---|---|---|---|
| 5 | Xiang dkk. (2026) | Sensors (MDPI) | Paling baru & paling dekat: 7-segment LED + kerangka akuisisi data |
| 6 | Kanagarathinam & Sekar (2019) | Energy Reports (Elsevier) | Dataset publik YUVA-EB — **DOI lama salah, lihat bagian D** |
| 7 | Reyes-Reyes dkk. (2025) | IEEE Access | **Domain-analog terdekat:** baca berat dari layar timbangan digital |
| 8 | Li dkk. (2022) | Engineering Reports (Wiley) | Baca display instrumen industri (capsule network), digitalisasi IIoT |
| 9 | Fan dkk. (2022) | IEEE Trans. on Instrumentation and Measurement | Pengenalan meter real-time di jurnal instrumen #1 (SJR Q1) |
| 10 | Zhao dkk. (2024) | IEEE Internet of Things Journal | Digit word-wheel meter air, infrastruktur urban |
| 11 | Meškuotienė dkk. (2025) | Applied Sciences (MDPI) | Integritas pengukuran & transaksi komersial di logistik |
| 12 | Jeon dkk. (2023) | Sensors (MDPI) | Digit recognition embedded real-time (ROMI) |
| 13 | Lobo dkk. (2023) | Heliyon (Elsevier) | Pipeline kamera HP → baca display alat → mHealth |
| 14 | Li dkk. (2025) | Sensors (MDPI) | Pointer meter reading untuk transformasi digital manufaktur |
| 15 | Fan & Li (2024) | IEEE Sensors Journal | Pembacaan meter pointer (instrumen, penerbit IEEE) |
| 16 | Liang dkk. (2022) | Scientific Reports (Nature) | Water meter reading berbasis deep learning |

### A3. Sim-to-real & data sintetik — Gap 3

| No | Penulis & tahun | Jurnal (penerbit) | Fungsi di paper |
|---|---|---|---|
| 17 | Chakir & Aaroud (2026) | Array (Elsevier) | 61,5% ≥95% di kondisi terkontrol, **hanya 4,5% sampai deployment** |
| 18 | Schraml & Notni (2024) | Sensors (MDPI) | Kamera/cahaya/noise menentukan kegagalan model berdata sintetik |
| 19 | Dalmasso dkk. (2026) | IJDAR (Springer) | Pendekatan sintetik→nyata untuk pengenalan karakter |
| 20 | Zhang dkk. (2025) | Pattern Recognition (Elsevier) | Domain adaptation multi-granularitas untuk text recognition |
| 21 | Mumuni dkk. (2024) | Machine Intelligence Research (Springer) | Survey augmentasi data sintetik di machine vision |
| 22 | Alzubaidi dkk. (2023) | Journal of Big Data (Springer) | Survey *data scarcity* + solusinya |

### A4. Constraint sistem: confidence-gate, audit, edge — Gap 4

| No | Penulis & tahun | Jurnal (penerbit) | Fungsi di paper |
|---|---|---|---|
| 23 | Hendrickx dkk. (2024) | Machine Learning (Springer) | **Justifikasi ilmiah** reject option/abstention = confidence-gate |
| 24 | Silva Filho dkk. (2023) | Machine Learning (Springer) | Dasar kalibrasi confidence (kenapa 76% confident bisa salah) |
| 25 | Gawlikowski dkk. (2023) | Artificial Intelligence Review (Springer) | Survey uncertainty DNN (*confidently wrong*) |
| 26 | Cordova-Cardenas dkk. (2025) | Electronics (MDPI) | Framework deployment Edge AI di perangkat embedded |
| 27 | Carvalho dkk. (2023) | Applied Sciences (MDPI) | Pembacaan meter real-time di perangkat edge |

### A5. Konteks lokal

| No | Penulis & tahun | Jurnal (penerbit) | Fungsi di paper |
|---|---|---|---|
| 28 | Nugroho dkk. (2024) | Jurnal RESTI (IAII) | Penggunaan Tesseract OCR di jurnal Indonesia — sitasi familiar |

---

## B. Target submit

Kuartil di bawah hanya yang **benar-benar saya buka buktinya**; yang belum diverifikasi ditandai eksplisit.

### B1. Internasional

| Jurnal | Penerbit | Indeks / kuartil | Biaya | Waktu | Catatan |
|---|---|---|---|---|---|
| IEEE Trans. on Instrumentation and Measurement | IEEE | Scopus **Q1**; JIF 5,9 Q1 (2024), coverage 1963–2026 | gratis (hybrid) | review ketat | **Paling pas** secara bidang. Bukti: [ringkasan metrik](https://www.iit.comillas.edu/publicacion/info_revista/en/29/IEEE_Transactions_on_Instrumentation_and_Measurement) |
| IEEE Access | IEEE | CiteScore **9,3** (2025), SJR **Q1** | ~USD 2.000 (OA wajib) | cepat | Bukti resmi: [ieeeaccess.ieee.org/about/bibliometrics](https://ieeeaccess.ieee.org/about/bibliometrics/) |
| Sensors | MDPI | Scopus + SCIE | APC (OA) | cepat | Bukti: [mdpi.com/journal/sensors/indexing](https://www.mdpi.com/journal/sensors/indexing) |
| Applied Sciences | MDPI | JCR + SCImago | APC (OA) | cepat | Bukti: [mdpi.com/journal/applsci/indexing](https://www.mdpi.com/journal/applsci/indexing) |
| Expert Systems with Applications | Elsevier | CiteScore **15,0**, IF **7,5** | gratis / USD 3.490 (OA) | 5 hari first decision, **147 hari** ke accepted | Bukti: [ScienceDirect](https://www.sciencedirect.com/journal/expert-systems-with-applications) |
| IJDAR (Document Analysis & Recognition) | Springer | **SCOPUS + SCIE**; IF 1,7 | gratis (hybrid) | **7 hari** first decision | Venue paling on-topic untuk OCR. Bukti: [Springer](https://link.springer.com/journal/10032) |
| Multimedia Tools and Applications | Springer | **SCOPUS** + EI Compendex + SCImago | gratis (hybrid) | 34 hari first decision | Bukti: [Springer](https://link.springer.com/journal/11042) |

Catatan jujur: scimagojr.com diblokir Cloudflare dari sesi ini, jadi kuartil IEEE diambil dari halaman
resmi IEEE + ringkasan metrik pihak ketiga. Verifikasi di SJR/Clarivate MJL sebelum submit.

### B2. Nasional (Sinta)

> ⚠️ `sinta.kemdikbud.go.id` tidak bisa diakses dari sesi ini, jadi **grade Sinta belum saya verifikasi** — cek sendiri sebelum submit.

| Kandidat jurnal | Bidang |
|---|---|
| Jurnal RESTI (IAII) | Rekayasa sistem & TI (sudah memuat paper OCR Tesseract) |
| IJCCS (UGM) | Sistem cerdas & komputasi |
| JEPIN | Informatika terapan |
| Jurnal Teknologi dan Sistem Komputer (UNDIP) / JITEKI | Sistem komputer & elektro |
| Buletin Ilmiah Sarjana Teknik Elektro (UAD) | Instrumen & elektronika |

**Saran:** untuk sidang cepat → **IJDAR** atau **Jurnal RESTI**. IEEE TIM & ESWA bagus tapi bar review-nya tinggi.

---

## C. Entri lama yang dibuang

Dari 18 entri di `references.md`, 10 tidak layak berdiri sebagai "jurnal terindeks".

### C1. Bukan artikel jurnal (prosiding / book series) — 6 entri

| Lama # | Venue | Status sebenarnya | Diganti nomor |
|---|---|---|---|
| 5 | ITM Web of Conferences | Prosiding konferensi (EDP Sciences) | 5 |
| 9 | Electronic Imaging | Prosiding simposium IS&T | 12 |
| 11 | Journal of Physics: Conference Series | Prosiding (IOP) | 8 |
| 15 | LNICST (Springer) | Book series konferensi | 7 |
| 16 | ECTI-CON 2022 | Konferensi | 15 |
| 17 | GTSD 2022 | Konferensi | 10 |

### C2. Jurnal tapi tidak terindeks internasional — 2 entri

| Lama # | Venue | Masalah | Diganti nomor |
|---|---|---|---|
| 6 | VFAST Transactions on Software Engineering | Jurnal nasional Pakistan (HEC), bukan Scopus/WoS | 6 |
| 18 | Computer Engineering and Applications (CEA) | Jurnal China, tanpa DOI, tidak di Scopus/WoS | 3 |

### C3. Dipertahankan (jurnal, DOI benar)

| Lama # | Jurnal | Nomor baru |
|---|---|---|
| 1 | Symmetry | 2 |
| 2 | Array | 17 |
| 3 | IEEE Access | 7 |
| 10 | Applied Sciences | 27 |
| 4 | Sensors (EDPNet) | opsional — tetap layak |
| 7 | Measurement | opsional — tetap layak |
| 8 | Computers, Materials & Continua | opsional — status indeks belum saya tarik buktinya |
| 13 | Journal of Electronic Imaging | opsional — status indeks belum saya tarik buktinya |

---

## D. Koreksi data entri lama

| Lama # | Masalah | Perbaikan |
|---|---|---|
| 12 | DOI `10.1016/j.egyr.2019.06.016` menunjuk ke paper lain (manajemen termal baterai EV) | DOI benar: **`10.1016/j.egyr.2019.07.004`** (nomor baru: 6) |
| 14 | Ditulis "Elrefaei, L. A." — penulis pertama sebenarnya **Finnegan, E.** | perbaiki nama penulis |
| 2 | Penulis SLR *Array* belum terisi | **Chakir, Y.; Aaroud, A.** |
| 4 | Penulis EDPNet *Sensors* belum lengkap | **Guan, S. dkk.** |

---

## E. Daftar pustaka siap copy-paste

Format APA-7. Satu baris = satu entri, DOI di akhir baris (agar `scripts/verify_refs.py` bisa memeriksa).

1. Huang, J.; Chen, Y.; Tsai, Y. (2024). Utilizing Cross-Ratios for the Detection and Correction of Missing Digits in Instrument Digit Recognition. *Mathematics*, 12(11), 1669. https://doi.org/10.3390/math12111669
2. Li, Y.; Bai, Y. (2026). Recognition of Electricity Meter Digits Based on Improved YOLOv10n and Cascaded Visual-Semantic Processing. *Symmetry*, 18(4), 694. https://doi.org/10.3390/sym18040694
3. Wang, Z.; Tian, L.; Du, Q.; An, Y.; Sun, Z.; Liao, W. (2023). Scale value guided Lite-FCOS for pointer meter reading recognition. *Measurement Science and Technology*, 34(12), 125405. https://doi.org/10.1088/1361-6501/acf23a
4. Peng, X.; Chen, Y.; Cai, X.; Liu, J. (2024). An Improved YOLOv7-Based Model for Real-Time Meter Reading with PConv and Attention Mechanisms. *Sensors*, 24(11), 3549. https://doi.org/10.3390/s24113549
5. Xiang, X.; Zhu, C.; Ou, Z.; Zhang, Q.; Zheng, S.; Chen, Z. (2026). Semi-Supervised Seven-Segment LED Display Recognition with an Integrated Data-Acquisition Framework. *Sensors*, 26(1), 265. https://doi.org/10.3390/s26010265
6. Kanagarathinam, K.; Sekar, K. (2019). Text detection and recognition in raw image dataset of seven segment digital energy meter display. *Energy Reports*, 5, 842-852. https://doi.org/10.1016/j.egyr.2019.07.004
7. Reyes-Reyes, N. A.; Catalin Doja, M.; Llagostera-Blasco, P.; Plà-Aragonès, L. M.; González-Araya, M. C. (2025). A Deep Learning Approach for Image Analysis and Reading Body Weight From Digital Scales in Pigs Farms. *IEEE Access*, 13, 39353-39363. https://doi.org/10.1109/access.2025.3543027
8. Li, D.; Hou, J.; Gao, W. (2022). Instrument reading recognition by deep learning of capsules network model for digitalization in Industrial Internet of Things. *Engineering Reports*, 4(12), e12547. https://doi.org/10.1002/eng2.12547
9. Fan, Z.; Shi, L.; Xi, C.; Wang, H.; Wang, S.; Wu, G. (2022). Real Time Power Equipment Meter Recognition Based on Deep Learning. *IEEE Transactions on Instrumentation and Measurement*, 71, 1-15. https://doi.org/10.1109/tim.2022.3191709
10. Zhao, S.; Lu, Q.; Zhang, C.; Ahn, C. K.; Chen, K. (2024). Effective Recognition of Word-Wheel Water Meter Readings for Smart Urban Infrastructure. *IEEE Internet of Things Journal*, 11(10), 17283-17291. https://doi.org/10.1109/jiot.2024.3357839
11. Meškuotienė, A.; Kaškonas, P.; Urbonavičius, B. G.; Dobilienė, J.; Raudienė, E. (2025). Ensuring Measurement Integrity in Petroleum Logistics: Applying Standardized Methods, Protocols, and Corrections. *Applied Sciences*, 15(12), 6886. https://doi.org/10.3390/app15126886
12. Jeon, S.; Ko, B. S.; Son, S. H. (2023). ROMI: A Real-Time Optical Digit Recognition Embedded System for Monitoring Patients in Intensive Care Units. *Sensors*, 23(2), 638. https://doi.org/10.3390/s23020638
13. Lobo, P.; Vilaça, J. L.; Torres, H.; Oliveira, B.; Simões, A. (2023). Smart scan of medical device displays to integrate with a mHealth application. *Heliyon*, 9(6), e16297. https://doi.org/10.1016/j.heliyon.2023.e16297
14. Li, X.; Zhao, J.; Zeng, C.; Yao, Y.; Zhang, S.; Yang, S. (2025). Deep Learning-Based Pointer Meter Reading Recognition for Advancing Manufacturing Digital Transformation Research. *Sensors*, 25(1), 244. https://doi.org/10.3390/s25010244
15. Fan, H.; Li, Y. (2024). Image Recognition and Reading of Single Pointer Meter Based on Deep Learning. *IEEE Sensors Journal*, 24(15), 25163-25174. https://doi.org/10.1109/jsen.2024.3416436
16. Liang, Y.; Liao, Y.; Li, S.; Wu, W.; Qiu, T.; Zhang, W. (2022). Research on water meter reading recognition based on deep learning. *Scientific Reports*, 12(1), 12861. https://doi.org/10.1038/s41598-022-17255-3
17. Chakir, Y.; Aaroud, A. (2026). The autonomy–accuracy–universality trilemma in camera-based water meter reading: A PRISMA systematic review and taxonomy. *Array*, 30, 100960. https://doi.org/10.1016/j.array.2026.100960
18. Schraml, D.; Notni, G. (2024). Synthetic Training Data in AI-Driven Quality Inspection: The Significance of Camera, Lighting, and Noise Parameters. *Sensors*, 24(2), 649. https://doi.org/10.3390/s24020649
19. Dalmasso, G.; Reineri, P.; Noel, M. P.; Achard, N.; Caseau, B.; Likforman Sulem, L.; Cavagnino, D.; Lucenteforte, M.; Fiandrotti, A.; Eyharabide, V. (2026). Reviving medieval byzantine seals: a synthetic-to-real approach to character recognition. *International Journal on Document Analysis and Recognition (IJDAR)*. https://doi.org/10.1007/s10032-026-00579-5
20. Zhang, J.; Liu, X.; Xue, Z.; Luo, X.; Xu, X. (2025). MAGIC: Multi-granularity domain adaptation for text recognition. *Pattern Recognition*, 161, 111229. https://doi.org/10.1016/j.patcog.2024.111229
21. Mumuni, A.; Mumuni, F.; Gerrar, N. K. (2024). A Survey of Synthetic Data Augmentation Methods in Machine Vision. *Machine Intelligence Research*, 21(5), 831-869. https://doi.org/10.1007/s11633-022-1411-7
22. Alzubaidi, L.; Bai, J.; Al-Sabaawi, A.; Santamaría, J.; Albahri, A. S.; Al-dabbagh, B. S. N.; Fadhel, M. A.; Manoufali, M.; Zhang, J.; Al-Timemy, A. H.; Duan, Y.; Abdullah, A.; Farhan, L.; Lu, Y.; Gupta, A.; Albu, F.; Abbosh, A.; Gu, Y. (2023). A survey on deep learning tools dealing with data scarcity: definitions, challenges, solutions, tips, and applications. *Journal of Big Data*, 10(1), 46. https://doi.org/10.1186/s40537-023-00727-2
23. Hendrickx, K.; Perini, L.; Van der Plas, D.; Meert, W.; Davis, J. (2024). Machine learning with a reject option: a survey. *Machine Learning*, 113(5), 3073-3110. https://doi.org/10.1007/s10994-024-06534-x
24. Silva Filho, T.; Song, H.; Perello-Nieto, M.; Santos-Rodriguez, R.; Kull, M.; Flach, P. (2023). Classifier calibration: a survey on how to assess and improve predicted class probabilities. *Machine Learning*, 112(9), 3211-3260. https://doi.org/10.1007/s10994-023-06336-7
25. Gawlikowski, J.; Tassi, C. R. N.; Ali, M.; Lee, J.; Humt, M.; Feng, J.; Kruspe, A.; Triebel, R.; Jung, P.; Roscher, R.; Shahzad, M.; Yang, W.; Bamler, R.; Zhu, X. X. (2023). A survey of uncertainty in deep neural networks. *Artificial Intelligence Review*, 56(S1), 1513-1589. https://doi.org/10.1007/s10462-023-10562-9
26. Cordova-Cardenas, R.; Amor, D.; Gutiérrez, Á. (2025). Edge AI in Practice: A Survey and Deployment Framework for Neural Networks on Embedded Systems. *Electronics*, 14(24), 4877. https://doi.org/10.3390/electronics14244877
27. Carvalho, R.; Melo, J.; Graça, R.; Santos, G.; Vasconcelos, M. J. M. (2023). Deep Learning-Powered System for Real-Time Digital Meter Reading on Edge Devices. *Applied Sciences*, 13(4), 2315. https://doi.org/10.3390/app13042315
28. Nugroho, I. A.; Susanti, B. H.; Ardyani, M. W.; Paramita R.A., N. (2024). The Design of a C1 Document Data Extraction Application Using a Tesseract-Optical Character Recognition Engine. *Jurnal RESTI (Rekayasa Sistem dan Teknologi Informasi)*, 8(1), 42-53. https://doi.org/10.29207/resti.v8i1.5151

---

## F. Verifikasi

```bash
python3 scripts/verify_refs.py
```

Terakhir dijalankan **18 Sep 2026: 28/28 DOI valid** (judul, jurnal, tahun, penulis cocok dengan Crossref).
Menambah referensi baru? Tulis satu baris dengan format sama seperti bagian E → script otomatis memeriksanya.
