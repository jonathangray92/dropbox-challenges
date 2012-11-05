from sys import stdin 

def combinations(lst):
    """ Generator for all combinations of elements in input list. """
    for i in xrange(1,2**len(lst)):
        yield [lst[j] for j in xrange(len(lst)) if (1<<j)&i]

def main():
    """ Reads input from stdin, prints answer to stdout, and returns. """
    # Parse input
    lines = ''.join(stdin.readlines()).split('\n')
    splits = ( a.split(' ') for a in lines[1:] )    # generator
    parsed = [ (a[0], int(a[1])) for a in splits ]

    # Build lists 
    positive, negative = [], []
    for p in parsed:
        if p[1] > 0:
            positive.append(p)
        else:
            negative.append(p)

    # Find smaller list
    (smaller, larger) = (positive, negative) if len(positive) < len(negative) else (negative, positive)

    # Permute the smaller list
    for combo in combinations(smaller):
        calories = sum( a[1] for a in combo )
        for pcombo in combinations( [l for l in larger if abs(l[1]) < abs(calories)] ): # ignore elements with calorie count too big
            if sum( b[1] for b in pcombo ) + calories == 0:
                for ele in sorted( a[0] for a in combo+pcombo ):
                    print ele
                return 

    # No solution found
    print 'no solution'


if __name__ == '__main__':
    main()