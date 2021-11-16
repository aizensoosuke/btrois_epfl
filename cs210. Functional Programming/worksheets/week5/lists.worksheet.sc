val nums = List(1, 2, 3, 4, 5, 6)
nums.partition(x => x % 2 != 0)
nums.span(x => x % 2 != 0)
def flatten(xs: Any): List[Any] = xs match {
  case Nil => Nil
  case x :: xs => flatten(x) ::: flatten(xs)
  case x => List(x)
}

flatten(List(5, List(List(3, 2), 3, List(1, 9))))

print("caco")
