def solution(s):
    num_dict = {"zero":0, "one": 1, "two":2, "three":3, "four":4, "five":5, "six":6,
           "seven":7, "eight":8, "nine":9}
    max_len = 50
    for k in num_dict:
        s=s.replace(k, str(num_dict[k]))
    return int(s)
