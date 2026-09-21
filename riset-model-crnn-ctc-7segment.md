# Riset: Model untuk "Evaluasi CRNN-CTC Berbasis Data Sintetis untuk OCR Seven-Segment Timbangan Digital"

Riset: 21 Sep 2026. Semua DOI/sumber dicek via CrossRef, HuggingFace API, GitHub API (bukan dari ingatan).

## TL;DR

1. CRNN-CTC + data sintetis = resep STANDAR di literatur SSOCR (Seven-Segment OCR). Ada jurnal yang persis topiknya, dari Indonesia (JIIF Unpad, 2025).
2. Model 7-seg "siap pakai" SUDAH ADA, tapi terbatas: Tesseract traineddata (ssd, letsgodigital), TFLite keras-ocr, classifier digit HuggingFace. Tidak ada satu pun yang setara "YOLO-nya seven-segment" untuk kondisi lapangan.
3. Model scene-text umum (CRNN/PARSeq pretrained) TIDAK cukup tanpa fine-tune — terukur: hanya ~49-57% word accuracy di dataset 7Seg.
4. From scratch bukan keharusan dan bukan masalah: CRNN kecil (~8-9 juta parameter), data sintetis tak terbatas (font DSEG/LetsGoDigital + augmentasi). Alternatif: init dari OCR pretrained (PaddleOCR/MMOCR/keras-ocr) lalu fine-tune. Membandingkan keduanya = kontribusi yang bagus untuk judul "Evaluasi".

## Analogi dengan People Counting (YOLO)

- People counting: YOLO deteksi objek, di-fine-tune agar hanya manusia yang terdeteksi.
- 7-segment ada 2 paradigma:
  (a) Deteksi per-digit ala YOLO (tiap digit = objek, kelas 0-9) — butuh label bounding box per digit.
  (b) Sequence recognition CRNN-CTC: gambar baris display -> string "150.5" tanpa segmentasi — cukup label teks utuh. CTC menangani panjang bervariasi dan masalah klasik 7-seg (digit menempel, titik desimal "bleeding").
- Di PWA ANALISA TIMBANG, ROI sudah difix lewat bracket kamera -> tidak perlu detektor, tinggal recognizer. Jadi CRNN-CTC paling pas; detektor YOLO (jalur a) hanya perlu jika layar belum ter-crop.

## A. Literatur CRNN-CTC + data sintetis (jalur judul)

1. Effendi, Grania, Adiperdana, Faizal (2025). "Unjuk Kerja Real-time Data Logger Berbasis Model CRNN-CTC untuk Perekaman Data Display Seven Segment". Jurnal Ilmu dan Inovasi Fisika (JIIF) Unpad, Vol 9 No 2.
   - YOLOv8 (deteksi area display) + CRNN-CTC (rekognisi, 6 lapis konvolusi + BiLSTM).
   - Data: dataset open-source + foto smartphone + generator citra + augmentasi.
   - Hasil: CER 3.6%, akurasi test 90.37% (197/218 gambar).
   - DOI tidak ada (jurnal nasional); PDF: https://jurnal.unpad.ac.id/jiif/article/download/64116/pdf_1 ; index: https://garuda.kemdiktisaintek.go.id/documents/detail/5324992
2. Yenneti, Chiou, Price (2023). "Lightweight single pass numerical reading extraction for displays in the wild". IS&T Electronic Imaging 2023. DOI: 10.2352/ei.2023.35.7.image-282
   - VGG16 backbone + digit inference head; dilatih 100% pada generator display sintetis + augmentasi (blur, motion blur, affine).
   - Hasil: 97.8% single-frame pada citra real-world, 30 FPS; digit accuracy real-world 92%; mode filtering antar-frame menambah stabil.
3. Gushima & Kashima (2023). "Automatic Generation of Seven-Segment Display Image for Machine-Learning-Based Digital Meter Reading". PHM Society Asia-Pacific. DOI: 10.36001/phmap.2023.v4i1.3612
   - Generator citra sintetis otomatis dengan noise: refleksi matahari, bayangan, blur goyangan kamera.
   - Hasil: akurasi pembacaan 96.8%.
