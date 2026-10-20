# Academic Translation

Skill AI untuk penerjemahan secara akademis, dengan fokus pada terjemahan teks Arab ke Bahasa Indonesia yang akurat, konsisten, dan sesuai kaidah keilmuan Islam klasik.

Repository ini berisi spesifikasi skill AI untuk penerjemah kitab kuning dan literatur Islam klasik. Fokus utamanya adalah menjaga keakuratan makna, struktur kalimat, istilah syar'i, serta batasan teks sumber agar tidak terjadi penambahan, pengurangan, atau interpretasi yang melampaui konteks yang tersedia.

## Latar Belakang dan Catatan Proyek

Proyek ini dibuat untuk mendukung penerjemahan modul bahan ajar yang digunakan di Pondok Pesantren Darul Ihsan Madiun. Materi yang diterjemahkan mengacu pada sistem pembelajaran dan standar kurikulum yang berorientasi pada pendekatan Muadalah Saudi Arabia, khususnya dalam menjaga akurasi istilah, struktur, serta kesesuaian materi pendidikan Islam dengan kebutuhan pembelajaran yang terstandar.

Dengan demikian, skill ini tidak hanya berfungsi sebagai alat penerjemah umum, tetapi juga sebagai pendukung akademik untuk menjaga kualitas terjemahan modul pembelajaran agar tetap setia terhadap sumber, konsisten dalam istilah keislaman, dan layak digunakan dalam konteks pendidikan pesantren dan kurikulum formal.

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

Project ini bertujuan untuk menjaga kualitas terjemahan secara akademis dan tidak menggantikan metode tafsir atau syarah. Oleh karena itu, output yang dihasilkan harus berfokus pada pemindahan makna secara aman dan setia terhadap teks sumber.

---

Academic Translation
Skill AI untuk penerjemahan secara akademis.
