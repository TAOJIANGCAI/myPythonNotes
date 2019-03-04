import sys
from operator import xor
from functools import reduce
from collections import Counter, deque
from time import time
import re
from itertools import combinations, product, groupby, zip_longest


def letterCasePermutation(S):
    """
    :type S: str
    :rtype: List[str]
    """
    res = ['']
    for ch in S:
        if ch.isalpha():
            res = [i + j for i in res for j in [ch.upper(), ch.lower()]]
        else:
            res = [i + ch for i in res]
    return res


def findTheDifference(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    # m = list(map(ord, s + t))
    # print(m)
    # r = reduce(xor, m)
    # print(r)
    # return chr(r)
    return list(Counter(t) - Counter(s))[0]


def detectCapitalUse(nums):
    """
    :type word: str
    :rtype: bool
    """
    temp = [i for i in range(1, len(nums) + 1)]

    return list(Counter(temp) - Counter(nums))


def majorityElement(nums):
    Counter(nums).elements()
    for num, i in Counter(nums).items():
        if i > len(nums) / 2:
            return num
    return 0


def titleToNumber(s):
    return sum(((ord(num) - 65 + 1) * (26 ** index) for index, num in enumerate(s[::-1])))


def isAnagram(s, t):
    return Counter(s) == Counter(t)


def containsDuplicate(nums):
    return Counter(nums) != Counter(set(nums))


def canConstruct(ransomNote, magazine):
    for i in set(ransomNote):
        if ransomNote.count(i) > magazine.count(i):
            return False
    return True


class Person(object):
    __slots__ = ('name', 'age')


class Girl(Person):
    pass


def isOneBitCharacter(bits):
    t = bits[:-1]
    res = [xor(i, 0) for i in t]
    if res == t and len(t) % 2 == 0:
        return True
    return False


def twoSum(numbers, target):
    dicts = {}
    for index, num in enumerate(numbers):
        if num in dicts:
            return [dicts.get(num), index + 1]
        else:
            dicts[target - num] = index + 1
    return None


def firstUniqChar(s):
    res = [s.index(i) for i in s if s.count(i) == 1]
    return min(res) if res else -1


def findShortestSubArray(nums):
    t = Counter(nums)
    first, last = {}, {}
    for index, num in enumerate(nums):
        first.setdefault(num, index)
        last[num] = index
    degree = max(t.values())
    return min(last[i] - first[i] + 1 for i in t if t[i] == degree)


def findRelativeRanks(nums):
    temp = sorted(nums)[::-1]
    rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(map(str, range(4, len(nums) + 1)))
    return list(map(dict(zip(temp, rank)).get, nums))


def longestPalindrome(s):
    odds = sum(i & 1 for i in Counter(s).values())
    return len(s) - odds + bool(odds)


def missingNumber(nums):
    nums = sorted(nums)
    n = len(nums)
    return (n + 1) * nums[0] + n * (n + 1) // 2 - sum(nums)


def findRestaurant(list1, list2):
    dicts = {}
    common = [i for i in list1 if i in list2]
    for i in common:
        dicts[i] = list1.index(i) + list2.index(i)
    return [i for i in dicts.keys() if dicts[i] == min(dicts.values())]


def intersect(nums1, nums2):
    a, b = map(Counter, (nums1, nums2))
    return list((a & b).elements())
    Counter.elements()


def maximumProduct(nums):
    # for i in product(nums):
    #     print(i)
    # return max(i[0] * i[1] * i[2] for i in combinations(nums, 3))
    nums.sort()
    return max(nums[-3] * nums[-2] * nums[-1], nums[0] * nums[1] * nums[-1])


def levelOrderBottom(root):
    stack = [(root, 0)]
    res = []
    while stack:
        node, level = stack.pop()
        if len(res) < level + 1:
            res.insert(0, [])
        if node:
            res[-(level + 1)].append(node.val)
            stack.append((node.right, level + 1))
            stack.append((node.left, level + 1))
    return res


def isLongPressedName(name, typed):
    return all(ch1 == ch2 and len(list(g1)) <= len(list(g2)) for ((ch1, g1), (ch2, g2)) in
               zip_longest(groupby(name), groupby(typed), fillvalue=(None, None)))


def binaryTreePaths(S, T):
    back = lambda x, y: x[:-1] if y == '#' else x + y
    return reduce(back, S, "") == reduce(back, T, "")


def isHappy(n):
    num = set()
    while n != 1:
        n = sum(int(i) ** 2 for i in str(n))
        if n in num:
            return False
        else:
            num.add(n)
    return True


def findLengthOfLCIS(nums):
    n = [1] * len(nums)
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            n[i] = n[i - 1] + 1
    return max(n)


def generate(numRows):
    # res = [[1]]
    # if numRows == 0:
    #     return []
    # elif numRows == 1:
    #     return res
    # elif numRows == 2:
    #     res.append([1, 1])
    #     return res
    # else:
    #     res.append([1, 1])
    #     for i in range(2, numRows):
    #         temp = []
    #         for t in zip(res[i - 1], res[i - 1][1:]):
    #             temp.append(t[0] + t[1])
    #         temp.insert(0, 1)
    #         temp.append(1)
    #         res.append(temp)
    res = [[1]]
    for i in range(1, numRows):
        res.append(list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1])))
    return res


