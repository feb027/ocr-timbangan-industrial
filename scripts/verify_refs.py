#!/usr/bin/env python3
"""Cek semua DOI di jurnal-terindeks.md ke Crossref API.

Pakai: python3 scripts/verify_refs.py [file.md]
Exit 0 kalau semua DOI resolve & metadata cocok; exit 1 kalau ada yang gagal.

Gunanya: mencegah DOI salah-tunjuk seperti kasus Kanagarathinam (10.1016/j.egyr.2019.06.016
= paper baterai EV, bukan 7-segment dataset).
"""
import json
import pathlib
import re
import sys
import time
import urllib.parse
import urllib.request

UA = {"User-Agent": "ref-verifier/1.0 (paper check)"}


def crossref(doi: str):
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
    for _ in range(3):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=40) as r:
                return json.load(r)["message"]
        except Exception:
            time.sleep(2)
    return None


def main(path: str) -> int:
    text = pathlib.Path(path).read_text()
    # Klaim kalimat pendek sebelum DOI diambil dari baris yang sama -> dipakai sebagai ekspektasi
    rows = re.findall(r"^\s*\d+\.\s.*?https://doi\.org/(\S+)\s*$", text, re.M)
    if not rows:
        print("Tidak ada DOI ditemukan di", path)
        return 1
    bad = 0
    for doi in rows:
        m = crossref(doi)
        if not m:
            print(f"[GAGAL] {doi} — tidak resolve di Crossref")
            bad += 1
            continue
        jr = (m.get("container-title") or ["?"])[0]
        yr = (m.get("published", {}).get("date-parts") or [[None]])[0][0]
        au = (m.get("author") or [{}])[0].get("family", "?")
        print(f"[OK] {doi} :: {jr} ({yr}) — {au} dkk. — {m.get('title', ['?'])[0][:70]}")
    print(f"\n{len(rows) - bad}/{len(rows)} DOI valid.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "jurnal-terindeks.md"))
