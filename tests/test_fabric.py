import unittest

from aoc2018.fabric import Claim, ClaimChecker


class TestClaim(unittest.TestCase):
    def test_create_claim_from_str(self):
        claim = Claim.from_str("#14 @ 12,38: 40x57")
        self.assertEqual(claim.id, "14")
        self.assertEqual(claim.start, (12, 38))
        self.assertEqual(claim.width, 40)
        self.assertEqual(claim.height, 57)

    def test_squares(self):
        claim = Claim.from_str("#1 @ 1,3: 2x3")
        squares = list(s for s in claim.squares)
        expected = [(1, 3), (2, 3), (1, 4), (2, 4), (1, 5), (2, 5)]
        self.assertEqual(expected, squares)


class TestClaimChecker(unittest.TestCase):
    def test_counts_multiply_claimed_squares(self):
        claims = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
        checker = ClaimChecker(claims)
        self.assertEqual(checker.claimed_by_multiple(), 4)

    def test_finds_non_overlapping_claims(self):
        claims = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
        checker = ClaimChecker(claims)
        self.assertEqual(["3"], checker.nonoverlapping())
