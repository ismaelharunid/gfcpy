
import sys, urllib.parse


prime_cache = [2, 3]

def iter_primes(i0=0, i1=None):
    if not isinstance(i0, int) or i0 < 0:
        ValueError("value expects an integer but found {:}".format(value))
    i = i0
    for p in prime_cache[i0:len(prime_cache) if i1 is None else i1]:
        yield p
        i += 1
    p = prime_cache[-1]
    while i1 is None or i < i1:
        p += 2
        for f in prime_cache:
            if p % f == 0:
                break
        else:
            prime_cache.append(p)
            yield p
            i += 1

def iprime(index):
    return iter_primes(index, index + 1).__next__()

def gfc(value, as_tuples=False):
    if not isinstance(value, int):
        ValueError("value expects an integer but found {:}".format(value))
    av = avalue = abs(value)
    factors = []
    if as_tuples:
        for p in iter_primes():
            if av < p:
                break
            n = 0
            while av % p == 0:
                n += 1
                av //= p
            if n > 0:
                factors.append((p, n))
        return factors or [(avalue, 1)]
    for p in iter_primes():
        if av == 1 or avalue < p:
            break
        while av % p == 0:
            factors.append(p)
            av //= p
    return factors or [avalue]

def sanity(i0=0, i1=10001):
    from numpy import prod
    for i in range(i0, i1):
        ps = gfc(i)
        print(i, ps)
        assert i == prod(ps), "we hate {:} with {:}".format(i, ps)
    return True

def print_factor_table(n_columns=7, n_rows=7, n_pages=1, n_start=1,
                       as_tuples=False,
                       table_selector="prime-table",
                       style_sheet=None):
    from numpy import sqrt, ceil
    #print(n_columns, n_rows, n_pages, n_start, as_tuples,
    #      table_selector, style_sheet)
    if n_rows is None:
        n_rows = max(1, int(sqrt(n_columns)))
        n_columns = int(ceil(n_columns / n_rows))
    items_per_page = n_rows * n_columns
    max_items = items_per_page * n_pages
    lines = ["""
<style>
table.{selector} {{
  width: -webkit-fill-available;
}}
table.{selector}, table.{selector} td {{
  border: 1px black solid;
}}
table.{selector} td * {{
  font-size: 18px;
}}
table.{selector} td sup {{
  font-size: 12px;
}}
table.{selector} span.number {{
  display: inline-block;
  text-align: right;
  width: 54px;
}}
table.{selector} span.number::after {{
  content: " =";
}}
table.{selector} span.factors {{
  padding-left: 9px;
}}
</style>
""".format(selector=table_selector)]
    if style_sheet is not None:
        lines.append("""<script src="{:}" async=""></script>\n"""
                     .format(urllib.parse.quote(style_sheet)))
    i, val = 0, n_start
    while i < max_items:
        if i % items_per_page == 0:
            lines.append('<table class="{selector}">\n<caption>Factors for {valstart} through {valstop}</caption><tr>'
                         .format(selector=table_selector,
                                 valstart=val,
                                 valstop=val + items_per_page - 1))
        elif i % n_columns == 0:
            lines.append('\n<tr>')
        factors = (' &times; '.join(str(n) for n in gfc(val))
                   if as_tuples else
                   ' &times; '.join("{:}<sup>{:}</sup>"
                                    .format(*nf)
                                    for nf in gfc(val, True)))
        lines.append(('<td><span class="number">{:}</span>'
                      '<span class="factors">{:}</span></td>')
                     .format(val, factors))
        i += 1
        val += 1
        if i % items_per_page == 0:
            lines.append('<tr>\n</table>\n')
        elif i % n_columns == 0:
            lines.append('</tr>\n')
    if i % items_per_page != 0:
        lines.append('</tr></table>\n')
    print(''.join(lines))
    return n_start + i

def main(*args, debug=False):
    """gfc -- v0.0 -- prints table of factors
    Usage:
        gfc n-columns [n-rows] [n-pages] [n_start] {extra-options}
            or
        gfc --n-columns=n [-n-rows=n] [--n-pages=n] [--n_start=n]
            or
        any variation of the above 2, positional arguments match the
        positions presented above.
    options:
        --n-columns=n       the number of columns in table.
        --n-rows=n          the number of rows in table.
        --n-pages=n         the number of table pages.
        --n-start=n         the number to start with (default: 1).
        --as-tuples=b       if True (default) then format as factors.
        --table-selector=s  the class selector name for the table(s).
        --style_sheet=s     a filepath or url of a stylesheet to include.
    """
    if any(name in ("-?", "-h", "--help") for name in args):
        print(main.__doc__)
        return 0
    args, kwargs = list(args), {}
    i_args = 0
    while i_args < len(args):
        if args[i_args].startswith('--'):
            kw, kwval = args.pop(i_args)[2:], False
            try:
                i = kw.index('=', 2)
            except ValueError:
                kw = kw.strip().replace('-', '_')
            else:
                kwval = kw[i+1:].strip()
                kw = kw[:i].strip().replace('-', '_')
            kwargs[kw] = kwval
        else:
            i_args += 1
    names = ("n_columns", "n_rows", "n_pages", "n_start",
             "as_tuples", "table_selector", "style_sheet")
    for name in names:
        if name not in kwargs and args:
            kwargs[name] = args.pop(0)
    unsupported = list(name for name in kwargs.keys() if name not in names)
    bad_values = []
    for name in names:
        if name in kwargs.keys():
            if name.startswith("n_"):
                try:
                    kwargs[name] = int(kwargs[name])
                except ValueError:
                    bad_values.append(name)
            elif name.startswith("as_"):
                try:
                    kwargs[name] = kwargs[name].lower() not in ("false", "0")
                except ValueError:
                    bad_values.append(name)
    msgs = []
    if not (args or unsupported or bad_values):
        if debug:
            print_factor_table(**kwargs)
            return 0
        else:
            try:
                print_factor_table(**kwargs)
            except Exception as msg:
                msgs.append(str(msg))
            else:
                return 0
    if args:
        print("excess positional arguments: {:}"
              .format(', '.join(args[2:])))
    if unsupported:
        print("unsupported keyword arguments: {:}"
              .format(', '.join(unsupported)))
    if bad_values:
        print("bad values for: {:}"
              .format(', '.join("{:}={:}".format(n, kwargs[n])
                                for n in bad_values)))
    for msg in msgs:
        print("error: {:}".format(msg))
    print(main.__doc__)
    return 1

if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
