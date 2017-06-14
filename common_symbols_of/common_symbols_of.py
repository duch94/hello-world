import sys
import getopt


def distinct_on_symbols_of(str):
    distinct_symbols = ""
    for sym in str:
        if distinct_symbols.find(sym) == -1:
            distinct_symbols = "%s%s" % (distinct_symbols, sym)
            #distinct_symbols = bubble_sort(distinct_symbols)
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
    a = "askdjfp9283rj9jf[2213\v\23]v\12v5\]1v2[]\15v\12b3[5\]2p45p\b2p315bp123ov5p12o3[c5\1234\5c1\23c4"
    b = "]2vj12\5v\12\v\jvp12jv123\4\v2v3\n\\\q4bb[5ib902ubm 5qbm9m5w c8ewq -89 -98 sa980df80 hsa0 a8a8 s0d7f h8a s0h"
    print repr(common_symbols_of(a, b))


if __name__ == "__main__":
    main()