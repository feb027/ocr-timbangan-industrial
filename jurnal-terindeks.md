# Jurnal Terindeks — Referensi Pengganti + Target Submit

> Dibuat: 18 September 2026 · untuk paper OCR timbangan industrial (hybrid edge–cloud).
> **Semua DOI di file ini sudah dicek langsung ke Crossref API** (judul, jurnal, tahun, penulis cocok).
> Cara cek ulang kapan saja: `python3 scripts/verify_refs.py`
>
> **Masalah dengan daftar lama (`references.md`):** 8 dari 18 entri bukan artikel jurnal —
> itu prosiding konferensi/book series, plus 1 DOI salah-tunjuk dan 1 daftar penulis salah.
> Rinciannya di bagian **C**.

---

## A. Referensi pengganti (28 jurnal, semua terverifikasi)

Urutan sudah dipetakan ke gap/RQ di `gap-analysis.md`. Semua di jurnal, bukan prosiding.

### A1. Inti — desimal / nilai eksak (Gap 2)

2. Huang, J.; Chen, Y.; Tsai, Y. (2024). Utilizing Cross-Ratios for the Detection and Correction of Missing Digits in Instrument Digit Recognition. *Mathematics*, 12(11), 1669. https://doi.org/10.3390/math12111669
   → **Yang paling dekat dengan kebaruanmu:** secara formal mengoreksi digit yang hilang pada pembacaan instrumen. Pakai ini sebagai *anchor* klaim "koreksi semantik".
4. Li, Y.; Bai, Y. (2026). Recognition of Electricity Meter Digits Based on Improved YOLOv10n and Cascaded Visual-Semantic Processing. *Symmetry*, 18(4), 694. https://doi.org/10.3390/sym18040694
   → Desimal hilang = error 100×, diselesaikan lewat *format rules*. Sudah ada di daftar lama, tetap dipakai.
13. Wang, Z.; Tian, L.; Du, Q.; An, Y.; Sun, Z.; Liao, W. (2023). Scale value guided Lite-FCOS for pointer meter reading recognition. *Measurement Science and Technology*, 34(12), 125405. https://doi.org/10.1088/1361-6501/acf23a
   → Nilai skala dipakai sebagai *prior* semantik saat membaca instrumen.
14. Peng, X.; Chen, Y.; Cai, X.; Liu, J. (2024). An Improved YOLOv7-Based Model for Real-Time Meter Reading with PConv and Attention Mechanisms. *Sensors*, 24(11), 3549. https://doi.org/10.3390/s24113549

### A2. Domain — pembacaan display / instrumen (Gap 1)

1. Xiang, X.; Zhu, C.; Ou, Z.; Zhang, Q.; Zheng, S.; Chen, Z. (2026). Semi-Supervised Seven-Segment LED Display Recognition with an Integrated Data-Acquisition Framework. *Sensors*, 26(1), 265. https://doi.org/10.3390/s26010265
   → Paling baru (2026) & paling dekat: 7-segment LED + kerangka akuisisi data.
3. Kanagarathinam, K.; Sekar, K. (2019). Text detection and recognition in raw image dataset of seven segment digital energy meter display. *Energy Reports*, 5, 842–852. https://doi.org/10.1016/j.egyr.2019.07.004
   → Dataset publik *YUVA-EB*. **DOI di `references.md` salah** — diganti ke DOI yang benar ini.
6. Reyes-Reyes, N. A.; Catalin Doja, M.; Llagostera-Blasco, P.; Plà-Aragonès, L. M.; González-Araya, M. C. (2025). A Deep Learning Approach for Image Analysis and Reading Body Weight From Digital Scales in Pigs Farms. *IEEE Access*, 13, 39353–39363. https://doi.org/10.1109/access.2025.3543027
   → Domain-analog terdekat (baca **berat** dari layar timbangan). Sudah ada di daftar lama.
