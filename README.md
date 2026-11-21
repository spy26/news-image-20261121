# news-image-20261121 — Missiles Hit NATO Soil

[![news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/spy26/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/spy26/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121)

Entri lomba gambar berita make.fun untuk edisi **Saturday 21 November 2026**, dibuat
sebagai sampul koran satu halaman yang merangkum hari yang penuh gejolak.

## Isi gambar

Berita utama di halaman depan: **Russian missiles land in Poland — NATO soil**,
dengan kutipan Perdana Menteri Polandia Tusk yang menyebut serangan itu sebagai
*deliberate provocation*. Di bawahnya, empat sorotan hari itu:

- **KYIV STRUCK** — 400+ drones dan 110+ missiles menghantam Kyiv.
- **MARKETS CRASH** — S&P -3.7%, Nasdaq -5.3% saat pasar panik.
- **COP31 NO DEAL** — perundingan iklim berakhir tanpa kesepakatan.
- **CYCLONE AKVAN** — 372,000 orang dievakuasi dari jalur badai.

Gambar ini (1024×1024, JPEG) sudah jadi dan tersimpan sebagai `entry.png`.
Tidak ada proses olah gambar di repo ini: apa yang kamu lihat di `entry.png`
adalah hasil akhirnya, dan skrip hanya bertugas menyalinnya utuh.

## Cara menjalankan

Skrip `main.py` hanya menyalin `entry.png` ke folder keluaran yang kamu pilih,
sambil memeriksa keaslian berkasnya. Ia memakai pustaka standar Python saja,
jadi tidak ada yang perlu dipasang. Contoh, dengan folder keluaran bernama
`hasil/` di dalam repo ini:

```sh
MAKEFUN_OUTPUT_DIR=hasil python3 main.py
```

Sesudah perintah itu selesai, salinan gambarnya ada di `hasil/entry.png`.
Kalau variabel `MAKEFUN_OUTPUT_DIR` tidak kamu isi, skrip memakai `/output`
sebagai tujuan. Skrip menolak berkas yang bukan JPEG dan yang ukurannya
melewati 1 MiB, lalu mencocokkan sidik SHA-256 salinan dengan sumbernya —
dua kali jalan harus menghasilkan byte yang persis sama.

## Berkas

- `entry.png` — gambar entri final.
- `main.py` — penyalin gambar dengan pemeriksaan format, ukuran, dan hash.
- `LICENSE` — lisensi MIT.

## Lisensi

MIT — lihat `LICENSE`.
