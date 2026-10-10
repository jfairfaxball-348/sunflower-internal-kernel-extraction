import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import semantics
import validate


class SemanticTests(unittest.TestCase):
    def test_fixed_population(self):
        data = json.loads((ROOT / "experiments/SEMANTIC_FIXTURES.json").read_text())
        for case in data["cases"]:
            with self.subTest(case=case["id"]):
                ambient = semantics.family(case["ambient"])
                selected = tuple(ambient[i] for i in case["selected_indices"])
                self.assertEqual(semantics.witnessed(selected, selected, case["m"]), case["internal"])
                self.assertEqual(semantics.witnessed(selected, ambient, case["m"]), case["external"])
                self.assertEqual(semantics.internal_by_links(selected, case["m"]), case["internal"])

    def test_kernel_must_be_exact(self):
        edges = semantics.family([[1, 2, 3], [1, 2, 4], [1, 2, 5]])
        self.assertFalse(semantics.has_exact_sunflower(edges, 3, frozenset([1])))
        self.assertTrue(semantics.has_exact_sunflower(edges, 3, frozenset([1, 2])))

    def test_repeated_petals_rejected(self):
        with self.assertRaises(ValueError):
            semantics.family([[1, 2], [1, 2]])

    def test_invalid_m_rejected_even_for_empty_family(self):
        with self.assertRaises(ValueError):
            semantics.witnessed((), (), 1)

    def test_external_substitution_rejected(self):
        target = copy.deepcopy(validate.read("research/TARGET.json"))
        target["witness_family"] = "F"
        with self.assertRaises(AssertionError):
            validate.check_target(target)

    def test_constant_dependence_cannot_weaken(self):
        target = copy.deepcopy(validate.read("research/TARGET.json"))
        target["constant_depends_only_on"] = ["k", "m"]
        with self.assertRaises(AssertionError):
            validate.check_target(target)

    def test_project_records(self):
        validate.main()


if __name__ == "__main__":
    unittest.main()
