def countingBob(string_check):
    n_bobs = 0
    string_len = len(string_check) - 2
    i = 0
    while i < string_len:
        print string_check[i:]
        if string_check[i] == 'b':
            if string_check[i + 1] == 'o':
                if string_check[i + 2] == 'b':
                    n_bobs += 1
        i += 1
        print "Number of times 'bob' occurs is: ", n_bobs


print countingBob('obobobobbfobooboboboboreboboboboobboboboboboj')
