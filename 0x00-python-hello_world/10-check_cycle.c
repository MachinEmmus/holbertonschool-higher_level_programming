#include "lists.h"
/**
 * check_cycle - check if a loop is infinity
 * @head: is the head of my linked list
 * Return: 0 is not loop, 1 is a loop
 */

int check_cycle(listint_t *head)
{
	listint_t *hare = head;
	listint_t *turtle = head;

	while (head && turtle->next && hare->next->next)
	{
		hare = hare->next->next;
		turtle = turtle->next;
		if (turtle == hare)
			return (1);
	}
	return (0);
}
