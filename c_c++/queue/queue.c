#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int value;
    struct Node *next;
};

struct Node *head = NULL;
struct Node *tail = NULL;
int length = 0;

int peak()
{
    return head->value;
}

void enqueue(int value)
{
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    newNode->value = value;
    newNode->next = NULL;

    if (head == tail)
    {
        head = tail = newNode;
        return;
    }

    tail->next = newNode;
    tail = newNode;
}

int dequeue()
{
    if (head == NULL)
    {
        return -1;
    }

    struct Node *temp = head;
    int value = temp->value;

    if (head == tail)
    {
        head = tail = NULL;
    }
    else
    {
        head = head->next;
    }

    free(temp);
    length--;

    return value;
};

int main()
{
    enqueue(5);
    printf("%d\n", head->value);
}