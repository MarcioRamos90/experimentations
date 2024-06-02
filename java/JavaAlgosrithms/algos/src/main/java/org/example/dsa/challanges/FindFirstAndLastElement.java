package org.example.dsa.challanges;

public class FindFirstAndLastElement {
    public static void main(String[] args) {
        int[] arr = {1,1,8,8,8,8,8,12,13,11,12,13,14,15,18,18,18};
        int[] result = binarySearch(arr, 1);
        System.out.print(result[0] + " " + result[1]);

    }

    public static int[] binarySearch(int[] arr, int target) {
        int first = firstOccurrence(arr, target);

        if (first == -1) return  new int[]{-1,-1};

        int last = findLastOccurrence(arr, target);

        return new int[]{first, last};
    }
    public static int firstOccurrence(int[] arr, int target) {
        int start = 0;
        int end = arr.length - 1;
        int last = -1;

        while (start <= end) {
            int mid = start + (end - start) / 2;
            if (target < arr[mid]) {
                end = mid - 1;
            } else if (target > arr[mid]) {
                start = mid + 1;
            } else {
                last = mid;
                end = mid - 1;
            }
        }
        return last;
    }

    public static int findLastOccurrence(int[] arr, int target) {
        int start = 0;
        int end = arr.length - 1;
        int last = -1;

        while (start <= end) {
            int mid = start + (end - start) / 2;
            if (target < arr[mid]) {
                end = mid - 1;
            } else if (target > arr[mid]) {
                start = mid + 1;
            } else {
                last = mid;
                start = mid + 1;
            }
        }
        return last;
    }
}