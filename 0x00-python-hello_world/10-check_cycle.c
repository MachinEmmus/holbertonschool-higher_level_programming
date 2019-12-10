#include "lists.h"
/**
 *
 *
 *
 */

int check_cycle(listint_t *head)
{
	listint_t *hare = head;
	listint_t *turtle = head;
	
	if (!head)
		return (0);

	while(turtle->next && hare->next->next)
	{
		turtle = turtle->next;
		hare = hare->next->next;
		if (turtle == hare)
			return (1);
	}
	return (0);
}
