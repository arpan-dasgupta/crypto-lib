class OneWay{
    int func_type;
    OneWay(int type=1){
        func_type = type;
    }
    long long int eval(long long int inp)
    {
        if(func_type==1)
            return discrete_log(inp);
        return -1;
    }
    long long int g = 23, p = 1000000007;

    public:
    long long int discrete_log(long long int val){
        long long int ans = 1, temp=1;
        while(val>0)
        {
            if(val%2==1)
                ans = (ans * temp)%p;
            temp = (temp * g)%p;
            val/=2;
        }
        return ans;
    }
    int hardcore_pred(long long int val)
    {
        if(val>p/2)
            return 1;
        else 
            return 0;
    }
};