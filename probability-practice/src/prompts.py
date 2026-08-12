FIX_LATEX_PROMPT = """
Replace all "\\[" and "\\]" from the LaTeX in the following text with "$$" or if it's inline "$".

EXAMPLES:
BAD:
```
\\[
33\\cdot 32\\cdot 31\\cdot 30\\cdot 29\\cdot 28\\cdot 27\\cdot 26\\cdot 25
= 13\\,995\\,229\\,248\\,000
\\]
```
GOOD:
```
$$
33\\cdot 32\\cdot 31\\cdot 30\\cdot 29\\cdot 28\\cdot 27\\cdot 26\\cdot 25
= 13\\,995\\,229\\,248\\,000
$$
```

BAD:
```
\\[
\binom{33}{9}= \frac{13\\,995\\,229\\,248\\,000}{362\\,880}=115\\,701\\,300
\\]
```

GOOD:
```
$$
\binom{33}{9}= \frac{13\\,995\\,229\\,248\\,000}{362\\,880}=115\\,701\\,300
$$
```

BAD:
```
\\[
\boxed{115\\,701\\,300}
\\]
```

GOOD:
```
$\boxed{115\\,701\\,300}$
```
"""
