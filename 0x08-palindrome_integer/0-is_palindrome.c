#include <stdlib.h>
#include <stdio.h>
#include "palindrome.h"


/**
 * is_palindrome - function that checks whether
 * or not a given unsigned integer is a palindrome.
 * @n: the number to validate if it is a palindrome.
 * Return: 1 if the number is a palindrome, 0 If this is not.
 **/

int is_palindrome(unsigned long n)
{
	unsigned long num = n;
	unsigned long num_reverse = 0;
	unsigned long last_digit = 0;

	while (num != 0)
	{
		last_digit = num % 10;
		num_reverse *= 10;
		num_reverse += last_digit;
		num /= 10;
	}
	if (num_reverse == n)
	{
		return (1);
	}
	else
	{
		return (0);
	}
}
