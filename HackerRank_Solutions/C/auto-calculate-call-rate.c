#include <stdio.h>
int main()
{
	double min;
	printf("Enter the number of minutes: ");
	scanf("%lf", &min);
	
	double money = 0.0;
	
	if(min <= 1){
	money = 4.0;
	} else if(min <= 5){
	money = 3.5;
	} else if(min <= 8){
	money = 3.2;
	} else if(min <= 12){
	money = 3.0;
	} else if(min <= 16){
	money = 2.8;
	} else if(min <= 25){
	money = 2.0;
	} else {
	money = 1.6;
	}
	
	money *= min;
	money = money + ((money * 1.5) / 100);
	
	printf("Total charge: %.3lf\n", money);
	return 0;
}