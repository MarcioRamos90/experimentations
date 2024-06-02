package org.example.dsa.challanges;

public class OrderAgnosticBinarySearch {
    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18};
        System.out.println(binarySearch(arr, 18));

        int[] arr2 = {111,22,13,9,7,5,4,3,2,1};
        System.out.println(binarySearch(arr2, 2));
        System.out.println(binarySearch(arr2, 9));
    }

    // return the index
    // return -1 if does not find
    public static int binarySearch(int[] arr, int target) {

        int start = 0;
        int end = arr.length - 1;

        boolean isAsc = arr[start] < arr[end];

        while (start <= end) {
            // find middle element
            int mid = start + (end - start) / 2;

            if (target == arr[mid]) {
                return mid;
            }

            if (isAsc) {
                if (target < arr[mid]) {
                    end = mid - 1;
                } else {
                    start = mid + 1;
                }
            } else {
                if (target > arr[mid]) {
                    end = mid - 1;
                } else {
                    start = mid + 1;
                }
            }
        }
        return -1;
    }
}
