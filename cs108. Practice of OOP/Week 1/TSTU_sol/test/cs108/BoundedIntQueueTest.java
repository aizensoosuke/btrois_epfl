package cs108;

import org.junit.jupiter.api.Test;

import java.util.Random;

import static org.junit.jupiter.api.Assertions.*;

public abstract class BoundedIntQueueTest {
    protected abstract BoundedIntQueue newBoundedIntQueue(int capacity);

    @Test
    public void constructingAQueueWithNegativeCapacityFails() {
        assertThrows(IllegalArgumentException.class, () -> {
            newBoundedIntQueue(-1);
        });
    }

    @Test
    public void capacityIsEqualToWhatWasAsked() {
        for (int c = 0; c <= 100; ++c)
            assertEquals(c, newBoundedIntQueue(c).capacity());
    }

    @Test
    public void initialSizeIsZero() {
        assertEquals(0, newBoundedIntQueue(10).size());
    }

    @Test
    public void addingToQueueWithZeroCapacityFails() {
        BoundedIntQueue q = newBoundedIntQueue(0);
        assertThrows(IllegalStateException.class, () -> {
            q.addLast(0);
        });
    }

    @Test
    public void addingToFullQueueFails() {
        BoundedIntQueue q = newBoundedIntQueue(2);
        q.addLast(1);
        q.addLast(2);
        assertThrows(IllegalStateException.class, () -> {
            q.addLast(3);
        });
    }

    @Test
    public void removingFromEmptyQueueFails() {
        BoundedIntQueue q = newBoundedIntQueue(10);
        assertThrows(IllegalStateException.class, () -> {
            q.removeFirst();
        });
    }

    @Test
    public void sizeReturnsCorrectValue() {
        int capacity = 100;
        BoundedIntQueue q = newBoundedIntQueue(capacity);
        for (int i = 0; i < capacity; ++i) {
            assertEquals(i, q.size());
            q.addLast(i);
        }
    }

    @Test
    public void isEmptyIsInitiallyTrue() {
        for (int capacity = 0; capacity < 100; ++capacity) {
            BoundedIntQueue q = newBoundedIntQueue(capacity);
            assertTrue(q.isEmpty());
        }
    }

    @Test
    public void isFullIsInitiallyFalse() {
        for (int capacity = 1; capacity < 100; ++capacity) {
            BoundedIntQueue q = newBoundedIntQueue(capacity);
            assertFalse(q.isFull());
        }
    }

    @Test
    public void hasFirstInFirstOutBehavior() {
        Random rng = new Random();
        BoundedIntQueue q = newBoundedIntQueue(20);
        int nextToAdd = 0;
        int nextToRemove = 0;
        for (int i = 0; i < 1000; ++i) {
            if (q.isEmpty() || (!q.isFull() && rng.nextInt(3) != 0))
                q.addLast(nextToAdd++);
            else
                assertEquals(nextToRemove++, q.removeFirst());
        }
        while (!q.isEmpty())
            assertEquals(nextToRemove++, q.removeFirst());
        assertEquals(nextToAdd, nextToRemove);
    }
}
