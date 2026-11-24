#!/usr/bin/env python3
"""Sinkronisasi SKILL.md dengan Program.py.

SKILL.md adalah satu-sumber-kebenaran untuk instruksi skill.
Skrip ini memastikan Program.py tetap menjadi pemuat SKILL.md yang konsisten
untuk integrasi lama.
"""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILL_FILE = ROOT / "SKILL.md"
PROGRAM_FILE = ROOT / "Program.py"


def get_skill() -> str:
    if not SKILL_FILE.is_file():
        raise FileNotFoundError(f"Sumber skill tidak ditemukan: {SKILL_FILE}")
    return SKILL_FILE.read_text(encoding="utf-8").strip()


def build_program() -> str:
    return '''# -*- coding: utf-8 -*-
"""
Pemuatan spesifikasi Academic Translation.

SKILL.md adalah satu-sumber-kebenaran untuk instruksi skill.
Aturan terstruktur disimpan secara terpisah pada Rules.yaml.
"""

from pathlib import Path


def get_skill() -> str:
    """Memuat spesifikasi skill lengkap dari SKILL.md."""
    skill_path = Path(__file__).with_name("SKILL.md")
    if not skill_path.is_file():
        raise FileNotFoundError(
            f"Sumber skill tidak ditemukan: {skill_path}"
        )
    return skill_path.read_text(encoding="utf-8").strip()


# Nama SKILL dipertahankan untuk kompatibilitas integrasi lama.
SKILL = get_skill()


if __name__ == "__main__":
    print(SKILL)
'''


def synchronize(check_only: bool = False) -> bool:
    get_skill()

    if not PROGRAM_FILE.is_file():
        raise FileNotFoundError(f"File program tidak ditemukan: {PROGRAM_FILE}")

    generated = build_program()
    current = PROGRAM_FILE.read_text(encoding="utf-8")

    if current == generated:
        print("Sinkron: SKILL.md dan Program.py konsisten.")
        return True

    if check_only:
        print("Tidak sinkron: jalankan 'python scripts/sync_skill.py'.")
        return False

    PROGRAM_FILE.write_text(generated, encoding="utf-8")
    print("Sinkronisasi selesai: Program.py diperbarui.")
    return True


if __name__ == "__main__":
    check_only = "--check" in sys.argv

    try:
        success = synchronize(check_only=check_only)
    except (FileNotFoundError, OSError) as error:
        print(f"Kesalahan sinkronisasi: {error}", file=sys.stderr)
        raise SystemExit(1)

    if not success:
        raise SystemExit(1)
