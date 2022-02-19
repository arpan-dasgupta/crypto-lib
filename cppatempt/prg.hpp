class PRG{
    long long int val;
    PRG(){
        val=0;
    }

    private:
    long long int add_bit(bool bit){
        val = (val<<1LL) + bit;
        return val;
    }
};
