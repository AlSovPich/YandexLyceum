def eratosthenes(N):
    nums = []
    matched_num = []
    string = []
    for n in range(N + 1):
        if n >= 2:
            nums.append(n)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j] not in matched_num and nums[j] != nums[i] and nums[j] % nums[i] == 0:
                matched_num.append(nums[j])
                string.append(nums[j])
    print(" ".join(map(str, string)))

eratosthenes(15)
