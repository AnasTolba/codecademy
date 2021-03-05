// importing util.random and util.scanner to be able to generate a random number and allow the user to ask a question
import java.util.Random;
import java.util.Scanner;

public class Magic8
{
    public static void main ( String[] args )
    {
        // creating the random and scanner objects
        Random r = new Random();
        Scanner s = new Scanner(System.in);

        // generating the random number between 1 and 15, initializing response
        int choice = 1 + r.nextInt(15);
        String response;

        // user input
        System.out.println("Please ask a yes or no question:");
        String question = s.nextLine();

        // indicating magic 8 ball response based on random number
        switch (choice) {
            case 1:
                response = "It is certain";
                break;
            case 2:
                response = "It is decidedly so";
                break;
            case 3:
                response = "Without a doubt";
                break;
            case 4:
                response = "Yes - definitely";
                break;
            case 5:
                response = "You may rely on it";
                break;
            case 6:
                response = "As I see it, yes";
                break;
            case 7:
                response = "Most likely";
                break;
            case 8:
                response = "Outlook good";
                break;
            case 9:
                response = "Signs point to yes";
                break;
            case 10:
                response = "Yes";
                break;
            case 11:
                response = "Reply hazy, try again";
                break;
            case 12:
                response = "Ask again later";
                break;
            case 13:
                response = "Better not tell you now";
                break;
            case 14:
                response = "Cannot predict now";
                break;
            case 15:
                response = "Concentrate and ask again";
                break;
            default:
                response = "8-BALL ERROR!";
        }
        System.out.println("You asked the Magic 8 ball: " + question);
        System.out.println("MAGIC 8-BALL SAYS: " + response);
    }
}