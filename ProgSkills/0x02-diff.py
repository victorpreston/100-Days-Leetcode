#!/usr/bin/python3
class Solution:
	def findTheDifference(self, s: str, t: str) -> str:
		count = {}
		"""Dictionary to count the frequency of chars"""
	
		for char in s:
			if char not in count:
				count[char] = 1
			else:
				count[char] += 1

		for char in t:
			if char not in count or count[char] == 0:
				return char
			else:
				count[char] -= 1
		return "Error: added character not found"
