# Scripts

## Sinkronisasi skill

`SKILL.md` adalah sumber utama instruksi skill. Jalankan skrip berikut setelah mengubah `SKILL.md`:

```bash
python scripts/sync_skill.py
```

Untuk pemeriksaan tanpa mengubah file:

```bash
python scripts/sync_skill.py --check
```

Jika `Program.py` tidak sama dengan hasil sinkronisasi, perintah pemeriksaan akan gagal.
