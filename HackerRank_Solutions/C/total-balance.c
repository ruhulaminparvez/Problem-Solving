#include <stdio.h>
int
main () 
{
  
	double taka;
	  
	printf ("Enter the amount(BDT): "); 
	scanf ("%lf", &taka);
	  
	taka -= (taka / 2);
	taka -= (taka / 4);
	  
	double answer = taka + ((taka * 10) / 100);
	  
	printf ("Final Balance: %.2lf\n", answer);
	  
	return 0;

}
