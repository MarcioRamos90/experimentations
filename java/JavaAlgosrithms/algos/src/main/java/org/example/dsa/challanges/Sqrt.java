package org.example.dsa.challanges;

public class Sqrt {
    public static void main(String[] args) {
        System.out.println(mySqrt(2147395599));
    }
    public static int mySqrt(int x) {
        if(x==0)return x;
        int start = 1;
        int end = x;
        while (start <= end) {
            int mid = start + (end - start) / 2;

            if (mid > x/mid) {
                end = mid - 1;
            } else if (mid < x/mid)  {
                start = mid + 1;
            } else {
                return mid;
            }
        }
        return end;
    }

}
