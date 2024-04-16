t = int(input())

for _ in range(t):
    missing = ""
    for i in range(3):
        s = input().strip()
        
        if missing == "":
            if "A" not in s:
                missing = "A"
            elif "B" not in s:
                missing = "B"
            elif "C" not in s:
                missing = "C"

    print(missing)