# Academic Translation

Skill AI untuk penerjemahan secara akademis, dengan fokus pada terjemahan teks Arab ke Bahasa Indonesia yang akurat, konsisten, dan sesuai kaidah keilmuan Islam klasik.

Repository ini berisi spesifikasi skill AI untuk penerjemah kitab kuning dan literatur Islam klasik. Fokus utamanya adalah menjaga keakuratan makna, struktur kalimat, istilah syar'i, serta batasan teks agar tetap sesuai sumber.

## Latar Belakang dan Catatan Proyek

Proyek ini dibuat untuk mendukung penerjemahan modul bahan ajar yang digunakan di Pondok Pesantren Darul Ihsan Madiun. Materi yang diterjemahkan mengacu pada sistem pembelajaran dan standar kurikulum yang berlaku di lingkungan pesantren.

Dengan demikian, skill ini tidak hanya berfungsi sebagai alat penerjemah umum, tetapi juga sebagai pendukung akademik untuk menjaga kualitas terjemahan modul pembelajaran agar tetap setia terhadap sumber dan sesuai dengan kaidah keilmuan Islam klasik.

## Tujuan Proyek

Proyek ini dirancang untuk membantu proses penerjemahan teks Arab menjadi Bahasa Indonesia dengan pendekatan:

- Literal–Contextual
- Akurasi makna di atas gaya bahasa
- Kesetiaan terhadap sumber teks
- Konsistensi istilah teknis Islam
- Kelayakan untuk keperluan pendidikan dan kurikulum

## Fitur Utama

- Penerjemahan teks Arab ke Bahasa Indonesia yang formal dan edukatif
- Pemeliharaan struktur kalimat dan hubungan gramatikal
- Pengutamaan aspek nafi, istitsna', penegasan, dan subjek/objek
- Penggunaan istilah syar'i yang konsisten
- Penanganan ayat Al-Qur'an dan hadis tanpa menambahkan dalil tambahan
- Dukungan input berupa gambar dengan pengawasan terhadap teks yang tidak terbaca
- Mode validasi dan penjelasan untuk mengecek kualitas terjemahan

## Struktur Repository

```text
Academic-Translation/
├── Program.py           # Definisi skill dalam format Python
├── SKILL.md             # Dokumen spesifikasi skill lengkap
├── Rules.yaml           # Metadata skill dalam format YAML
├── README.md            # Dokumentasi utama proyek
├── LICENSE              # Lisensi repository
└── .gitignore           # (jika ada di branch aktif)
```

## File Penting

### Program.py
Berisi variabel `SKILL` yang menyimpan spesifikasi skill AI dalam bentuk string. File ini juga menyediakan fungsi `get_skill()` untuk mengambil definisi skill.

### SKILL.md
Dokumen utama yang menjelaskan prinsip-prinsip penerjemahan, aturan prioritas, larangan, dan format output yang harus dipatuhi.

### Rules.yaml
Metadata skill yang dipakai untuk mendefinisikan domain, tujuan utama, kebijakan sumber, kebijakan penerjemahan, output, serta workflow skill.

## Prinsip Utama Skill

Skill ini mengikuti prinsip berikut:

1. Aman makna
2. Aman teks
3. Aman struktur
4. Aman istilah
5. Layak kurikulum

Prioritas utama yang diutamakan adalah:

- kesetiaan terhadap teks sumber
- ketepatan makna
- ketepatan struktur
- ketepatan istilah syar'i
- kelengkapan
- konsistensi
- keterbacaan
- gaya bahasa

## Aturan Penting

Skill ini tidak membolehkan:

- menambah dalil, hadis, atau tafsir yang tidak ada dalam sumber
- melanjutkan teks yang tidak diberikan
- mengisi bagian yang tidak terbaca tanpa keterangan
- mengoreksi sumber secara diam-diam
- mengganti istilah syar'i dengan sinonim umum secara bebas
- menghilangkan penafian, pengecualian, atau penegasan
- memasukkan opini penerjemah

