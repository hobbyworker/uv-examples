import sys
from collections import Counter
def count_words(text:str)->Counter[str]:
    words=[w.strip(".,!?\"'()").lower() for w in text.split()]
    return Counter(w for w in words if w)
def main()->None:
    paths=sys.argv[1:]
    for path in paths:
        with open(path,encoding="utf-8") as f: counts=count_words(f.read())
        total=sum(counts.values())
        print(path+": "+total+" words")
        for word,n in counts.most_common(3): print(f"  {word:<10} {n}")
