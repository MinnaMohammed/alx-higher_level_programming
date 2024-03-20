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
	unsigned int n; /* number of nodes */

	current = *head;

	if (*head == NULL)
		return (1);

	n = 0;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}

	if (n % 2 == 0)
		return (1);
	else
		return (0);
	return (1);
}
