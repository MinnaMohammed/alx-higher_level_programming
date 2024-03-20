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
	unsigned int n, half, first, last; /* number of nodes */
	int cond1 = 0, cond2 = 0;

	current = *head;

	if (*head == NULL)
		return (1);

	n = 0;
	half = 0;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}
	half = n / 2;

	if (n % 2 == 0 || n == 1)
	{
		first = 0, last = 0;
		while (current != NULL)
		{
			if (first == half - 1)
			{
				if (current->n == current->next->n)
					cond1 = 1;
				else
					return (0);
			}
			else if (cond1 == 1 && cond2 == 0)
			{
				if (last == half - 1)
				{
					if (current->next->n == (*head)->n)
						cond2 = 1;
					else
						return (0);

				}
				last++;
			}
			first++;
			current = current->next;
		}
	}
	else
		return (0);
	return (1);
}
