class rangePrimeRecursion
{
    public static boolean check(int start, int n, int end) {
        if(n%start==0)
            return false;
        else if(start==end)
            return true;
        return check(++start, n, end);
    }

    public static int numbers(int n, int num) {
        if(n==num+1)
            return n;

        if(n==2 || n==3)
            System.out.println(n);
            
        else if((check(2, n, (int)Math.sqrt(n))) == true)
            System.out.println(n);

        return numbers(++n, num);
    }

    public static void main(String[] args) {
        int num=10000;
        numbers(2, num);
    }
}
