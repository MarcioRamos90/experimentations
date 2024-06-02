package org.example.dsa.challanges;

public class BSRotateArray {
    public static void main(String[] args) {
        int[] arr = {15,16,17,18, 1,2,3,4,5,6,7,8,9,11,12,13,14};
        System.out.println(search(arr, 4));
    }
    public static int search(int[] arr, int target) {
        int pivot = findPivot(arr);
        int firstHalf = binarySearch(arr, target, 0, pivot);
        if (firstHalf != -1 || arr.length == pivot + 1) return firstHalf;
        return binarySearch(arr, target, pivot + 1, arr.length - 1);
    }
    public static int binarySearch(int[] arr, int target, int start, int end) {
        while (start <= end) {
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
    public static int findPivot(int[] arr) {
        int start = 0;
        int end = arr.length - 1;
        while (start < end) {
            int mid = start + (end - start) / 2;
            if (arr[mid] < arr[0]) {
                end = mid - 1;
            } else if (arr[mid] >= arr[0] && arr[mid] < arr[mid + 1]) {
                start = mid + 1;
            } else {
                return mid;
            }
        }
        return start;
    }
}
