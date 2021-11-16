package cs108;

import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import java.lang.IllegalArgumentException;

import cs108.BoundedIntQueueBuggy;
import cs108.BoundedIntQueueOk;
import cs108.BoundedIntQueueBuggySrc;

/**
 * Une classe de test pour BoundedIntQueue
 * @author Abehssera Yohan
 */
public class BoundedIntQueueTest {

    private static BoundedIntQueue newBoundedIntQueue(int capacity) {
        return new BoundedIntQueueBuggySrc(capacity);
    }

    private BoundedIntQueue makeFullQueue() {
        BoundedIntQueue queue = newBoundedIntQueue(123);
        for (int i = 0; i < 123; i++) {
            queue.addLast(i);
        }
        return queue;
    }

    @Test
    public void negativeCapacityThrowIllegalArgument() {
        assertThrows(IllegalArgumentException.class, () -> {
            BoundedIntQueue queue = newBoundedIntQueue(-1);
        });
    }
    // PASSED

    @Test
    public void largeNegativeCapacityThrowIllegalArgument() {
        assertThrows(IllegalArgumentException.class, () -> {
            BoundedIntQueue queue = newBoundedIntQueue(-999999);
        });
    }
    // PASSED

    @Test
    public void zeroCapacityForZeroCapacityQueue() {
        assertEquals(0, newBoundedIntQueue(0).capacity());
    }
    // FAILED => minimum capacity is 1 ??

    @Test
    public void emptyQueueIsEmpty() {
        assertTrue(newBoundedIntQueue(5).isEmpty());
    }
    // FAILED => constructor doesn't construct empty list?

    @Test
    public void capacityIsCorrectForSingletonQueue() {
        assertEquals(1, newBoundedIntQueue(1).capacity());
    }
    // FAILED : capacity is 1 more than it should be

    @Test
    public void capacityIsCorrect() {
        assertEquals(123, newBoundedIntQueue(123).capacity());
    }
    // FAILED : same thing, capacity is 124 not 123

    @Test
    public void zeroCapacityQueueIsFull() {
        assertTrue(newBoundedIntQueue(0).isFull());
    }
    // PASSED

    @Test
    public void canFillToCapacityWithoutError() {
        makeFullQueue();
        // No assert, this fails if exception is thrown
    }
    // FAILED : exception full queue (since the constructor doesn't make empty queue)

    @Test
    public void fullListIsFull() {
        BoundedIntQueue queue = makeFullQueue();
        assertTrue(queue.isFull());
    }
    // FAILED : same as just before, can't use makeFullQueue()

    @Test
    public void throwsErrorOnAddToFullList() {
        BoundedIntQueue queue = makeFullQueue();
        assertThrows(java.lang.IllegalStateException.class, () -> {
            queue.addLast(0);
            });
    }
    // FAILED : the wrong exception is thrown (should be illegalstate, not illegalargument)

    @Test
    public void throwsErrorOnRemoveFromEmptyList() {
        BoundedIntQueue queue = newBoundedIntQueue(123);
        assertThrows(java.lang.IllegalStateException.class, () -> {
            queue.removeFirst();
            });
    }

    @Test
    public void addAndRemoveFromSingletonReturnsElement() {
        BoundedIntQueue singleton = newBoundedIntQueue(1);
        singleton.addLast(5);
        assertEquals(5, singleton.removeFirst());
    }
    // FAILED : since this test tries to fill the queue and constructor is wrong

    @Test
    public void constructedQueueIsEmpty() {
        assertTrue(newBoundedIntQueue(123).isEmpty());
    }
    // FAILED : previous tests already say why

    @Test
    public void emptyQueueHasZeroSize() {
        assertEquals(0, newBoundedIntQueue(123).size());
    }
    // FAILED : previous tests say why

    @Test
    public void sizeIsCorrect() {
        BoundedIntQueue queue = newBoundedIntQueue(123);
        for (int i = 0; i < 123; i++) {
            assertEquals(i, queue.size());
            queue.addLast(i);
        }
        for (int i = 0; i < 123; i++) {
            assertEquals(123 - i, queue.size());
            queue.removeFirst();
        }
        assertEquals(0, queue.size());
    }
    // FAILED : constructed isn't empty

    @Test
    public void removeFirstReturnsRightElements() {
        BoundedIntQueue queue = newBoundedIntQueue(123);
        int random = 443398;

        for (int i = 0; i < 123; i++) {
            queue.addLast(random + i);
        }
        for (int i = 0; i < 123; i++) {
            assertEquals(random + i, queue.removeFirst());
        }
    }
    // FAILED : trying to fill queue...
}
