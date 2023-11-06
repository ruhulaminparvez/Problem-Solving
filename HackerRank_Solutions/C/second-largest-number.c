#include <stdio.h>
void
main ()
{
  int arr[50], n, i, j = 0, largest, second;
  printf ("Enter number of employees: ");
  scanf ("%d", &n);
  printf ("Enter the salaries: ", n);
  for (i = 0; i < n; i++)
    {
      scanf ("%d", &arr[i]);
    }
  largest = 0;
  for (i = 0; i < n; i++)
    {
      if (largest < arr[i])
	{
	  largest = arr[i];
	  j = i;
	}
    }
  second = 0;
  for (i = 0; i < n; i++)
    {
      if (i == j)
	{
	  i++;
	  i--;
	}
      else
	{
	  if (second < arr[i])
	    {
	      second = arr[i];
	    }
	}
    }
  printf ("Second largest salary: %d \n\n", second);
}
