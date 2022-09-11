class Calculator{
 public static void main(String[] a){
 System.out.println(new Fac().Compute(10));
 }
}
class Fac {
 public int Compute(int num){
 int n ;
 if (num < 1)
 n = 1 ;
 else
 n = num * (this.Compute(new Adder().Compute(num, 0 - 1))) ;
 return n ;
 }
}
class Adder {
 public int Compute(int a , int b){
 result = a + b;
 return result ;
 }
}