def nextGreatestLetter(letters, target):
    for i in letters:
        if ord(i) > ord(target):
            return i
    return letters[0]


def longestWord(words):
    valid = set([""])

    for word in sorted(words, key=lambda x: len(x)):
        if word[:-1] in valid:
            valid.add(word)

    print(valid, sorted(valid))
    valid.add('appla')
    return max(sorted(valid), key=lambda x: len(x))

    # sets = set([""])
    # words.sort()
    # print(words)
    # for i in words:
    #     if i[:-1] in sets:
    #         sets.add(i)
    # return max(sorted(sets, key=lambda x: len(x)))


def removeElement(nums, val):
    first = {}
    last = {}
    for val, index in enumerate(nums):
        first.setdefault(val, index)
        last[val] = index


def climbStairs(n):
    if n == 1:
        return 1
    a, b = 1, 2
    for i in range(2, n):
        tmp = b
        b = a + b
        a = tmp
    return b


def addStrings(num1, num2):
    n1, n2 = list(num1), list(num2)
    res, carry = [], 0
    while len(n1) > 0 or len(n2) > 0:
        a1 = ord(n1.pop()) - ord('0') if len(n1) > 0 else 0
        a2 = ord(n2.pop()) - ord('0') if len(n2) > 0 else 0

        temp = a1 + a2 + carry

        res.append(temp % 10)
        carry = temp // 10
    if carry:
        res.append(carry)
    return ''.join(str(i) for i in res[::-1])


def findLHS(nums):
    # res = []
    # for num in nums:
    #     temp = []
    #     if (num + 1) in nums:
    #         temp = [num] * nums.count(num) + [num + 1] * nums.count(num + 1)
    #         res.append(temp)
    # return max([len(i) for i in res])
    dicts = Counter(nums)
    return max([dicts[count] + dicts[count + 1] for count in dicts if count + 1 in dicts] or [0])


def isPowerOfTwo(n):
    i, t = 0, n
    while t:
        t = t // 3
        i += 1
    if 3 ** (i - 1) == n:
        return True
    else:
        return False


def mostCommonWord(paragraph, banned):
    res = re.split(r'[ ,.]', paragraph)
    t = [i.lower() for i in res if i and i.lower() not in banned]

    return Counter(t).most_common(1)[0][0]


def getRow(rowIndex):
    res = [[1]]
    for i in range(1, rowIndex + 1):
        res.append([map(lambda x, y: x + y, res[-1] + [0], 0 + res[-1])])
    return res[-1]


def reverseVowels(s):
    # li = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    # indexs = []
    # for index, num in enumerate(s):
    #     if num in li:
    #         indexs.append(index)
    # l = len(indexs)
    # res = list(s)
    # if l % 2 == 0:
    #     n = l // 2
    #     for i in range(n):
    #         res[indexs[i]], res[indexs[l - 1 - i]] = res[indexs[l - 1 - i]], res[indexs[i]]
    # else:
    #     n = l // 2
    #     for i in range(n + 1):
    #         res[indexs[i]], res[indexs[l - 1 - i]] = res[indexs[l - 1 - i]], res[indexs[i]]
    #
    # return ''.join(res)
    vowels = re.findall(r'[aeiou]', s, flags=re.IGNORECASE)

    return re.sub(r'(?i)([aeiou])', lambda m: vowels.pop(), s)


def isPalindrome(x):
    if x < 0:
        return False
    p, res = x, 0
    while x:
        res = res * 10 + x % 10
        x = x // 10

    return res == p


def plusOne(digits):
    # digits.reverse()
    # l = len(digits)
    # if (digits[0] + 1) == 10:
    #     digits[0] = 0
    #     temp = 1
    #     if l == 1:
    #         digits.append(temp)
    #     for i in range(1, l):
    #         if (digits[i] + temp) == 10:
    #             digits[i] = 0
    #             temp = 1
    #             if i == (l - 1):
    #                 digits.append(temp)
    #         else:
    #             digits[i] = digits[i] + temp
    #             temp = 0
    # else:
    #     digits[0] += 1
    #
    # digits.reverse()
    # return digits

    nums = 0
    l = len(digits)
    for i in range(l):
        nums += digits[i] * (10 ** (l - i - 1))
    return [int(i) for i in str(nums + 1)]


