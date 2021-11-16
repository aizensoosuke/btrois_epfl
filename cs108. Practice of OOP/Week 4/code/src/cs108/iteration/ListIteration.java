package cs108.iteration;

import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;

public final class ListIteration {

    private static void printList1(List<String> l) {
        for (int i = 0; i < l.size(); ++i)
            System.out.println(l.get(i));
    }

    private static void printList2(List<String> l) {
        for (String s: l)
            System.out.println(s);
    }

    private static void printList3(List<String> l) {
        Iterator<String> i = l.iterator();
        while (i.hasNext())
            System.out.println(i.next());
    }

    public static void main(String[] args) {
        List<String> l = List.of("un", "deux", "trois");
        System.out.println("1:");
        printList1(l);
        System.out.println("2:");
        printList2(l);
        System.out.println("3:");
        printList3(l);
    }
}