4. Moreira (2022). "Automated Medical Device Display Reading Using Deep Learning Object Detection". arXiv:2210.01325
   - Fine-tune EfficientDet & EfficientDet-lite pada foto alat medis (7-seg).
   - Hasil: >98% presisi deteksi & akurasi klasifikasi; EfficientDet-lite1 100%/100% (104 img, 438 digit).
5. Finnegan, Villarroel, Velardo, Tarassenko (2019). "Automated method for detecting and reading seven-segment digits from images of blood glucose metres and blood pressure monitors". J. Medical Engineering & Technology. DOI: 10.1080/03091902.2019.1673844
   - Dataset sintetis 7-seg untuk latih classifier + dataset citra real alat medis; HOG + neural network.
   - Hasil: 93% akurasi digit pada perangkat nyata; lokalisasi F1 0.87/0.80 (dataset publik).
6. Carvalho, Melo, Graça, Santos et al. (2023). "Deep Learning-Powered System for Real-Time Digital Meter Reading on Edge Devices". Applied Sciences 13(4):2315. DOI: 10.3390/app13042315
   - Fine-tuned EAST (deteksi) + fine-tuned CRNN (rekognisi), deploy edge/ONNX.
   - Hasil: <250 ms/frame preview, 1500 ms pipeline penuh; akurasi end-to-end 55-73% (kondisi sulit) — bukti gap sim-to-real itu nyata.
7. Xiang, Zhu, Ou, Zhang (2026). "Semi-Supervised Seven-Segment LED Display Recognition with an Integrated Data-Acquisition Framework". Sensors 26(1):265. DOI: 10.3390/s26010265
   - Masalah domain shift antar environment (cahaya, warna, kontras); semi-supervised adversarial (self-training + SE block + GAN adversarial examples).
   - Arah riset terkini: mengurangi label manual untuk adaptasi environment baru.
8. Laroca, Barroso, Diniz, Gonçalves et al. (2019). "Convolutional neural networks for automatic meter reading". J. Electronic Imaging. DOI: 10.1117/1.jei.28.1.013023
   - Pipeline AMR klasik: Fast-YOLO + tiga alternatif rekognisi (CR-Net, multi-task, CRNN); CR-Net menang.
   - Lanjutan: Salomon, Laroca, Menotti (2020) IJCNN, dataset & baseline dial meter. DOI: 10.1109/ijcnn48605.2020.9207318
9. Kanagarathinam & Sekar (2019). "Text detection and recognition in raw image dataset of seven segment digital energy meter display". Energy Reports 5:842-852. DOI: 10.1016/j.egyr.2019.07.004
10. Utomo, Pinem, Christoko (2021). "Pembacaan Meter Air dengan OCR LSTM-RNN pada Perangkat Mobile Tanpa Internet". Jurnal RESTI 5(1). DOI: 10.29207/resti.v5i1.2807
    - Hasil: 86% keseluruhan, 97% digit tunggal, ~2.3 s/proses; contoh sistem on-device Indonesia.

## B. Bukti model umum TIDAK cukup tanpa training khusus

- Low, Salleh, Law, Zakaria (2024). "Detecting and recognizing seven segment digits using a deep learning approach". ITM Web of Conferences 63:01007. DOI: 10.1051/itmconf/20246301007
  - Benchmark pretrained (PaddleOCR, MMOCR, EasyOCR, Tesseract) zero-shot pada dataset 7Seg (189 img, 165 valid).
  - Hasil: PARSeq terbaik pun hanya 56.97% word accuracy; CRNN ~49.09% (avg CER 26.23%); beberapa model <20% pada kondisi custom. Glare & LED bleeding = penyebab utama.
  - Rekomendasi paper: DBNet (PaddleOCR) untuk deteksi + fine-tuning untuk rekognisi.
  - Kode & protokol: https://github.com/Milsk01/FYP

## C. Referensi spesifik timbangan digital / elektronik

