#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct {
    int height;
    char name[10];
    int age;
} Person;

void print_person(const Person *p) {
    printf("Name: %s, Age: %d, Height: %d\n", p->name, p->age, p->height);
}


int main() {
    Person people[3];

    strcpy(people[0].name, "Alice");
    people[0].age = 28;
    people[0].height = 190;

    strcpy(people[1].name, "Bob");
    people[1].age = 34;
    people[0].height = 180;

    strcpy(people[2].name, "Charlie");
    people[2].age = 22;
    people[0].height = 155;

    printf("Printing people:\n");
    for (int i = 0; i < 3; i++) {
        print_person(&people[i]);
    }

    return 0;
}
