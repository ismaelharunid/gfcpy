# gfcpy

A factor and factor table generator

```
$ python pfc.py --help
gfc -- v0.0 -- prints table of factors
    Usage:
        gfc n-columns [n-rows] [n-pages] [n_start] {extra-options}
            or
        gfc --n-columns=n [-n-rows=n] [--n-pages=n] [--n_start=n]
            or
        any variation of the above 2, positional arguments match the
        positions presented above.
    Options:
        --n-columns=n       the number of columns in table.
        --n-rows=n          the number of rows in table.
        --n-pages=n         the number of table pages.
        --n-start=n         the number to start with (default: 1).
        --as-tuples=b       if True (default) then format as factors.
        --table-selector=s  the class selector name for the table(s).
        --style_sheet=s     a filepath or url of a stylesheet to include.
        --md                print as markdown instead of html
```
