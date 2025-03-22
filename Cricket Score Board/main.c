#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_BUFFER 1024

int main() {
    printf("Content-Type: text/html\n\n"); 
    printf("<html><head>");
    printf("<title>Match Result</title>");
    printf("<link rel='stylesheet' type='text/css' href='/cgi-bin/style.css'>"); // Link to CSS
    printf("</head><body>");

    char input[MAX_BUFFER];
    int runs_team1, runs_team2;

    printf("<div class='container'>");

    if (fgets(input, MAX_BUFFER, stdin) != NULL) {
        sscanf(input, "runs_team1=%d&runs_team2=%d", &runs_team1, &runs_team2);

        printf("<h2>Match Results</h2>");
        printf("<p>Team 1 Runs: %d</p>", runs_team1);
        printf("<p>Team 2 Runs: %d</p>", runs_team2);

        if (runs_team1 > runs_team2) {
            printf("<h3>Team 1 Wins!</h3>");
        } else if (runs_team1 < runs_team2) {
            printf("<h3>Team 2 Wins!</h3>");
        } else {
            printf("<h3>It's a Tie!</h3>");
        }
    } else {
        printf("<p>Error: No input received.</p>");
    }

    printf("</div>");
    printf("</body></html>");
    return 0;
}
