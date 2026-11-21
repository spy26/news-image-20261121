#!/usr/bin/env python3
"""Penyalin gambar entri untuk lomba news-image-20261121.

Skrip kecil ini mengambil berkas ``entry.png`` yang duduk di sebelah
skrip ini lalu menaruh salinannya di folder keluaran sebagai
``entry.png``. Tidak ada pengolahan gambar di sini: yang disalin
adalah byte demi byte, supaya hasil akhirnya identik dengan aslinya.

Folder keluaran dibaca dari variabel lingkungan
``MAKEFUN_OUTPUT_DIR``; kalau variabel itu tidak diisi, dipakai
``/output``. Sebelum menyalin, berkas diperiksa dulu: harus diawali
tanda JPEG (``FF D8``) dan ukurannya tidak boleh melewati 1 MiB.
Sesudah menyalin, sidik hash SHA-256 salinan dicocokkan dengan
sumbernya; kalau tidak cocok, salinan dibuang dan program berhenti
dengan pesan galat.
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

JPEG_TANDA = b"\xff\xd8"
BATAS_BYTE = 1 * 1024 * 1024
NAMA_BERKAS = "entry.png"


def cari_sumber() -> Path:
    """Kembalikan alamat berkas sumber di sebelah skrip ini."""
    return Path(__file__).resolve().parent / NAMA_BERKAS


def folder_keluaran() -> Path:
    """Tentukan folder tujuan dari lingkungan, atau /output."""
    import os

    tujuan = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    return Path(tujuan) if tujuan else Path("/output")


def sidik_sha256(berkas: Path) -> str:
    """Hitung sidik SHA-256 dari isi sebuah berkas."""
    pencerna = hashlib.sha256()
    with berkas.open("rb") as gagang:
        while True:
            potongan = gagang.read(1024 * 1024)
            if not potongan:
                break
            pencerna.update(potongan)
    return pencerna.hexdigest()


def periksa_berkas(sumber: Path) -> int:
    """Pastikan sumber ada, berformat JPEG, dan ukurannya wajar.

    Mengembalikan ukuran sumber dalam byte bila semua pemeriksaan
    lolos; kalau tidak, program berhenti dengan pesan yang jelas.
    """
    if not sumber.is_file():
        sys.exit(f"gagal: berkas sumber tidak ketemu di {sumber}")
    ukuran = sumber.stat().st_size
    if ukuran == 0:
        sys.exit("gagal: berkas sumber kosong, tidak ada yang disalin")
    if ukuran > BATAS_BYTE:
        sys.exit(
            f"gagal: berkas sumber {ukuran} byte, melewati batas {BATAS_BYTE} byte"
        )
    with sumber.open("rb") as gagang:
        awal = gagang.read(2)
    if awal != JPEG_TANDA:
        sys.exit("gagal: berkas sumber bukan JPEG (tanda awal tidak cocok)")
    return ukuran


def salin_dan_cocokkan(sumber: Path, tujuan: Path) -> str:
    """Salin sumber ke tujuan lalu cocokkan sidik hash keduanya.

    Mengembalikan sidik SHA-256 sumber. Bila salinan tidak cocok,
    salinan dihapus dan program berhenti dengan galat.
    """
    if sumber.resolve() == tujuan.resolve():
        sys.exit("gagal: sumber dan tujuan itu berkas yang sama")
    tujuan.parent.mkdir(parents=True, exist_ok=True)
    data = sumber.read_bytes()
    tujuan.write_bytes(data)
    sidik_asli = hashlib.sha256(data).hexdigest()
    if sidik_sha256(tujuan) != sidik_asli:
        tujuan.unlink(missing_ok=True)
        sys.exit("gagal: salinan tidak identik dengan sumber, salinan dibuang")
    return sidik_asli


def main() -> int:
    sumber = cari_sumber()
    ukuran = periksa_berkas(sumber)
    tujuan = folder_keluaran() / NAMA_BERKAS
    sidik = salin_dan_cocokkan(sumber, tujuan)
    print(f"tersalin: {sumber} ({ukuran} byte) -> {tujuan}")
    print(f"format diperiksa: JPEG, {ukuran} byte, di bawah batas 1 MiB")
    print(f"sha256: {sidik}")
    print("verifikasi: salinan identik dengan sumber")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