7. Li, D.; Hou, J.; Gao, W. (2022). Instrument reading recognition by deep learning of capsules network model for digitalization in Industrial Internet of Things. *Engineering Reports*, 4(12), e12547. https://doi.org/10.1002/eng2.12547
8. Fan, Z.; Shi, L.; Xi, C.; Wang, H.; Wang, S.; Wu, G. (2022). Real Time Power Equipment Meter Recognition Based on Deep Learning. *IEEE Transactions on Instrumentation and Measurement*, 71, 1–15. https://doi.org/10.1109/tim.2022.3191709
   → **IEEE TIM = jurnal instrumen & pengukuran #1** (SJR Q1) — sitasi ini menaikkan kelas daftar pustakamu.
9. Zhao, S.; Lu, Q.; Zhang, C.; Ahn, C. K.; Chen, K. (2024). Effective Recognition of Word-Wheel Water Meter Readings for Smart Urban Infrastructure. *IEEE Internet of Things Journal*, 11(10), 17283–17291. https://doi.org/10.1109/jiot.2024.3357839
10. Meškuotienė, A.; Kaškonas, P.; Urbonavičius, B. G.; Dobilienė, J.; Raudienė, E. (2025). Ensuring Measurement Integrity in Petroleum Logistics: Applying Standardized Methods, Protocols, and Corrections. *Applied Sciences*, 15(12), 6886. https://doi.org/10.3390/app15126886
    → Konteks **integritas pengukuran & transaksi komersial di rantai pasok** — pembenaran mengapa nilai berat harus eksak.
11. Jeon, S.; Ko, B. S.; Son, S. H. (2023). ROMI: A Real-Time Optical Digit Recognition Embedded System for Monitoring Patients in Intensive Care Units. *Sensors*, 23(2), 638. https://doi.org/10.3390/s23020638
12. Lobo, P.; Vilaça, J. L.; Torres, H.; Oliveira, B.; Simões, A. (2023). Smart scan of medical device displays to integrate with a mHealth application. *Heliyon*, 9(6), e16297. https://doi.org/10.1016/j.heliyon.2023.e16297
15. Li, X.; Zhao, J.; Zeng, C.; Yao, Y.; Zhang, S.; Yang, S. (2025). Deep Learning-Based Pointer Meter Reading Recognition for Advancing Manufacturing Digital Transformation Research. *Sensors*, 25(1), 244. https://doi.org/10.3390/s25010244
16. Fan, H.; Li, Y. (2024). Image Recognition and Reading of Single Pointer Meter Based on Deep Learning. *IEEE Sensors Journal*, 24(15), 25163–25174. https://doi.org/10.1109/jsen.2024.3416436
17. Liang, Y.; Liao, Y.; Li, S.; Wu, W.; Qiu, T.; Zhang, W. (2022). Research on water meter reading recognition based on deep learning. *Scientific Reports*, 12(1), 12861. https://doi.org/10.1038/s41598-022-17255-3

### A3. Sim-to-real / data sintetik (Gap 3 — klaim kebaruan kedua)

5. Chakir, Y.; Aaroud, A. (2026). The autonomy–accuracy–universality trilemma in camera-based water meter reading: A PRISMA systematic review and taxonomy. *Array*, 30, 100960. https://doi.org/10.1016/j.array.2026.100960
   → 61,5% capai ≥95% di kondisi terkontrol, hanya 4,5% sampai *deployment* lapangan. Sudah ada di daftar lama (penulis dilengkapi).
18. Schraml, D.; Notni, G. (2024). Synthetic Training Data in AI-Driven Quality Inspection: The Significance of Camera, Lighting, and Noise Parameters. *Sensors*, 24(2), 649. https://doi.org/10.3390/s24020649
19. Dalmasso, G.; Reineri, P.; Noel, M. P.; Achard, N.; Caseau, B.; Likforman Sulem, L.; Cavagnino, D.; Lucenteforte, M.; Fiandrotti, A.; Eyharabide, V. (2026). Reviving medieval byzantine seals: a synthetic-to-real approach to character recognition. *International Journal on Document Analysis and Recognition (IJDAR)*. https://doi.org/10.1007/s10032-026-00579-5
    → IJDAR = jurnal khusus *document analysis/recognition* (SCOPUS + SCIE).
