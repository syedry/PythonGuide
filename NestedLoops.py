domino=[1,2,3,4,5,6]
for left in domino:
    for right in domino:
        print("["+str(left)+"]["+str(right)+"]",end=" ")
    print()

"""The print() function writes a special character '/n' (represents newline) at the end.
When we include end=" " parameter, it takes a space instead of the newline character."""     