// Last updated: 2/5/2026, 7:44:53 AM
bool isPalindrome(int x)
{
long long sum=0,ld,on=x;
    while(x>0)
    {
        ld=x%10;
        sum=sum*10+ld;
        x=x/10;        
    }
    if (sum==on)
        return true;
    return false;
}
