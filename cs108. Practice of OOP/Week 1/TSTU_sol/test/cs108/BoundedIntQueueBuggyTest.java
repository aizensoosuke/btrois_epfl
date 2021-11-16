package cs108;


public final class BoundedIntQueueBuggyTest extends BoundedIntQueueTest {
    public BoundedIntQueueBuggyTest() {}

    @Override
    protected BoundedIntQueue newBoundedIntQueue(int capacity) {
        return new BoundedIntQueueBuggy(capacity);
    }
}
