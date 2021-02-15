#include <stdio.h>

int main()
{
    // โปรแกรมตัดเกรด
    int user_1_English_score = 72;
    if (user_1_English_score >= 50 && user_1_English_score < 60)
    {
        printf("เกรด 1 ");
    }
    else if (user_1_English_score >= 60 && user_1_English_score < 69)
    {
        printf("เกรด 2");
    }
    else if (user_1_English_score >= 70 && user_1_English_score < 80)
    {
        printf("เกรด 3");
    }
    else if (user_1_English_score >= 80 && user_1_English_score <= 100)
    {
        printf("เกรด 4");
    }
    else if (user_1_English_score >= 0 && user_1_English_score < 50)
    {
        printf("ติด 0 !!!");
    }
    else
    {
        printf("ป้อนเลขให้ถูก ... ");
    }
    return 0;
}