20. Zhang, J.; Liu, X.; Xue, Z.; Luo, X.; Xu, X. (2025). MAGIC: Multi-granularity domain adaptation for text recognition. *Pattern Recognition*, 161, 111229. https://doi.org/10.1016/j.patcog.2024.111229
21. Mumuni, A.; Mumuni, F.; Gerrar, N. K. (2024). A Survey of Synthetic Data Augmentation Methods in Machine Vision. *Machine Intelligence Research*, 21(5), 831–869. https://doi.org/10.1007/s11633-022-1411-7
22. Alzubaidi, L.; Bai, J.; Al-Sabaawi, A.; Santamaría, J.; Albahri, A. S.; Al-dabbagh, B. S. N.; Fadhel, M. A.; Manoufali, M.; Zhang, J.; Al-Timemy, A. H.; Duan, Y.; Abdullah, A.; Farhan, L.; Lu, Y.; Gupta, A.; Albu, F.; Abbosh, A.; Gu, Y. (2023). A survey on deep learning tools dealing with data scarcity: definitions, challenges, solutions, tips, and applications. *Journal of Big Data*, 10(1), 46. https://doi.org/10.1186/s40537-023-00727-2

### A4. Constraint sistem: confidence-gate, audit, edge (Gap 4)

23. Hendrickx, K.; Perini, L.; Van der Plas, D.; Meert, W.; Davis, J. (2024). Machine learning with a reject option: a survey. *Machine Learning*, 113(5), 3073–3110. https://doi.org/10.1007/s10994-024-06534-x
    → **Justifikasi ilmiah confidence-gate + no-manual-input.** Ini yang membuat constraint-mu terdengar seperti keputusan engineering, bukan batasan proyek.
24. Silva Filho, T.; Song, H.; Perello-Nieto, M.; Santos-Rodriguez, R.; Kull, M.; Flach, P. (2023). Classifier calibration: a survey on how to assess and improve predicted class probabilities. *Machine Learning*, 112(9), 3211–3260. https://doi.org/10.1007/s10994-023-06336-7
    → Dasar ilmiah untuk membahas kalibrasi confidence (kenapa 76% confident bisa salah).
25. Gawlikowski, J.; Tassi, C. R. N.; Ali, M.; Lee, J.; Humt, M.; Feng, J.; Kruspe, A.; Triebel, R.; Jung, P.; Roscher, R.; Shahzad, M.; Yang, W.; Bamler, R.; Zhu, X. X. (2023). A survey of uncertainty in deep neural networks. *Artificial Intelligence Review*, 56(S1), 1513–1589. https://doi.org/10.1007/s10462-023-10562-9
26. Cordova-Cardenas, R.; Amor, D.; Gutiérrez, Á. (2025). Edge AI in Practice: A Survey and Deployment Framework for Neural Networks on Embedded Systems. *Electronics*, 14(24), 4877. https://doi.org/10.3390/electronics14244877
27. Carvalho, R.; Melo, J.; Graça, R.; Santos, G.; Vasconcelos, M. J. M. (2023). Deep Learning-Powered System for Real-Time Digital Meter Reading on Edge Devices. *Applied Sciences*, 13(4), 2315. https://doi.org/10.3390/app13042315
    → Sudah ada di daftar lama, tetap dipakai (paling dekat ke constraint edge/offline).

### A5. Konteks lokal (enak dibaca & familiar di Indonesia)

28. Ircham Aji Nugroho; Susanti, B. H.; Mareta Wahyu Ardyani; Nadia Paramita R.A. (2024). The Design of a C1 Document Data Extraction Application Using a Tesseract-Optical Character Recognition Engine. *Jurnal RESTI (Rekayasa Sistem dan Teknologi Informasi)*, 8(1), 42–53. https://doi.org/10.29207/resti.v8i1.5151
    → Penerbit IAII, jurnal Indonesia terakreditasi — sitasi "Tesseract" yang tidak asing.

