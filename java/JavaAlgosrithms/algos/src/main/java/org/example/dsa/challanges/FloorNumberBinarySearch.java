package org.example.dsa.challanges;

public class FloorNumberBinarySearch {

    public static void main(String[] args) {
        int[] arr = {1,2,3,5,6,7,9,11,12,13,15,17,18};
        int res = floor(arr, 10);
        System.out.println(res + " " + arr[res]);
    }

    // return the index
    // return -1 if does not find
    public static int floor(int[] arr, int target) {
        int start = 0;
        int end = arr.length - 1;
        if (target < arr[start]) return -1;
        while (start < end) {
            int mid = start + (end - start) / 2;
            if (target == arr[mid]) return  mid;
            if (target < arr[mid]) {
                end = mid - 1;
            } else if (target > arr[mid]) {
                start = mid + 1;
            }
        }
        return end;
    }
}
