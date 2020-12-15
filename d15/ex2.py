def main(nums, end=30000000):
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
    assert main([0,3,6]) == 175594
    assert main([1,3,2]) == 2578
    assert main([2,1,3]) == 3544142
    assert main([1,2,3]) == 261214
    assert main([2,3,1]) == 6895259
    assert main([3,2,1]) == 18
    assert main([3,1,2]) == 362


if __name__ == "__main__":
    #test()
    res = main([2,20,0,4,1,17])
    print(res)
