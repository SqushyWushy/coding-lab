
public class DisplayCurrentTime {
    public static void main(String[] args) {
        System.out.println(getMyTime());
    }
    public static String getMyTime(){
        long totalMilliseconds = System.currentTimeMillis();
        long totalSeconds = totalMilliseconds / 1000;
        long totalMinutes = totalSeconds / 60;
        long totalHours = totalMinutes / 60;
        long currentSeconds = totalSeconds % 60;
        long currentMinutes = totalMinutes % 60;
        long currentHours = (totalHours % 24) % 12;

        if(currentHours == 0){
            currentHours = 12;
        }
        String amPm = (totalHours % 24 < 12) ? "AM" : "PM";

        return String.format("%02d:%02d:%02d %s", currentHours, currentMinutes, currentSeconds, amPm);
    }
}