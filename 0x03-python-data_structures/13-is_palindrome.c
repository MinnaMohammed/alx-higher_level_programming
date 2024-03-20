#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 *
 *@head: pointer to pointer of first node of listint_t list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
*/
int is_palindrome(listint_t **head)
{
	listint_t *current;
	unsigned int n, values; /* number of nodes */
	int sum1 = 0, sum2 = 0;

	current = *head;

	if (*head == NULL)
		return (1);

	n = 0;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}

	if (n % 2 == 0 || n == 1)
	{
		values = 0;
		while (current != NULL)
		{
			if (values < (n / 2))
				sum1 += current->n;
			else
				sum2 += current->n;
			current = current->next;
			values++;
		}
		if (sum1 == sum2)
			return (1);
		else
			return (0);
	}
	else
		return (0);
	return (1);
}
