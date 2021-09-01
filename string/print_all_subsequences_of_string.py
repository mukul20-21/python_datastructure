def printSubsequence(input, output,res):

    # Base Case--if the input is empty print the output string
    if len(input) == 0:
        res.append(output)
        return

    # output is passed with including the 1st characther of input string
    printSubsequence(input[1:], output+input[0],res)

    # output is passed without including the 1st character of input string
    printSubsequence(input[1:], output,res)


# Driver code
# output is set to null before passing in as a parameter
if __name__ == "__main__":
    out = ""
    inp = input()
    res = []
    printSubsequence(inp, out,res)
    print(res)
