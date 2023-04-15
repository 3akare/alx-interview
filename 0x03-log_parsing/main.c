#include <stdio.h>
#include <string.h>

int main(void)
{
    int x, y, z;
    scanf("%d %*d %d", &x, &y, &z);
    printf("%d %d %d", x, y, z);
}