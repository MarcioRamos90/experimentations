import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int greather = 0;
        int value;
        do {
            value = scanner.nextInt();
            if (value > greather) {
                greather = value;
            }
        }
        while(value > 0);
        System.out.println(greather);
    }
}

class Main2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int countScan = 0;
        int numberOfEntries = scanner.nextInt();
        int greaterNum = Integer.MIN_VALUE;
        while (countScan < numberOfEntries) {
            int entry = scanner.nextInt();
            if (entry > greaterNum && entry % 4 == 0 ) {
                greaterNum = entry;
            }
            countScan++;
        }

        System.out.println(greaterNum);
    }
}