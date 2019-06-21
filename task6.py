a = str(input())


def reverse(a):
    w = a.split(" ")
    ww = [bb[::-1] for bb in w]
    ss = " ".join(ww)
    return ss


print(reverse(a))
