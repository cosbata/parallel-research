import unittest

from research_mode import infer_research_mode, max_sources_for_mode


class ResearchModeTest(unittest.TestCase):
    def test_explicit_depth_wins(self):
        self.assertEqual(infer_research_mode("출처를 검증해줘", "deep"), "deep")

    def test_verification_has_priority_over_deep_keywords(self):
        self.assertEqual(infer_research_mode("학술 논문으로 출처 검증해줘"), "verify_sources")

    def test_source_limits_are_bounded(self):
        self.assertEqual(max_sources_for_mode("fast"), 6)
        self.assertEqual(max_sources_for_mode("deep"), 10)
        self.assertEqual(max_sources_for_mode("unknown"), 8)


if __name__ == "__main__":
    unittest.main()