- Xu, Wang, Niu, Kan (2020). "A method of positioning and recognition of electronic scale characters based on deep learning". J. Phys. Conf. Ser. 1693:012122. DOI: 10.1088/1742-6596/1693/1/012122 — YOLOv3 + Deeplabv3+ + SVM untuk display timbangan elektronik (konteks: ujian kimia SMA).
- Jiang & Li (2026). "A method for recognizing the content of the digital display area of electronic scales based on image processing". ICCIIA 2026 (SPIE). DOI: 10.1117/12.3113037 — template matching 7-seg + koreksi Hamming: 99.7% pada 1.146 karakter, ~20 ms (baseline non-DL yang kuat di kondisi terkontrol).
- Dong, Zhang, Zhao (2019). "Digital Recognition of Weighing Instruments Based on Machine Vision". J. Phys. Conf. Ser. 1237:022153. DOI: 10.1088/1742-6596/1237/2/022153 — BP neural network, akurasi ~97%.
- Patent US 12561978 — "Electronic counter scale intelligent verification method based on deep learning" (verifikasi timbangan otomatis; deteksi karakter indikator + koreksi desimal).

## D. Model/artefak yang SUDAH ADA (siap dipakai / diuji / di-fine-tune)

Tesseract traineddata khusus 7-seg:
- https://github.com/Shreeshrii/tessdata_ssd — ssd.traineddata (Tesseract 4, 7-seg). Sudah dipakai di PWA ANALISA TIMBANG.
- https://github.com/arturaugusto/display_ocr (letsgodigital.traineddata) dan https://github.com/adrianlazaro8/Tesseract_sevenSegmentsLetsGoDigital — sudah dipakai di PWA.

Model rekognisi siap pakai:
- https://github.com/renjithsasidharan/seven-segment-ocr — keras-ocr (CRNN-CTC) dilatih data 7-seg -> model_float16.tflite (17.6 MB) + notebook Colab + skrip anotasi PPOCRLabel. Kandidat terbaik untuk dievaluasi & di-fine-tune ringan.
- https://github.com/faustomorales/keras-ocr — library; recognizer CRNN-CTC pretrained, ada dokumentasi training custom.
- PaddleOCR / MMOCR / EasyOCR — semua punya recognizer CRNN/SVTR/PARSeq yang bisa fine-tune (PaddleOCR menyediakan panduan fine-tuning recognition).
- HuggingFace: https://huggingface.co/sgenzer/seven-segment-led — Swin classifier digit tunggal (val acc 86.8%); terbatas (klasifikasi per digit, bukan baris). Dataset sgenzer/autotrain-data-seven-segment-led.

Non-DL (baseline):
- https://github.com/auerswal/ssocr (225*) — CLI klasik, morphology + template.
- https://github.com/jiweibo/SSOCR — lookup tabel segmen.
- https://github.com/suyashkumar/seven-segment-ocr — profil garis, tanpa model.
- https://github.com/SachaIZADI/Seven-Segment-OCR — eksperimen MNIST per-digit vs end-to-end (Goodfellow multi-digit).

Proyek timbangan nyata (referensi implementasi):
- https://github.com/JacobsFarm/OpenAgLoadMonitor — YOLO deteksi digit layar timbangan (feed mixer), dataset Roboflow publik.
- https://github.com/limkhysok/fast-ssocr — timbangan A12E: HSV red-masking + EasyOCR, format "179.5 kg".
- https://github.com/aniketsandhanwootz-wq/MFCVISION — pipeline Gemini VLM untuk foto timbangan.
- https://github.com/zhuzhenLi/ocr-digital-display — training CTC (gluon-cv) pakai generator sintetis TRDG.

## E. Dataset publik

