def is_square(n):
    # need to confirm is positive (also removes lots of error inducing stress) and need to confirm that the square root is an integer equivalent to the square root of the number
    return n >= 0 and n**(1/2)==int(n**(1/2))

def main():
    n = -4
    answer = is_square(n)
    print(answer)

if __name__ == '__main__':
    main()