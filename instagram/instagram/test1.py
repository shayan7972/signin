def vector_length(v: object) -> object:
    import math
    s=0
    for d in v:
        s+=d*d
    s=math.sqrt(s)
    return s
print(vector_length([4  ,3,]))

