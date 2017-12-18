def get_prefix_table(pattern):
    table = [0]
    pattern_length = len(pattern)
    for i in range(1, pattern_length):
        j = 0
        while pattern[i] == pattern[j]:
            j += 1
            # j < pattern_length:
            # if :
            # if j == pattern_length:
            # else:
        table.append(j)
    return table


def substring_index(needle, haystack):
    prefix_table = get_prefix_table(needle)
    haystack_length = len(haystack)
    j = 0
    for i in range(haystack_length):
        while j > 0 and needle[j] != haystack[i]:
            j = prefix_table[j - 1]
        if needle[j] == haystack[i]:
            j += 1
            if len(needle) == j:
                yield i - (j - 1)
                i = i - (j - 1) + 1
                j = prefix_table[j - 1]
    return None

tests = [("TEST", "THIS IS A TEST TEXT"), ("ANA", "BANANA")]
for test in tests:
    for occurrence in substring_index(*test):
        print("Found {0} at {1} position".format(test[0], occurrence))