def isUgly(num):
    for i in 2, 3, 5:
        while num % i == 0 < num:
            num /= i
    return num == 1


def cla(*nums):
    sum = 0
    for i in nums:
        sum += i
    return sum


def person(name, age, **kwargs):
    print(name, age, kwargs)


def student(name, age, *kw, city, height):
    print(name, age, kw, city, height)


def searchInsert(nums, target):
    # if target in nums:
    #     return nums.index(target)
    # else:
    #     nums.append(target)
    #     nums.sort()
    #     return nums.index(target)
    return len([x for x in nums if x < target])


def findErrorNums(nums):
    return [sum(nums) - sum(set(nums)), sum(range(1, len(nums) + 1)) - sum(set(nums))]


def dominantIndex(nums):
    m = max(nums)
    for i in nums:
        if m < 2 * i and i != m:
            return -1
    return nums.index(m)


def pivotIndex(nums):
    left, right = 0, sum(nums)
    for index, num in enumerate(nums):
        right -= num
        if left == right:
            return index
        left += num

    return -1


def licenseKeyFormatting(S, K):
    S = S.upper().replace("-", "")[::-1]
    size = len(S)
    times = size // K if size % K == 0 else size // K + 1
    res = []
    for i in range(times):
        res.append(S[K * i:K * (i + 1)][::-1])
    res.reverse()
    return "-".join(res)


def isPerfectSquare(num):
    i = 1
    while num > 0:
        num -= i
        i += 2
    return num == 0


def findMaxAverage(nums, k):
    # l = len(nums)
    # if l <= k:
    #     return sum(nums) / l
    # else:
    #     m = 0
    #     for i in range(0, l - k + 1):
    #         su = sum(nums[i:k + i]) / k
    #         if su > m:
    #             m = su
    #     return m
    m = sum(nums[:k])
    temp = m
    for i in range(len(nums) - k):
        temp = temp - nums[i] + nums[i + k]
        if temp > m:
            m = temp
    return m / k


def lengthOfLongestSubstring(s):
    # res = []
    # temp = []
    # temp.append(s[0])
    # start = 0
    # for i in range(1, len(s)):
    #     if s[i] in temp and start <=
    #         res.append(temp)
    #         temp = []
    #         temp.append(s[i])
    #     else:
    #         temp.append(s[i])
    # res.append(temp)
    # m = 0
    # for i in res:
    #     t = len(i)
    #     if t > m:
    #         m = t
    # print(res, m)

    # for i in range(len(s)):
    #     if s[i] in usedChar and start <= usedChar[s[i]]:
    #         start = usedChar[s[i]] + 1
    #     else:
    #         maxLength = max(maxLength, i - start + 1)
    #
    #     usedChar[s[i]] = i
    #
    # return maxLength

    start = maxlength = 0
    usedDict = {}
    for i, num in enumerate(s):
        if num in usedDict and start <= usedDict[num]:
            start = usedDict[num] + 1
        else:
            maxlength = max(maxlength, i - start + 1)
        usedDict[num] = i
    return maxlength


# 1,2,3,4
def findMedianSortedArrays(nums1, nums2):
    nums = nums1 + nums2
    nums.sort()
    l = len(nums)
    if l % 2 != 0:
        return float(nums[l // 2])
    else:
        return float((nums[l // 2] + nums[l // 2 - 1]) / 2)


def longestCommonPrefix(strs):
    if not strs:
        return ""
    for index, num in enumerate(zip(*strs)):
        if len(set(num)) > 1:
            return strs[0][:index]
    else:
        return min(strs)


def translate(string):
    li = []
    i = 0
    while True:
        if i == 4:
            li.append(string[i:i + 4])
            i += 4
        else:
            li.append(string[i:i + 2])
            i += 2
        if i >= len(string):
            break

    print(li)


s = ['01', '21', '07d2', '00', 'c0', 'a8', '00', '19']
{"AMR": 1, "F2": 1, "F1": 1, "T4": 1, "T3": 1, "T2": 1, "T1": 1}
li = []
if s[0] == "01":
    li.append("BR1")
else:
    li.append("BR2")
temp = ""
for i in bin(int(s[1], 16))[2:]:
    pass

li.append(str(int(s[2], 16)))
li.append(s[3])
li.append(".".join([str(int(i, 16)) for i in s[4:]]))
print(li)
