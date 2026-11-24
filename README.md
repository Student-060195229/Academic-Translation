# Academic Translation

Skill AI untuk penerjemahan akademis dari bahasa Arab ke Bahasa Indonesia, khususnya teks kitab kuning dan literatur Islam klasik.

Proyek ini memprioritaskan:

- kesetiaan terhadap teks sumber;
- ketepatan makna dan struktur;
- konsistensi istilah syar'i;
- kelengkapan terjemahan; dan
- Bahasa Indonesia yang formal, edukatif, dan layak digunakan dalam kurikulum pesantren.

> **Aman Makna — Aman Teks — Aman Struktur — Aman Istilah — Layak Kurikulum**

## Ringkasan

Academic Translation bukan alat peringkas, penafsir, pensyarah, atau editor isi kitab. Skill ini berfungsi untuk memindahkan teks Arab yang diberikan pengguna ke Bahasa Indonesia tanpa menambah, mengurangi, atau mengubah teks sumber.

Fitur utamanya meliputi:

- penerjemahan Arab–Indonesia dengan pendekatan **Literal–Kontekstual**;
- pemeliharaan urutan kalimat dan hubungan gramatikal;
- penjagaan negasi, pengecualian, penegasan, subjek, objek, dan rujukan dhamir;
- konsistensi istilah teknis Islam;
- penanganan ayat dan hadis tanpa menambah dalil, takhrij, status hadis, atau tafsir;
- dukungan input teks dan gambar;
- mode validasi terjemahan, penjelasan, dan perbandingan.

## Struktur Repository

```text
Academic-Translation/
├── .github/
│   └── workflows/
│       └── quality.yml       # Pemeriksaan sinkronisasi dan pengujian otomatis
├── scripts/
│   ├── sync_skill.py         # Sinkronisasi pemeriksaan Program.py
│   └── README.md
├── tests/
│   └── test_project.py       # Pengujian kualitas proyek
├── LICENSE                   # Lisensi Academic Use License (AUL) 1.0
├── Program.py                # Pemuat spesifikasi skill
├── README.md                 # Dokumentasi proyek
├── Rules.yaml                # Metadata dan aturan terstruktur
├── SKILL.md                  # Sumber utama instruksi skill
└── .gitignore
```

## Berkas Utama

### `SKILL.md`

Sumber utama yang memuat identitas, ruang lingkup, prinsip penerjemahan, hierarki prioritas, larangan, mode output, dan standar kualitas skill.

### `Rules.yaml`

Metadata terstruktur yang mendokumentasikan nama skill, domain, metode, kebijakan sumber, aturan tata bahasa, istilah syar'i, pola input gambar, mode kerja, dan pemeriksaan kualitas.

### `Program.py`

Memuat teks `SKILL.md` melalui fungsi `get_skill()` dan variabel `SKILL` untuk kompatibilitas integrasi lama.

### `scripts/sync_skill.py`

Memastikan konfigurasi `Program.py` tetap sinkron dengan struktur skill saat repo diperbarui.

### `tests/test_project.py`

Memeriksa ketersediaan `SKILL.md`, kesesuaian pemuatan skill oleh `Program.py`, dan keberadaan bagian penting pada `Rules.yaml`.

## Prinsip Penerjemahan

### Hierarki prioritas

Urutan prioritas penerjemahan adalah:

1. kesetiaan terhadap teks asli;
2. ketepatan makna;
3. ketepatan struktur;
4. ketepatan istilah syar'i;
5. kelengkapan;
6. konsistensi;
7. keterbacaan; dan
8. keindahan bahasa.

### Unsur yang dijaga

Skill ini memperhatikan jumlah ismiyyah dan fi'liyyah, mubtada, khabar, fi'il, fa'il, maf'ul bih, na'at, man'ut, idhafah, jar-majrur, dhamir, nafy, istitsna', taukid, qashr, hashr, syarat, dan hubungan antarkalimat.

Negasi, pengecualian, dan penegasan harus tetap terasa dalam terjemahan. Misalnya, pola `ما ... إلا` atau `لا ... إلا` dipertahankan dalam bentuk setara seperti “tidak ... kecuali ...” jika konteks mengizinkan.

### Batasan sumber

Skill hanya menerjemahkan teks yang benar-benar tersedia pada input. Skill tidak:

- melanjutkan teks yang terpotong atau hilang;
- menebak bagian yang tidak terbaca;
- mengarang lafaz dari ingatan;
- mengambil konteks dari edisi lain;
- menambah dalil, hadis, tafsir, atau syarah;
- memperbaiki teks sumber secara diam-diam;
- mengubah istilah syar'i secara bebas; atau
- memasukkan opini penerjemah.

