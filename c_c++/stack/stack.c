#include <stdio.h>
#include <stdlib.h>
#define MAX(x, y) (((x) > (y)) ? (x) : (y))

struct Node
{
    int value;
    struct Node *prev;
};

struct Node *head = NULL;
int length = 0;

void push(int value)
{
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    newNode->value = value;
    newNode->prev = NULL;
    length++;
    if (head == NULL)
    {
        head = newNode;
    }
    else
    {
        newNode->prev = head;
        head = newNode;
    }
}

int pop()
{
    if (head == NULL)
        return -1;

    length = MAX(0, length - 1);

    if (length == 0)
    {
        struct Node *temp = head;
        int value = temp->value;
        head = NULL;
        free(temp);
        return value;
    }

    struct Node *temp = head;
    int value = temp->value;
    head = head->prev;
    free(temp);

    return value;
}

int peek()
{
    return head->value;
};

int main()
{
    push(5);
    push(2);
    push(6);
    push(10);
    pop();
    printf("%d\n", head->value);
    printf("%d\n", length);
}