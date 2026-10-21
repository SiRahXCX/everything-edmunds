#include <stdio.h>
#define MAX 10

int queue[MAX];
int front = -1, rear = -1;

void enqueue(int);
int dequeue();
int peek();
void display();
void test_queue();  // function for testing all the queue operations 

int main()
{
  test_queue();  

  return 0;
}

void enqueue(int item)
{
  if (rear == MAX-1)
  {
    printf("queue overflow");
    return;
  }

  if (front == -1 && rear == -1)
    front = rear = 0;
  else
    ++rear;

  queue[rear] = item;
}

int dequeue()
{
  int item;

  if (front == -1 || front > rear)
  {
    printf("queue underflow");
    return -1;
  }

  item = queue[front++];
  return item;
}

int peek()
{
  if (front == -1 || front > rear)
  {
    printf("queue empty");
    return -1;
  }

  return queue[front];
}

void display()
{
  int index;

  if (front == -1 || front > rear)
  {
    printf("queue empty");
    return;
  }

  for (index = front; index <= rear; ++index)
    printf("%d\t", queue[index]);
}

void test_queue()
{
  printf("--- Enqueueing elements ---\n");
  enqueue(10);
  enqueue(20);
  enqueue(30);

  printf("Queue contents: ");
  display();
  printf("\n\n");

  printf("Peek front element: %d\n\n", peek());

  printf("--- Dequeueing an element ---\n");
  printf("Dequeued: %d\n", dequeue());

  printf("Queue contents after dequeue: ");
  display();
  printf("\n");
}