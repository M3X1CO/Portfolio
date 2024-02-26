import java.nio.file.Paths;
import java.util.Scanner;

public class SportStatistics {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("File:");
        String file = scanner.nextLine();

        System.out.println("Team:");
        String teamToSearch = scanner.nextLine();

        TeamStats teamStats = getTeamStats(file, teamToSearch);

        System.out.println("Games: " + teamStats.getGamesPlayed());
        System.out.println("Wins: " + teamStats.getWins());
        System.out.println("Losses: " + teamStats.getLosses());
    }

    public static TeamStats getTeamStats(String file, String teamToSearch) {
        TeamStats teamStats = new TeamStats();

        try (Scanner reader = new Scanner(Paths.get(file))) {
            while (reader.hasNextLine()) {
                String row = reader.nextLine();
                String[] parts = row.split(",");
                String homeTeam = parts[0];
                String visitingTeam = parts[1];
                int homeTeamPoints = Integer.parseInt(parts[2]);
                int visitingTeamPoints = Integer.parseInt(parts[3]);

                if (homeTeam.equals(teamToSearch) || visitingTeam.equals(teamToSearch)) {
                    teamStats.addGame(homeTeam.equals(teamToSearch), homeTeamPoints, visitingTeamPoints);
                }
            }
        } catch (Exception e) {
            System.out.println("Error reading file: " + e.getMessage());
        }

        return teamStats;
    }
}

class TeamStats {
    private int gamesPlayed;
    private int wins;
    private int losses;

    public void addGame(boolean isHomeTeam, int homeTeamPoints, int visitingTeamPoints) {
        gamesPlayed++;

        if ((isHomeTeam && homeTeamPoints > visitingTeamPoints) || (!isHomeTeam && visitingTeamPoints > homeTeamPoints)) {
            wins++;
        } else {
            losses++;
        }
    }

    public int getGamesPlayed() {
        return gamesPlayed;
    }

    public int getWins() {
        return wins;
    }

    public int getLosses() {
        return losses;
    }
}