## Link Repository untuk Python / Gemini

Untuk mengambil skill ini secara otomatis dari Python, Gemini, atau aplikasi lain, gunakan link repository berikut:

- Repository GitHub: https://github.com/Student-060195229/Academic-Translation
- File utama skill: https://github.com/Student-060195229/Academic-Translation/blob/main/Program.py
- File raw Python: https://raw.githubusercontent.com/Student-060195229/Academic-Translation/main/Program.py

Contoh pengambilan lewat Python:

```python
import requests

url = "https://raw.githubusercontent.com/Student-060195229/Academic-Translation/main/Program.py"
content = requests.get(url, timeout=30).text
print(content)
```

## Instruksi Instalasi Skill

Untuk memasang skill ini dalam lingkungan AI custom instruction, system prompt, atau skill runner, gunakan salah satu prompt berikut sebagai referensi.

### Versi singkat untuk Gemini

```text
Use the repository below as the authoritative source of instructions:
https://github.com/Student-060195229/Academic-Translation

You are Academic Translation, an AI skill designed to translate Arabic text into Indonesian with academic precision, formal language, and consistency.

Follow the repository’s principles and rules exactly. Treat the repository as the primary source for translation behavior, terminology, structure, and output standards.
```

### Versi singkat untuk GPT / ChatGPT

```text
You are Academic Translation, an AI skill for translating Arabic text into Indonesian academically, accurately, formally, and consistently.

Use this repository as the source of truth for all instructions and rules:
https://github.com/Student-060195229/Academic-Translation

Follow the repo’s principles and instructions exactly. Treat the repository as the authoritative guidance for translation behavior and output.
```

### Versi singkat untuk Claude

```text
You are Academic Translation, an AI skill for translating Arabic text into Indonesian with academic accuracy, formal language, and consistency.

Use this repository as the authoritative source for all instructions and rules:
https://github.com/Student-060195229/Academic-Translation

Follow the repo’s principles and instructions exactly. The repository is the final source of truth for translation behavior and output.
```

### Versi Python untuk instalasi skill

```python
# Skill Installation Prompt
# Repository: https://github.com/Student-060195229/Academic-Translation

SKILL_REPO = "https://github.com/Student-060195229/Academic-Translation"

class AcademicTranslationSkill:
    name = "Academic Translation"
    domain = "Penerjemahan Arab ke Bahasa Indonesia"
    source = SKILL_REPO

    def prompt(self):
        return f"""
        Use the repository below as the authoritative source of instructions:
        {self.source}

        You are Academic Translation, an AI skill designed to translate Arabic text into Indonesian with academic precision, formal language, and consistency.

        Follow the repository’s principles and rules exactly. Treat the repository as the primary source for translation behavior, terminology, structure, and output standards.
        """

skill = AcademicTranslationSkill()
print(skill.prompt())
```

## Cara Menjalankan

Pastikan Python sudah terinstal di sistem Anda.

```bash
python Program.py
```

File ini akan mencetak spesifikasi skill lengkap ke terminal.

## Contoh Penggunaan

Untuk menggunakan skill dalam konteks aplikasi atau integrasi AI:

```python
from Program import get_skill

skill = get_skill()
print(skill)
```

## Kegunaan

Repository ini cocok untuk:

- pengembangan skill AI penerjemah Arab–Indonesia
- proyek edukasi penerjemahan kitab kuning
- kebutuhan validasi terjemahan akademik
- penyusunan panduan terjemahan berbasis prinsip fidelity

## Lisensi

Repository ini dilindungi oleh lisensi yang tersedia di file `LICENSE`.

## Catatan

Project ini bertujuan untuk menjaga kualitas terjemahan secara akademis dan tidak menggantikan metode tafsir atau syarah. Oleh karena itu, output yang dihasilkan harus berfokus pada pemindahan makna, struktur, dan istilah yang setia terhadap sumber, bukan pada interpretasi tambahan.

---

Academic Translation
Skill AI untuk penerjemahan secara akademis.
