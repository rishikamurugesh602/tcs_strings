def min_stack():
    n = int(input())

    stack = []
    minstack = []
    output = []

    for _ in range(n):

        arr = input().split()

        if arr[0] == "PUSH":
            x = int(arr[1])
            stack.append(x)

            if not minstack or x <= minstack[-1]:
                minstack.append(x)

        elif arr[0] == "POP":

            if not stack:
                output.append("empty")
            else:
                val = stack.pop()
                output.append(val)

                if minstack and val == minstack[-1]:
                    minstack.pop()

        elif arr[0] == "MIN":

            if not minstack:
                output.append("empty")
            else:
                output.append(minstack[-1])

    for x in output:
        print(x)

min_stack()
