import java.util.Scanner;

public class PlayerRandom {

    public static void main(String[] args) {
        int bidQuantity = 0;
        int bidValue = 6;
        Scanner s = new Scanner(System.in);
        while (s.hasNext()) {
            switch (s.next()) {
                case "NEW_ROUND":
                    bidQuantity = 0;
                    bidValue = 6;
                    break;
                case "PLAYER_BIDS":
                    s.nextInt();
                    bidQuantity = s.nextInt();
                    bidValue = s.nextInt();
                    break;
                case "PLAY":
                    if (bidQuantity > 0 && Math.random() < 0.4) {
                        System.out.println("CHALLENGE");
                    } else {
                        System.out.println("BID " + (bidQuantity + 1) + " " + bidValue);
                    }
            }
            s.nextLine();
        }
    }
}
