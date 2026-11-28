# Academic Translation — Claude Skill

Folder ini disiapkan sebagai paket skill untuk Claude. Di `SKILL.md` terdapat metadata YAML (`name` dan `description`) beserta instruksi skill.

## Claude.ai / Claude Desktop

1. Unduh repository sebagai ZIP atau clone repository.
2. Buat ZIP yang berisi folder `claude-skill` sehingga `claude-skill/SKILL.md` berada di dalamnya. Jangan mengunggah ZIP seluruh repo jika importer meminta `SKILL.md` berada tepat di root folder skill.
3. Di Claude, buka **Customize > Skills** (nama menu dapat berbeda menurut versi/akun), pilih opsi untuk menambahkan atau mengunggah skill, lalu unggah ZIP tersebut.
4. Pastikan skill aktif. Coba minta: “Terjemahkan teks Arab ini ke Bahasa Indonesia secara setia.”

Jika unggahan masih gagal, periksa pesan error dan pastikan ZIP tidak memiliki folder induk tambahan di atas folder skill. Pada sebagian akun, fitur Skills perlu diaktifkan terlebih dahulu.

## Claude Code

Salin folder ini ke `.claude/skills/academic-translation/` dalam proyek, atau ke `~/.claude/skills/academic-translation/` untuk penggunaan global. Pastikan file berada di `.../academic-translation/SKILL.md`.
