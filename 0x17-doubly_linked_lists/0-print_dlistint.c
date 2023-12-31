#include "list.h"

/**
 *
 * print_dlistint - print doubly-linked list
 * @h: address of head node
 *
 * Return: size of list
 */

size_t print_dlistint(const dlistint_t *h)
{

	size_t a = 0;

	while (h)
	{
		printf("%d/n", h->n);
		h = h->next;
		a++;
	}
	return(a)
}


