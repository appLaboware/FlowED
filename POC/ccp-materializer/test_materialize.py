import copy
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from materialize import ValidationError, compile_poc, read_json, structure, validate_contract


ROOT = Path(__file__).resolve().parent


class MaterializerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.inputs = self.root / "inputs"
        shutil.copytree(ROOT / "inputs", self.inputs)
        self.output = self.root / "output"

    def rewrite(self, name, value):
        (self.inputs / name).write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")

    def test_three_projections_preserve_exact_source_and_are_reproducible(self):
        before = (self.inputs / "source.md").read_bytes()
        report = compile_poc(self.inputs, self.output)
        self.assertEqual(set(report["projections"]), {"REDUCT-MAX", "BASE", "DEFESA"})
        ccp = read_json(self.output / "ccp.json")
        source_lines = before.decode().splitlines()
        for name in report["projections"]:
            bundle = read_json(self.output / (name + ".json"))
            for key, node in bundle["nodes"].items():
                span = node["provenance"]
                self.assertEqual(node["text"], "\n".join(source_lines[span["start_line"]-1:span["end_line"]]))
                self.assertEqual(node, ccp["nodes"][key])
                self.assertIn(ccp["source"]["commit"], span["url"])
            self.assertIn("candidata em revisão", bundle["nodes"]["state"]["text"])
            self.assertTrue(set(ccp["invariants"]) <= bundle["nodes"].keys())
        first = {p.name: p.read_bytes() for p in self.output.iterdir()}
        compile_poc(self.inputs, self.output)
        self.assertEqual(first, {p.name: p.read_bytes() for p in self.output.iterdir()})
        self.assertEqual(before, (self.inputs / "source.md").read_bytes())

    def test_source_tampering_fails_before_output(self):
        with (self.inputs / "source.md").open("a") as handle:
            handle.write("alteração")
        with self.assertRaisesRegex(ValidationError, "SHA-256"):
            compile_poc(self.inputs, self.output)
        self.assertFalse(self.output.exists())

    def test_invented_quote_fails(self):
        index = read_json(self.inputs / "markings.json")
        index["marks"][1]["quote"] = "conclusão não presente na fonte"
        self.rewrite("markings.json", index)
        with self.assertRaisesRegex(ValidationError, "quote mismatch"):
            compile_poc(self.inputs, self.output)

    def test_invalid_span_and_duplicate_node_fail(self):
        original = read_json(self.inputs / "markings.json")
        for mutation in ("span", "duplicate"):
            with self.subTest(mutation=mutation):
                index = copy.deepcopy(original)
                if mutation == "span":
                    index["marks"][0]["start_line"] = 0
                else:
                    index["marks"].append(index["marks"][0])
                self.rewrite("markings.json", index)
                with self.assertRaises(ValidationError):
                    structure(self.inputs)

    def test_omitting_limits_fails_even_when_declared_optional(self):
        contract = read_json(self.inputs / "projection-contract.json")
        spec = contract["projections"]["REDUCT-MAX"]
        spec["retain"].remove("limits")
        spec["allowed_omissions"].append("limits")
        self.rewrite("projection-contract.json", contract)
        with self.assertRaisesRegex(ValidationError, "required invariant omitted"):
            compile_poc(self.inputs, self.output)

    def test_unknown_node_and_wrong_defesa_axis_fail(self):
        ccp = structure(self.inputs)
        original = read_json(self.inputs / "projection-contract.json")
        for mutation in ("unknown", "axis"):
            with self.subTest(mutation=mutation):
                contract = copy.deepcopy(original)
                spec = contract["projections"]["DEFESA"]
                if mutation == "unknown":
                    spec["retain"].append("invented")
                else:
                    spec["axis"] = "editorial-density"
                with self.assertRaises(ValidationError):
                    validate_contract(ccp, contract)

    def test_unit_selection_and_single_projection(self):
        with self.assertRaisesRegex(ValidationError, "unknown unit"):
            compile_poc(self.inputs, self.output, unit="P9.9")
        report = compile_poc(self.inputs, self.output, projection="BASE", unit="P2.3")
        self.assertEqual(report["projections"], ["BASE"])
        self.assertFalse((self.output / "DEFESA.md").exists())

    def test_output_cannot_overwrite_preserved_inputs(self):
        for output in (self.inputs, self.inputs / "nested", self.inputs.parent):
            with self.subTest(output=output), self.assertRaises(ValidationError):
                compile_poc(self.inputs, output)


if __name__ == "__main__":
    unittest.main()
