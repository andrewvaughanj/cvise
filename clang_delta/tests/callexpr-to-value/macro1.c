#define macro bar(1,2)
int bar(int p1, int p2) {
  return p1 + p2;
}

void foo(void) {
  int x = macro;
}
