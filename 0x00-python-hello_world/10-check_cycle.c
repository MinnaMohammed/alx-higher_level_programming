#include "lists.h"
#include <stdio.h>
/**
 * check_cycle: checks if a singly linked list has a cycle in it.
 *
 *@list: given singly linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *current;
	current = list;

	if (list ==  NULL)
		return (0);
	else
	{
		if (list->next == NULL)
		{
			return (0);
		}
		else
		{
			if (current-> next == list)
				return (1);
			else
			{
				return (0);

			}
			return (1);
		}
	}
	return (0);
}