---

## B. Kandidat target submit (biar tidak salah kirim)

Kolom **Bukti** = yang benar-benar saya buka & baca hari ini. Yang tidak ada buktinya saya tandai
apa adanya; verifikasi sendiri di SJR (scimagojr.com) atau Clarivate MJL sebelum submit.

### B1. Internasional (semua terindeks Scopus/WoS)

| Jurnal | Penerbit | Indeks & kuartil | Biaya | Waktu | Cocok untuk |
|---|---|---|---|---|---|
| **IEEE Transactions on Instrumentation and Measurement** | IEEE | Scopus **Q1** SJR; JIF 5,9 **Q1** (2024), coverage 1963–2026 | gratis (hybrid, bayar hanya kalau pilih OA) | review ketat | **Paling pas secara bidang** (instrumen + pengukuran + pembacaan display). Bukti: ringkasan metrik publik [iit.comillas.edu](https://www.iit.comillas.edu/publicacion/info_revista/en/29/IEEE_Transactions_on_Instrumentation_and_Measurement), [researchjournalrank](https://researchjournalrank.com/journal/ieee-transactions-on-instrumentation-and-measurement) |
| **IEEE Access** | IEEE | Scopus CiteScore **9,3** (2025), SJR **Q1** | ~USD 2.000 (OA wajib) | cepat | Sistem + pipeline + evaluasi lapangan. Bukti resmi: [ieeeaccess.ieee.org/about/bibliometrics](https://ieeeaccess.ieee.org/about/bibliometrics/) |
| **Sensors** | MDPI | Scopus + SCIE (halaman indexing resmi) | APC (OA) | cepat (~2 minggu first decision) | 7-segment/edge/instrumen. Bukti: [mdpi.com/journal/sensors/indexing](https://www.mdpi.com/journal/sensors/indexing) |
| **Applied Sciences** | MDPI | JCR + SCImago (halaman indexing resmi) | APC (OA) | cepat | Aplikasi industri/logistik. Bukti: [mdpi.com/journal/applsci/indexing](https://www.mdpi.com/journal/applsci/indexing) |
| **Expert Systems with Applications** | Elsevier | CiteScore **15,0**, IF **7,5** | gratis (subscription) / USD 3.490 kalau OA | 5 hari first decision; **147 hari** sampai accepted | Kalau mau nge-push "sistem cerdas" + koreksi semantik. Bukti: [sciencedirect.com/journal/expert-systems-with-applications](https://www.sciencedirect.com/journal/expert-systems-with-applications) |
| **IJDAR** (Int. J. on Document Analysis and Recognition) | Springer | **SCOPUS + SCIE**; IF 1,7 | gratis (hybrid) | **7 hari** first decision | Venue paling *on-topic* untuk OCR/koreksi digit. Bukti: [link.springer.com/journal/10032](https://link.springer.com/journal/10032) |
| **Multimedia Tools and Applications** | Springer | **SCOPUS** + EI Compendex + SCImago | gratis (hybrid) | 34 hari first decision | Sistem multimedia + aplikasi mobile. Bukti: [link.springer.com/journal/11042](https://link.springer.com/journal/11042) |

Catatan jujur: halaman Scimago langsung diblokir Cloudflare dari sesi ini, jadi kuartil IEEE saya
ambil dari ringkasan metrik pihak ketiga + halaman resmi IEEE. Angka SJR/JIF MDPI dari halaman
indexing resmi masing-masing jurnal.

### B2. Nasional (Sinta 1–2) — kalau ingin jalur cepat & familiar

`sinta.kemdikbud.go.id` tidak bisa diakses dari sesi ini, jadi **grade Sinta di bawah belum saya
verifikasi** — cek sendiri di SINTA sebelum submit. Kandidat yang bidangnya cocok:

- **Jurnal RESTI** (IAII) — rekayasa sistem & TI, sudah memuat paper OCR Tesseract
- **IJCCS** (Indonesian Journal of Computing and Cybernetics Systems, UGM) — sistem cerdas
- **JEPIN** (Jurnal Edukasi dan Penelitian Informatika)
- **Jurnal Teknologi dan Sistem Komputer** (UNDIP) / **JITEKI**
- **Buletin Ilmiah Sarjana Teknik Elektro** (UAD) — instrumen & elektronika

Saran taktis: kalau targetnya sidang cepat, **IJDAR/IEEE Access (cepat, terindeks)** atau
**Jurnal RESTI (nasional)** lebih realistis daripada ESWA/IEEE TIM (bar review tinggi).

---

## C. Yang dibuang dari `references.md` dan alasannya

Kategori 1 — **bukan artikel jurnal** (prosiding konferensi / book series). Untuk klaim
"≥10 jurnal terindeks" ini yang bikin daftar terlihat lemah:

| Lama # | Venue | Status sebenarnya |
|---|---|---|
| 5 | ITM Web of Conferences | prosiding konferensi (EDP Sciences) → ganti **A2.1** |
| 9 | Electronic Imaging | prosiding simposium IS&T → ganti **A2.11** |
| 11 | Journal of Physics: Conference Series | prosiding (IOP) → ganti **A2.7** |
| 15 | LNICST (Springer) | book series konferensi → ganti **A2.6** |
| 16 | ECTI-CON 2022 | konferensi → ganti **A2.16** |
| 17 | GTSD 2022 | konferensi → ganti **A2.9** |

Kategori 2 — **jurnal tapi tidak terindeks internasional**:

| Lama # | Venue | Masalah |
|---|---|---|
| 6 | VFAST Transactions on Software Engineering | jurnal nasional Pakistan (HEC), bukan Scopus/WoS → ganti **A2.3** |
| 18 | Computer Engineering and Applications (CEA) | jurnal China, tanpa DOI, tidak di Scopus/WoS → ganti **A2.13** |

Kategori 3 — **kesalahan data (bahaya kalau lolos ke submission)**:

| Lama # | Masalah | Perbaikan |
|---|---|---|
| 12 | DOI `10.1016/j.egyr.2019.06.016` **menunjuk ke paper lain** (manajemen termal baterai EV), bukan paper dataset 7-segment | DOI benar: **`10.1016/j.egyr.2019.07.004`** |
| 14 | Ditulis "Elrefaei, L. A." — penulis pertama paper *J. Med. Eng. Technol.* tersebut sebenarnya **Finnegan, E.** | perbaiki nama penulis |
| 2 | Penulis SLR *Array* belum terisi | **Chakir, Y.; Aaroud, A.** |
| 4 | Penulis EDPNet *Sensors* belum lengkap | **Guan, S. dkk.** |

Kategori 4 — **dipertahankan** (jurnal + DOI benar, tetap layak): #1 Symmetry, #2 Array,
#3 IEEE Access, #4 Sensors (EDPNet), #7 Measurement, #8 CMC, #10 Applied Sciences,
#13 Journal of Electronic Imaging, #14 J. Med. Eng. & Technology (nama penulis diperbaiki),
#12 Energy Reports (DOI diperbaiki). Status indeks CMC & J. Electronic Imaging belum saya tarik
bukti resminya di sesi ini — cek SJR kalau mau diklaim eksplisit di paper.

---

## D. Verifikasi

```bash
python3 scripts/verify_refs.py        # cek semua DOI di file ini ke Crossref
```

Terakhir dijalankan 18 Sep 2026: **28/28 DOI valid**, judul + jurnal + tahun cocok dengan apa yang
tertulis di atas. Kalau kamu menambah referensi baru, masukkan lewat format yang sama
(`N. Penulis ... https://doi.org/...` di akhir baris) supaya script tetap bisa memeriksanya.