- 7Seg — 189 citra (165 valid), AI Studio Baidu: https://aistudio.baidu.com/aistudio/datasetdetail/124936
- SSDI — 257 citra berlabel (eval deteksi ala ICDAR15; dipakai Low et al. 2024)
- SSDN (KMITL) — 13.600 citra digit (1.600/400 train/test normal): https://prip.it.kmitl.ac.th/seven-segment-display-number-ssdn-database/
- MiXaiLL76/7SEG_OCR (HuggingFace) — 3.333 sampel SINTETIS, label teks termasuk minus & titik desimal ("-7891", "3.730"), MIT: https://huggingface.co/datasets/MiXaiLL76/7SEG_OCR
- tomasko1987/seven-segment-digits (HuggingFace, MIT)
- CoccaGuo/Seven-Segment-Display-Dataset (GitHub releases)
- UFPR-AMR / UFPR-ADMR (Laroca) — meter nyata (dial; referensi)
- Roboflow Universe — cari "seven segment" / feed load monitors

## F. Generator sintetis (untuk "berbasis data sintetis")

- TextRecognitionDataGenerator (TRDG), 3.7k*: https://github.com/Belval/TextRecognitionDataGenerator — generate citra teks dengan font custom; dipakai untuk 7-seg di repo zhuzhenLi.
- Font DSEG (7-seg & 14-seg), 1.2k*: https://github.com/keshikan/DSEG ; font LetsGoDigital.
- Augmentasi yang dibuktikan literatur: glare/refleksi matahari, bayangan, motion blur, transformasi affine/perspektif, rotasi <60 derajat, warna LED (masking channel merah/hijau), LED bleeding (titik desimal menempel digit), noise background (Gushima 2023; Low 2024; Yenneti 2023).

## G. Desain eksperimen untuk judul "Evaluasi CRNN-CTC Berbasis Data Sintetis ..."

Variabel yang layak diuji:
1. Arsitektur: CRNN-CTC standar (VGG + BiLSTM, ~8-9 juta param) vs varian backbone (MobileNet/ResNet) vs SVTR/PARSeq.
2. Init: from scratch (random) vs init pretrained OCR lalu fine-tune -> ukur konvergensi & akurasi akhir.
3. Data sintetis: jumlah (10k/50k/100k), abrupsi augmentasi (mana yang paling menutup gap), synthetic-only vs synthetic + sedikit data real (fine-tune).
4. Decoder: CTC greedy vs beam-search; dampak pada angka.
5. Baseline pembanding: Tesseract ssd/letsgodigital, ssocr, template matching, PARSeq fine-tuned.
6. Metrik: CER, word accuracy, confusion digit khas (0/8, 6/5, 1/7), latensi on-device (ONNX), stabilitas antar-frame (mode filtering).
7. WAJIB: test set real lapangan (foto timbangan sesungguhnya) — tanpa ini, klaim "sintetis" tidak terbukti (bukti drop besar: PARSeq 57% di Low et al.; Carvalho 55-73% end-to-end).

Novelti yang realistis: protokol evaluasi + dataset sintetis domain timbangan + analisis gap sim-to-real + rekomendasi resep augmentasi. Tidak perlu arsitektur baru.

## H. Catatan untuk PWA ANALISA TIMBANG

- Sudah ada: Tesseract ssd + letsgodigital + CNN ONNX sintetis (~50% BETA). Eksperimen judul ini bisa langsung memakai app sebagai testbed.
- Jalur: (a) generate dataset sintetis domain timbangan (TRDG + DSEG/LetsGoDigital + augmentasi LED merah); (b) latih CRNN-CTC, export ONNX (vocab 0123456789.- seperti train.py sekarang); (c) benchmark vs Tesseract ssd; (d) fine-tune dengan export Mode Training (ground truth asli lapangan).
- ROI wajib sinkron 3 tempat (CaptureOCR.tsx <-> camera.ts <-> bracket); ingat constraint gate 0.95 dan tanpa input manual digit.

## Catatan jujur

- Tidak ada model publik 7-seg "tinggal comot" untuk kondisi lapangan; yang ada terbatas (Tesseract traineddata, repo kecil, classifier digit).
- Akurasi 96-99% di banyak paper = kondisi terkontrol; end-to-end in-the-wild realistis 55-92% (tergantung glare/kamera).
- "From scratch" untuk CRNN: murah dan terbukti; yang mahal (dan justru inti evaluasi) adalah gap sintetis ke kondisi nyata.
