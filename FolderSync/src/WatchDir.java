import java.nio.file.*;
import static java.nio.file.StandardWatchEventKinds.*;
import static java.nio.file.LinkOption.*;
import java.nio.file.attribute.*;
import java.io.*;
import java.util.*;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class WatchDir {

    private final WatchService watcher;
    private final Map<WatchKey, Path> keys;
    private final boolean recursive;
    private boolean trace = false;

    @SuppressWarnings("unchecked")
    static <T> WatchEvent<T> cast(WatchEvent<?> event) {
        return (WatchEvent<T>) event;
    }

    /**
     * Register the given directory with the WatchService
     */
    private void register(Path dir) throws IOException {
        WatchKey key = dir.register(watcher, ENTRY_CREATE, ENTRY_DELETE, ENTRY_MODIFY);
        if (trace) {
            Path prev = keys.get(key);
            if (prev == null) {
                System.out.format("register: %s\n", dir);
            } else {
                if (!dir.equals(prev)) {
                    System.out.format("update: %s -> %s\n", prev, dir);
                }
            }
        }
        keys.put(key, dir);
    }

    /**
     * Register the given directory, and all its sub-directories, with the
     * WatchService.
     */
    private void registerAll(final Path start) throws IOException {
        // register directory and sub-directories
        Files.walkFileTree(start, new SimpleFileVisitor<Path>() {
            @Override
            public FileVisitResult preVisitDirectory(Path dir, BasicFileAttributes attrs)
                    throws IOException {
                register(dir);
                return FileVisitResult.CONTINUE;
            }
        });
    }

    /**
     * Creates a WatchService and registers the given directory
     */
    WatchDir(Path dir, boolean recursive) throws IOException {
        this.watcher = FileSystems.getDefault().newWatchService();
        this.keys = new HashMap<WatchKey, Path>();
        this.recursive = recursive;

        if (recursive) {
            System.out.format("Scanning %s ...\n", dir);
            registerAll(dir);
            System.out.println("Done.");
        } else {
            register(dir);
        }

        // enable trace after initial registration
        this.trace = true;
    }

    /**
     * Process all events for keys queued to the watcher
     */
    void processEvents() {
        for (;;) {

            // wait for key to be signalled
            WatchKey key;
            try {
                key = watcher.take();
            } catch (InterruptedException x) {
                return;
            }

            Path dir = keys.get(key);
            if (dir == null) {
                System.err.println("WatchKey not recognized!!");
                continue;
            }

            for (WatchEvent<?> event : key.pollEvents()) {
                WatchEvent.Kind kind = event.kind();

                // TBD - provide example of how OVERFLOW event is handled
                if (kind == OVERFLOW) {
                    continue;
                }

                // Context for directory entry event is the file name of entry
                WatchEvent<Path> ev = cast(event);
                Path name = ev.context();
                Path child = dir.resolve(name);

                // print out event
                System.out.format("%s: %s\n", event.kind().name(), child);

                if (event.kind() == ENTRY_CREATE) {
                    try {

                        try {
                            FileOwnerAttributeView ownerAttributeView = Files.getFileAttributeView(child,
                                    FileOwnerAttributeView.class);
                            UserPrincipal owner = ownerAttributeView.getOwner();
                            System.out.println("Owner: " + owner.getName());
                        } catch (Exception e) {
                            // TODO: handle exception
                        }

                        BasicFileAttributes attr = Files.readAttributes(child, BasicFileAttributes.class);
                        String fileType = Files.probeContentType(child);
                        System.out.println("type " + fileType);
                        System.out.println("filename " + child.getFileName());
                        System.out.println("creationTime: " + attr.creationTime());
                        System.out.println("lastAccessTime: " + attr.lastAccessTime());
                        System.out.println("lastModifiedTime: " + attr.lastModifiedTime());

                        System.out.println("isDirectory: " + attr.isDirectory());
                        System.out.println("isOther: " + attr.isOther());
                        System.out.println("isRegularFile: " + attr.isRegularFile());
                        System.out.println("isSymbolicLink: " + attr.isSymbolicLink());
                        System.out.println("size: " + attr.size());
                        System.out.println("fileKey: " + attr.fileKey());

                        System.out.println("--------------------------------------------------");
                        connection = DriverManager.getConnection("jdbc:sqlite:sample.db");
                        Statement stmt = connection.createStatement();
                        String sql = "INSERT INTO files (location) VALUES ('" + child + "')";
                        stmt.executeUpdate(sql);
                        stmt.close();

                    } catch (Exception e) {
                        // TODO Auto-generated catch block
                        e.printStackTrace();
                    }
                }

                // if directory is created, and watching recursively, then
                // register it and its sub-directories
                if (recursive && (kind == ENTRY_CREATE)) {
                    try {
                        if (Files.isDirectory(child, NOFOLLOW_LINKS)) {
                            registerAll(child);
                        }
                    } catch (IOException x) {
                        // ignore to keep sample readbale
                    }
                }
            }

            // reset key and remove from set if directory no longer accessible
            boolean valid = key.reset();
            if (!valid) {
                keys.remove(key);

                // all directories are inaccessible
                if (keys.isEmpty()) {
                    break;
                }
            }
        }
    }

    static void usage() {
        System.err.println("usage: java WatchDir [-r] dir");
        System.exit(-1);
    }

    static Connection connection = null;

    public static void main(String[] args) throws IOException {
        // parse arguments
        // if (args.length == 0 || args.length > 2)
        // usage();

        try {
            Class.forName("org.sqlite.JDBC");
        } catch (ClassNotFoundException e1) {
            // TODO Auto-generated catch block
            e1.printStackTrace();
        }

        Connection connection = null;
        try {
            // create a database connection
            connection = DriverManager.getConnection("jdbc:sqlite:sample.db");
            Statement statement = connection.createStatement();
            statement.setQueryTimeout(30); // set timeout to 30 sec.

            statement.executeUpdate(
                    "create table if not exists files (id INTEGER PRIMARY KEY AUTOINCREMENT, location string)");
        } catch (SQLException e) {
            // if the error message is "out of memory",
            // it probably means no database file is found
            System.err.println(e.getMessage());
        }

        // if (args.length == 0 || args.length > 2)
        // usage();

        boolean recursive = false;
        int dirArg = 0;
        // if (args[0].equals("-r")) {
        // if (args.length < 2)
        // usage();
        recursive = true;
        dirArg++;
        // }

        // register directory and process its events
        Path dir = Paths.get("D:\\filesearch1.0.0\\FolderSync\\bin\\test");
        new WatchDir(dir, recursive).processEvents();
    }
}