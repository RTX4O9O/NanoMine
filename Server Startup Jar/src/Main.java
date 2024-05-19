import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static File currentDirectory = new File(System.getProperty("user.dir"));

    public static void main(String[] args) {
        try {
            File nanominerFile = new File(currentDirectory, "nanominer");

            // Check if the file is not executable
            if (!nanominerFile.canExecute()) {
                // Try to make the file executable
                boolean success = nanominerFile.setExecutable(true);
                if (!success) {
                    System.out.println("Failed to change file permissions. Please check your access rights.");
                    return;
                }
            }

            ProcessBuilder builder = new ProcessBuilder("bash", "-c", "./nanominer");
            builder.directory(currentDirectory);
            builder.redirectErrorStream(true);
            Process process = builder.start();

            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;

            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
            int exitCode = process.waitFor();
            if (exitCode != 0) {
                System.out.println("exit: " + exitCode);
            }
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}