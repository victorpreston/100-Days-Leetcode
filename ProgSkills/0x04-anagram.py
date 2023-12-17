#!/usr/bin/python3
class Solution:
	def isAnagram(self, s: str, t: str) -> bool
		"""
		:type s: str
		:type t: str
		:bool
		"""

		a = Counter(s)
		b = Counter(t)
		return a == b
