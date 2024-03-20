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


	if (*head == NULL)
		return (1);
	
	current = *head;
	repeat = *head;
	n = 0;
	half = 0;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}
	current = *head;
	half = n / 2;
	if (n == 1)
		return (1);
	if (n % 2 == 0 || n % 2 != 0)
	{
		first = 0, last = 0;
		while (true)
		{
			if (current != NULL)
			{
			if (first == half - 1)
			{ 

				if ((n % 2 == 0 && current->n == current->next->n) || (n % 2 != 0 && current->n == current->next->next->n))
				{
					cond1 = 1;
				}
				else
					return (0);
			}
			else if (cond1 == 1 && cond2 == 0 && current->next == NULL)
			{
				if (last == half - 1)
				{
					if (current->n == (*head)->n)
					{
						cond2 = 1;
						printf("first: %d head: %d\n", current->n, (*head)->n);
					}
					else
					{
						printf("last element: %d\n", current->n);
						printf("hello\n");
						return (0);
					}

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
						cnt++;
						current = current->next;
						if (cnt >= last)
						{
							if (current->n == repeat->n)
							{
								current = *head;
								repeat = repeat->next;
								cnt = 0;
								last--;
							}
							else
								return (0);
						}
					}
					return (1);

				}
			}

		}
	}
	return (1);
}
