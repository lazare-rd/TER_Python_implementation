import pandas as pd

def main():
    df = pd.DataFrame({
        "keys" : ['A', 'A', 'B', 'C', 'A', 'C', 'B'],
        "values" : [2, 4, 8, 9, 5, 3, 1]
    })
    df.groupby("keys").sum()

if __name__ == '__main__':
    main()
    