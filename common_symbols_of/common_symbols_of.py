import sys
import getopt

def string_to_list(str):
    lst = []
    str_pure = str
    for sym in str_pure:
        lst.append(sym)
    return lst

def bubble_sort(str):
    str_sorted = string_to_list(str)
    length = len(str)
    is_sorted = False
    while is_sorted == False:
        is_sorted = True
        for i in range (0, length - 1):
            if str_sorted[i] > str_sorted[i+1]:
                buf = str_sorted[i]
                str_sorted[i] = str_sorted[i+1]
                str_sorted[i+1] = buf
                is_sorted = False
    str_sorted = "".join(str_sorted)
    return str_sorted


def distinct_on_symbols_of(str):
    distinct_symbols = ""
    for sym in str:
        if distinct_symbols.find(sym) == -1:
            distinct_symbols = "%s%s" % (distinct_symbols, sym)
            distinct_symbols = bubble_sort(distinct_symbols)
    return distinct_symbols


def common_symbols_of(a, b):
    distinct_symbols = ""
    if (len(a) < len(b)):
        distinct_symbols = distinct_on_symbols_of(a)
        common = ""
        for sym in distinct_symbols:
            if b.find(sym) != -1:
                common = "%s%s" % (common, sym)
    else:
        distinct_symbols = distinct_on_symbols_of(b)
        common = ""
        for sym in distinct_symbols:
            if a.find(sym) != -1:
                common = "%s%s" % (common, sym)
    return common


def main():
    a = "askdjfp9283rj9jf[2213v23]v12v5]1v2[]15v12b3[5]2p45pb2p315bp123ov5p12o3[c512345c123c4- "
    b = "]2vj125v12vjvp12jv1234v2v3nq4bb[5ib902ubm 5qbm9m5w c8ewq -89 -98 sa980df80 hsa0 a8a8 s0d7f h8a s0h"
    print repr(common_symbols_of(a, b))


if __name__ == "__main__":
    main()