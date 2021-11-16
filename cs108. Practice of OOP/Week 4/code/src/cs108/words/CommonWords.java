package cs108.words;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Collection;
import java.util.HashSet;
import java.util.Iterator;

import static java.nio.charset.StandardCharsets.UTF_8;

public final class CommonWords {
    public static void main(String[] args) throws IOException {
        Collection<String> frWords = new HashSet<>(); // essayer aussi ArrayList, TreeSet
        Collection<String> enWords = new HashSet<>(); // idem

        System.out.print("Chargement des mots français...");
        loadWords("mots.txt", frWords);
        System.out.println("ok, " + frWords.size() + " mots chargés!");

        System.out.print("Chargement des mots anglais...");
        loadWords("words.txt", enWords);
        System.out.println("ok, " + enWords.size() + " mots chargés!");

        System.out.print("Recherche des mots communs...");
        frWords.retainAll(enWords);
        System.out.println("trouvé " + frWords.size() + " mots communs.");

        Iterator<String> it = frWords.iterator();
        for (int i = 0; i < 10; ++i)
            System.out.println(it.next());
    }

    private static void loadWords(String fileName, Collection<String> target) throws IOException {
        try (BufferedReader r = Files.newBufferedReader(Path.of(fileName))) {
            String w;
            while ((w = r.readLine()) != null)
                target.add(w);
        }
    }
}
