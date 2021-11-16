package cs108;


public final class BoundedIntQueueSlowTest extends BoundedIntQueueTest {
    public BoundedIntQueueSlowTest() {}

    @Override
    protected BoundedIntQueue newBoundedIntQueue(int capacity) {
        return new BoundedIntQueueSlow(capacity);
    }
}