Untuk teks tidak terbaca pada gambar, skill menggunakan penanda `[teks tidak terbaca]`. Jika rujukan dhamir tidak dapat dipastikan, dapat digunakan `[rujukan dhamir perlu verifikasi]`.

## Mode Penggunaan

### Terjemahan

Jika pengguna hanya memberikan teks Arab, output default adalah:

```markdown
## Terjemahan

[hasil terjemahan]
```

### Validasi

Gunakan perintah seperti:

- `Periksa terjemahan ini.`
- `Validasi terjemahan.`
- `Cek terjemahan.`

Mode validasi memeriksa makna, kelengkapan, penambahan atau penghilangan unsur, dhamir, subjek, objek, negasi, pengecualian, penegasan, istilah, dan struktur.

### Penjelasan

Jika pengguna meminta penjelasan, terjemahan dipisahkan dari penjelasan agar komentar tidak tercampur ke dalam teks terjemahan.

### Perbandingan

Jika beberapa versi terjemahan diberikan, setiap versi dinilai terutama berdasarkan ketepatan makna, kesetiaan struktur, ketepatan istilah, kelengkapan, dan keterbacaan.

## Menjalankan di Lokal

Pastikan Python 3.11 atau versi Python 3 yang kompatibel sudah terpasang.

```bash
python Program.py
```

Perintah tersebut mencetak seluruh spesifikasi skill dari `SKILL.md`.

### Mengambil Skill dari Aplikasi Python

```python
from Program import get_skill

skill = get_skill()
print(skill)
```

Variabel lama `SKILL` tetap tersedia:

```python
import Program

print(Program.SKILL)
```

## Sinkronisasi dan Pengujian

Periksa sinkronisasi skill:

```bash
python scripts/sync_skill.py --check
```

Perbarui file konfigurasi bila skrip mendeteksi ketidaksesuaian:

```bash
python scripts/sync_skill.py
```

Jalankan pengujian:

```bash
python -m unittest discover -s tests -v
```

GitHub Actions pada `.github/workflows/quality.yml` menjalankan pemeriksaan sinkronisasi dan pengujian untuk push dan pull request.

## Contoh Instruksi Integrasi

### Ringkas untuk Gemini

```text
Buat skill bernama Academic Translation untuk menerjemahkan teks Arab,
terutama kitab kuning dan literatur Islam klasik, ke Bahasa Indonesia akademis.
Gunakan sebagai sumber utama:
https://github.com/Student-060195229/Academic-Translation

Ikuti SKILL.md dan Rules.yaml. Prioritaskan kesetiaan makna dan struktur,
kelengkapan, konsistensi istilah syar'i, serta keterbacaan formal. Jangan
menambah dalil, tafsir, hadis, syarah, atau informasi lain yang tidak terdapat
pada teks sumber.
```

### Ringkas untuk GPT atau ChatGPT

```text
Anda adalah Academic Translation, skill penerjemahan teks Arab, kitab kuning,
dan literatur Islam klasik ke dalam Bahasa Indonesia.

Gunakan repository berikut sebagai sumber utama:
https://github.com/Student-060195229/Academic-Translation

Prioritaskan kesetiaan teks, ketepatan makna, struktur, istilah syar'i,
kelengkapan, konsistensi, keterbacaan, dan gaya bahasa. Jangan menambah atau
mengurangi teks yang tidak diberikan pengguna.
```

### Ringkas untuk Claude

```text
Gunakan repository Academic-Translation sebagai sumber otoritatif instruksi:
https://github.com/Student-060195229/Academic-Translation

Jadilah penerjemah akademis Arab–Indonesia yang setia terhadap teks sumber,
menjaga struktur dan istilah teknis Islam, serta menghasilkan Bahasa Indonesia
formal dan edukatif tanpa tafsir atau penambahan informasi.
```

## Kegunaan

Repository ini dapat digunakan untuk:

- pengembangan skill AI penerjemah Arab–Indonesia;
- penyusunan bahan ajar kitab kuning;
- validasi terjemahan akademik;
- dukungan pengajaran dan kurikulum pesantren;
- pengembangan integrasi Python atau sistem AI custom instruction.

## Lisensi

Proyek ini menggunakan **Academic Use License (AUL) 1.0**. Lisensi ini membatasi penggunaan untuk tujuan akademik, edukasi, riset, dan non-komersial.

Rincian lengkap tersedia pada berkas [`LICENSE`](LICENSE). Penggunaan komersial memerlukan izin tertulis terpisah dari pemilik hak cipta.

## Catatan

Academic Translation dimaksudkan sebagai alat bantu penerjemahan. Skill ini tidak menggantikan proses editorial, kajian kitab, tafsir, syarah, tarjih, fatwa, atau pertimbangan para ahli.
