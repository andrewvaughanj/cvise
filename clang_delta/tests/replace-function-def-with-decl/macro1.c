#define M2 {
#define M1 M2
#define M22 }
#define M11 M22
int foo() M1
  return 0;
}
void bar() {
  int x = 0;
M11
