from dataclasses import dataclass

@dataclass
class RecursionSnippets:
    def factorial(self, n: int = 1)->int:
        """Return the factorial of a given number."""
        if n == 1:
            return 1
        else:
            return n * factorial_rec(n-1)
