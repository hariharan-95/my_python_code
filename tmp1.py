def test(s, ch):
    new_str = []
    l = len(s)

    for i in range(len(s)):
        if (s[i] == ch and i != (l - 1) and
                i != 0 and s[i + 1] != ch and s[i - 1] != ch):
            new_str.append(s[i])

        elif s[i] == ch:
            if ((i != (l - 1) and s[i + 1] == ch) and
                    (i != 0 and s[i - 1] != ch)):
                new_str.append(s[i])

        else:
            new_str.append(s[i])

    return ("".join(i for i in new_str))

print(test("Hariharan","a"))