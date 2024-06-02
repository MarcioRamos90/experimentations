package org.example.dsa.challanges;

public class InfiniteBinarySearch {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 13, 15, 16, 17, 18, 19, 20, 21, 23, 35, 45, 66, 77, 88, 99, 100};
        int ans = research(arr, 100);
        System.out.println(ans);
    }

    public static int research(int[] arr, int target) {
        int start = 0;
        int end = 1;
        while (target > arr[end]) {
            int newStart = end + 1;
            end = Math.max(end + (end - start + 1) * 2, arr.length-1);
            start = newStart;
        }
        return binarySearch(arr, start, end, target);
    }

    // return the index
    // return -1 if does not find
    public static int binarySearch(int[] arr, int start, int end, int target) {
        while (start <= end) {
            // find middle element
            int mid = start + (end - start) / 2;

            if (target < arr[mid]) {
                end = mid - 1;
            } else if (target > arr[mid]) {
                start = mid + 1;
            } else {
                return mid;
            }
        }
        return -1;
    }
}
