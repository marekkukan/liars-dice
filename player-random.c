#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));
    char line[1000];
    char *str, *token, *end;
    int count, value;
    while (fgets(line, sizeof line, stdin)) {
        str = strdup(line);
        token = strsep(&str, " ");
        if (strcmp(token, "NEW_ROUND") == 0) {
            count = 0;
            value = 6;
        } else if (strcmp(token, "PLAYER_BIDS") == 0) {
            token = strsep(&str, " ");
            token = strsep(&str, " ");
            count = strtol(token, &end, 10);
            token = strsep(&str, " ");
            value = strtol(token, &end, 10);
        } else if (strcmp(token, "PLAY") == 0) {
            if (count > 0 && rand() % 100 < 40) {
                printf("CHALLENGE\n");
            } else {
                printf("BID %d %d\n", ++count, value);
            }
            fflush(stdout);
        }
    }
    return 0;
}
