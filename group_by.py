def group_by(keys, values):
    if len(keys) != len(values):
        raise ValueError("Both parameters must be lists of the same size")
    result = {}
    for i in range(len(keys)):
        if keys[i] in result:
            result[keys[i]] += values[i]
        else :
            result[keys[i]] = values[i]
    return result