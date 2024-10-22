from SLLNCStack import Stack
import math

def mergeStacksInterleave(stack1: Stack, stack2: Stack) -> Stack:
    merged_stack = Stack(stack1,stack2)

    return merged_stack
    
if __name__ == "__main__":
    s1 = Stack()
    # Isi Stack 1
    s1.push(1)
    s1.push(3)
    s1.push(5)

    s2 = Stack()
    # Isi Stack 2
    s2.push(2)
    s2.push(4)
    s2.push(6)

    s3 = mergeStacksInterleave(s1,s2)
    s3.printAll()