t = int(input())

for _ in range(t):
    a, b = input().strip().split()
    l1,l2 = len(a), len(b)
    s1, s2 = a[-1], b[-1]
    size = "SML"
    if s1 != s2:
        # size is different
        if size.find(s1) > size.find(s2):
            print(">")
        elif size.find(s1) < size.find(s2):
            print("<")
    else:
        # size is same
        if l1 == l2:
            print("=")
        elif l1 > l2:
            if s1 == "S":
                print("<")
            else:
                print(">")
        else:
            if s1 == "S":
                print(">")
            else:
                print("<")