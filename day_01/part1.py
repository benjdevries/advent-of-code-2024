def main():
    
    left = []
    right = []
    diff = 0
    
    with open("input.txt") as f:
        for line in f:
            l, r = line.split()
            left.append(int(l))
            right.append(int(r))
            
    left.sort()
    right.sort()
    
    for l, r in zip(left, right):
        diff += abs(l - r)
        print(diff)
    

if __name__ == "__main__":
    main()