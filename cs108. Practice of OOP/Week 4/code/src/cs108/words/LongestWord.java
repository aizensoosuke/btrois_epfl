package cs108.words;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

import static java.nio.charset.StandardCharsets.UTF_8;

public final class LongestWord {
    public static void main(String[] args) throws IOException {
        try {
            System.out.print("Chargement des mots...");
            List<String> words = loadWords("mots.txt");
            System.out.printf("ok, %,d mots chargés !%n", words.size());

            System.out.print("Recherche du mot le plus long...");
            String longestWord = longestWord(words);
            System.out.printf("trouvé : %s.%n", longestWord);
        } catch (FileNotFoundException e) {
            System.err.println("Erreur : " + e.getLocalizedMessage());
            System.exit(1);
        }
    }

    private static List<String> loadWords(String fileName) throws IOException {
        try (BufferedReader r = Files.newBufferedReader(Path.of(fileName))) {
            List<String> ws = new ArrayList<>(); // essayer avec LinkedList
            String w;
            while ((w = r.readLine()) != null)
                ws.add(w); // essayer avec ws.add(0, w)
            return ws;
        }
    }

    private static String longestWord(List<String> words) {
        String longestWord = "";
        for (int i = 0; i < words.size(); ++i) {
            String w = words.get(i);
            if (w.length() > longestWord.length())
                longestWord = w;
        }
        return longestWord;
    }
}
