package org.example.dsa.challanges;

public class FindSmallerChar {

    public static void main(String[] args) {
        char[] arr = {'c','f','j'};
        System.out.println(nextGreatestLetter(arr, 'd'));
    }
    static public char nextGreatestLetter(char[] arr, char target) {
        int start = 0;
        int end = arr.length - 1;

        if (target > arr[end]) return arr[start];

        while (start <= end) {
            int mid = start + (end - start) / 2;

            if (target == arr[mid]) {
                return arr[mid + 1];
            }
            if (target < arr[mid]) {
                end = mid - 1;
            } else if (target > arr[mid]) {
                start = mid + 1;
            }
        }
        return arr[start];
    }
}
