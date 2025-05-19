/*
 * Jr Hector Gonzalez
 * 03/03/2024
 * JDK 18.0.2.1
 * calculate the scores and stats of the grades in a classroom
 */
public class ArrayScores {
    public static void main(String[] args) {
        int scores[] = {90, 100, 80, 85, 63, 73, 80, 92, 90};
        
        int totalSum = 0;
        int averageScore;
        int highestIndex = 0;
        int lowestIndex = 0;
        int scoreA = 0;
        int scoreB = 0;
        int scoreC = 0;
        int scoreD = 0;
        int scoreF = 0;
        
        
        for(int i = 0; i < scores.length; i++){
            totalSum += scores[i];
        
            if(scores[i] > scores[highestIndex]){
                highestIndex = i;
            }
            if(scores[i] < scores[lowestIndex]){
                lowestIndex = i;
            }
            if(scores[i] >=90 && scores[i] <=100){
                scoreA++;
            }
            if(scores[i] >=80 && scores[i] <=90){
                scoreB++;
            }
            if(scores[i] >=70 && scores[i] <=80){
                scoreC++;
            }
            if(scores[i] >=60 && scores[i] <=70){
                scoreD++;
            }
            if(scores[i] >=0 && scores[i] <=60){
                scoreF++;
            }
        }
        
        System.out.println("The sum is " + totalSum);
        averageScore = (totalSum/scores.length);
        System.out.println("The average is " + averageScore);
        System.out.println("The largest test score is " + scores[highestIndex]);
        System.out.println("The lowest test score is " + scores[lowestIndex]);
        System.out.println("The numbers of students with scores 90-100(A) is " + scoreA);
        System.out.println("The numbers of students with scores 80-90(B) is " + scoreB);
        System.out.println("The numbers of students with scores 70-80(C) is " + scoreC);
        System.out.println("The numbers of students with scores 60-70(D) is " + scoreD);
        System.out.println("The numbers of students with scores 0-60(F) is " + scoreF);
    }
    
}
