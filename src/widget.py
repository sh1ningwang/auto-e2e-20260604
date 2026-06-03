"""Tiny widget module — seed-signal fixture for /auto --seed."""


def add(a, b):
    # TODO: validate that a and b are numbers before adding
    return a + b


def rounding(x):
    # FIXME: rounding is biased for .5 cases; use banker's rounding
    return int(x + 0.5)


def legacy_path(p):
    # HACK: strip trailing slash by hand instead of using os.path
    return p[:-1] if p.endswith("/") else p


def parse(s):
    # XXX: this parser does not handle escaped quotes
    return s.split(",")
