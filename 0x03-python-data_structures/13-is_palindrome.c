#include "lists.h"
#include <stdio.h>
#include <stdbool.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 *
 *@head: pointer to pointer of first node of listint_t list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
*/
int is_palindrome(listint_t **head)
{
	listint_t *current, *repeat;
	int n, half, first, last; /* number of nodes */
	int cond1 = 0, cond2 = 0, wait = 0, cnt = 0;

	current = *head;
	repeat = *head;

	if (*head == NULL)
		return (1);

	n = 0;
	half = 0;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}
	current = *head;
	half = n / 2;
	if (n % 2 == 0 || n == 1 || n % 2 != 0)
	{
		first = 0, last = 0;
		while (true)
		{
			if (current != NULL)
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
					if (current->n == (*head)->n)
					{
						cond2 = 1;
					}
					else
						return (0);

				}
				last++;
			}
			first++;
			current = current->next;
			}
			else if (current == NULL && wait == 0)
			{
				current = *head;
				first = 0;
				last = n - 2;
				if (current == *head)
				{
					repeat = repeat->next;
					while(last != half)
					{
						current = current->next;
						cnt++;
						if (cnt > last)
						{
							if (current->n == repeat->n)
							{
								repeat = repeat->next;
								cnt = 0;
								last--;
							}
							else
								return (0);
						}
					}

				}
			}

		}
	}
	return (1);
}
