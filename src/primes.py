class SearchPrimes():
    """[summary]
    """

    def is_prime_brute_force(self, num, look_progress = False):
        """ *fix docs* find a number a prime or not using brute force

        Args:
            num (int): number

        Returns:
            dict: 
                is_prime (bool) : True if its a prime, False if not.
                comment (str): comments
        """

        if num < 2:
            return {"is_prime":False, "comment": f"{num} is not prime"}

        for i in range(2,num):
            if num % i == 0:
                comment = f"{num} is not prime because it is divisible by {i} \n{num} = {i} x {num // i}"
                return {"is_prime":False, "comment": comment}
        
        return {"is_prime":False, "comment": f"{num} is a prime number"}

    def is_prime_brute_force_sqrt(self, num, look_progress = False):
        """ *fix docs* find a number a prime or not using brute force
        with square root to reduce computation

        Args:
            num (int): number
            look_progress: Bool

        Returns:
            dict: 
                is_prime (bool) : True if its a prime, False if not.
                comment (str): comments
        """
        if num < 2:
            return {"is_prime":False, "comment": f"{num} is not prime"}

        root_num = int(((num)**(1/2) + 1) // 1)

        for i in range(2,root_num):
            if num % i == 0:
                comment = f"{num} is not prime because it is divisible by {i} \n{num} = {i} x {num // i}"
                return {"is_prime":False, "comment": comment}
        
        return {"is_prime":False, "comment": f"{num} is a prime number"}

    def is_prime(self, num, method="sqrt_brute_force", look_progress = False):
        """Main function to determine whether a number is prime or not.

        Args:
            num (int): number to determine whether it is prime or not
            method (str, optional): method of find if its prime or not. Defaults to "brute_force".

        Returns:
            dict: 
                is_prime (bool) : True if its a prime, False if not.
                comment (str): comments
        """
        if method == "brute_force":
            return self.is_prime_brute_force(num, look_progress = look_progress)
        elif method == "sqrt_brute_force":
            return self.is_prime_brute_force_sqrt(num, look_progress = look_progress)
        else:
            return {"is_prime":None, "comment":"Nothing in there"}

            