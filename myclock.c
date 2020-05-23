#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

typedef struct {
	int hr;
	int min;
	int sec;
}timer;

void* increment_seconds (void* clock){
	timer* clk = clock;
	while(1){
		sleep(1);
		(clk -> sec)++;
		//printf("\r %02d", clk -> sec);
		//fflush(stdout);
	} 
}
 
void* increment_minutes (void* clock){
	timer* clk = clock;
	while(1){
		sleep(60);
		(clk -> min)++;	
		clk -> sec = 0;
		//printf("\r %02d", clk -> min);
	} 
}

void* increment_hours (void* clock){
	timer* clk = clock;
	while(1){
		sleep(3600);
		(clk -> hr)++;
		clk -> min = 0;
		//printf("\r %02d", clk -> hr);
	} 
}

void* final_clock(void* clock){
	timer* clk = clock;
	char h[3] = {'\0'};
	char m[3] = {'\0'};
	char s[3] = {'\0'};
	while(1){
		
		sprintf(h, "%02d", clk -> hr);
		sprintf(m, "%02d", clk -> min);
		sprintf(s, "%02d", clk -> sec);
		printf("%s : %s : %s \r", h, m, s);
	}
}

int main(){

	pthread_t thread1, thread2, thread3, thread4;
	printf("%s\n", "Clock :");

	timer* clock = malloc(sizeof(time));
	clock -> hr = 0;
	clock -> min = 0;
	clock -> sec = 0;

	pthread_create(&thread1, NULL, increment_seconds, clock);
	pthread_create(&thread2, NULL, increment_minutes, clock);
	pthread_create(&thread3, NULL, increment_hours, clock);
	pthread_create(&thread4, NULL, final_clock, clock);

	pthread_join(thread1, NULL);
	pthread_join(thread2, NULL);
	pthread_join(thread3, NULL);

	printf("Clock Ends\n");
	exit(0);
}