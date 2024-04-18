t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    st = set()

    for i in range(n - 1):
        st.add(s[i:i + 2])

    print(len(st))