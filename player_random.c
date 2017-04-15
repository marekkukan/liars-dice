#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));
    char line[1000];
    char *str, *token, *end;
    int quantity, value;
    while (fgets(line, sizeof line, stdin)) {
        str = strdup(line);
        token = strsep(&str, " ");
        if (strcmp(token, "NEW_ROUND") == 0) {
            quantity = 0;
            value = 6;
        } else if (strcmp(token, "PLAYER_BIDS") == 0) {
            token = strsep(&str, " ");
            token = strsep(&str, " ");
            quantity = strtol(token, &end, 10);
            token = strsep(&str, " ");
            value = strtol(token, &end, 10);
        } else if (strcmp(token, "PLAY") == 0) {
            if (quantity > 0 && rand() % 100 < 40) {
                printf("CHALLENGE\n");
            } else {
                printf("BID %d %d\n", ++quantity, value);
            }
            fflush(stdout);
        }
    }
    return 0;
}
