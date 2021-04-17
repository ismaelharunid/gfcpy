# gfcpy

A prime, factor and factor table generator

Installation:

```
$ git clone https://github.com/ismaelharunid/gfcpy.git
$ cp gfc.py /home/<your-username>/<your-project>
```

Usage (as module):

```
>>> import gfc
>>> print("the 5th prime number is", gfc.iprime(5))
the 5th prime number is 13
>>> print("the 7th prime number is", gfc.iprime(7))
the 7th prime number is 17
>>> gfc.gfc(360, as_tuples=False)
[2, 2, 2, 3, 3, 5]
>>> gfc.gfc(360, as_tuples=True)
[(2, 3), (3, 2), (5, 1)]
>>> gfc.gfc(2310, as_tuples=True)
[(2, 1), (3, 1), (5, 1), (7, 1), (11, 1)]
```

Usage (command line):

```
$ python gfc.py --help
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
        --style-sheet=s     a filepath or url of a stylesheet to include.
        --md                print as markdown instead of html
```
