from primes import SearchPrimes


def main():
    """ Main script
    If you want to try out this program, run and edit here.
    """
    sp = SearchPrimes()

    result = sp.is_prime(136363636361)["comment"]
    print(result)


if __name__ == "__main__":
    main()