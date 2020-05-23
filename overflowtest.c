#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void overflowed(){
    printf("\n		EXECUTION HIJACKED !!!\n\n");
}

void function1(char* str){
    char buffer[5];
    strcpy(buffer, str);
}

int main(int argc, char* argv[]){
    
    if(argc == 1){
        exit(0);
    }
    
    function1(argv[1]);
    printf("\nExecuted Normally !\n");
    return 0;
}
/*
 (gdb)	run $(perl -e 'print "A"x13 . "\x89\x51\x55\x55\x55\x55\x00\x00"')
 	>	gcc -g -fno-stack-protector -z execstack -o overflowtest overflowtest.c
 	>	x/16xw $rsp
*/
