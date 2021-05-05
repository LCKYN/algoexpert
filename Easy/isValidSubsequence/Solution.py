def isValidSubsequence(a, s):
	count_a = 0
	count_s = 0
	while(count_a < len(a)):
		if(a[count_a] == s[count_s]):
			count_s += 1
			
		count_a += 1
		
		if(count_s == len(s)):
			return True
		
	return False
