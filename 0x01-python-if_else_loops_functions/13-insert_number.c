#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>
/**
 * insert_node - inserts a number into a sorted singly linked list.
 *
 *@head: a double pointer pointing to the beginning of the listint_t list.
 *@number: a given number to be inserted.
 *
 * Return: the address of the new node, or NULL if it failed.
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;
	int start = 0;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		(*head) = new;
	else
	{
		while (current->next != NULL && current->next->n < number)
		{
			start = 1;
			current = current->next;
		}
		if (start == 0)
		{
			new->next = *head;
			return (new);
		}
		if (current->next == NULL)
			current->next = new;
		else
		{
			new->next = current->next;
			current->next = new;
		}
	}
	return (new);
}
