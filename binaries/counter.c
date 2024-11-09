#include<stdio.h>

int main()
{
   int x = 1;
   int* y = &x;
   int i;
   for(i=1;i<=100;i++)
   {
      printf("%d\n",*y);
      *y = *y + 1;
   }
}
