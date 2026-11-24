import unittest
from pathlib import Path

import Program


ROOT = Path(__file__).resolve().parents[1]


class ProjectQualityTests(unittest.TestCase):
    def test_skill_md_exists_and_is_nonempty(self):
        skill_file = ROOT / "SKILL.md"
        self.assertTrue(skill_file.is_file())
        self.assertGreater(len(skill_file.read_text(encoding="utf-8").strip()), 0)

    def test_program_loads_the_same_skill_text(self):
        skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8").strip()
        self.assertEqual(Program.get_skill(), skill_text)
        self.assertEqual(Program.SKILL, skill_text)

    def test_rules_yaml_exists_and_has_required_sections(self):
        rules_file = ROOT / "Rules.yaml"
        self.assertTrue(rules_file.is_file())
        rules = rules_file.read_text(encoding="utf-8")
        for required in (
            "name:",
            "primary_method:",
            "priority_order:",
            "workflow:",
            "final_standard:",
        ):
            self.assertIn(required, rules)


if __name__ == "__main__":
    unittest.main()
