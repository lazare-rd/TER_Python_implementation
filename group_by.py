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

def main():
    keys = ['A', 'A', 'B', 'C', 'A', 'C', 'B']
    values = [2, 4, 8, 9, 5, 3, 1]
    print(group_by(keys, values))

if __name__ == '__main__':
    main()
    