def main(nums, end=2020):
    last_seen = {v: i+1 for (i, v) in enumerate(nums[:-1])}

    t = len(nums)
    v = nums[-1]
    while t < end:
        if v not in last_seen:
            last_seen[v] = t
            v = 0
        else:
            last_seen[v], v = t, t - last_seen[v]
        t += 1

    return v

def test():
    assert main([0,3,6], 10) == 0
    assert main([0,3,6]) == 436
    assert main([1,3,2]) == 1
    assert main([2,1,3]) == 10
    assert main([1,2,3]) == 27
    assert main([2,3,1]) == 78
    assert main([3,2,1]) == 438
    assert main([3,1,2]) == 1836

if __name__ == "__main__":
    test()
    res = main([2,20,0,4,1,17])
    print(res)