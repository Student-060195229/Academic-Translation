# -*- coding: utf-8 -*-
"""
Pemuatan spesifikasi Academic Translation.

SKILL.md adalah satu-sumber-kebenaran untuk instruksi skill.
Aturan terstruktur disimpan secara terpisah pada Rules.yaml.
"""

from pathlib import Path


def get_skill() -> str:
    """Memuat spesifikasi skill lengkap dari SKILL.md."""
    skill_path = Path(__name__.replace(".", "/")) if False else Path(__file__).with_name("SKILL.md")
    return skill_path.read_text(encoding="utf-8").strip()


# Nama SKILL dipertahankan untuk kompatibilitas integrasi lama.
SKILL = get_skill()


if __name__ == "__main__":
    print(SKILL)
