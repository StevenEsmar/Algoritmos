package jokerfolder;

public class JokerFolder {
    public static void main(String[] args) {
        
        //Create variables and assign their initial values.
        int IntFn_2,IntFn_1,IntFn;
        IntFn_2=0;  IntFn_1=1;  IntFn=0;
        short  ShortFn_2,ShortFn_1,ShortFn;
        ShortFn_2=0;  ShortFn_1=1;  ShortFn=0;
        long  LongFn_2,LongFn_1,LongFn;
        LongFn_2=0; LongFn_1=1;  LongFn=0;
        //Auxiliar variables
        int IntAux;
        short ShortAux;
        long LongAux;
        //try to compute 100-th term of fibonacci secuence .
        int n= 100;
        boolean overflowInt=false,overflowShort=false,overflowLong=false;
        //overflow flag is true when fn is negative then it prints.
        for(int i=0;i<n;i++){
            IntAux=IntFn; 
            IntFn_2=IntFn_1;
            IntFn_1=IntFn;
            IntFn=IntFn_2+IntFn_1;
            //--------
            ShortAux=ShortFn; 
            ShortFn_2=ShortFn_1;
            ShortFn_1=ShortFn;
            ShortFn=(short) (ShortFn_2+ShortFn_1);
            //---------
            LongAux=LongFn; 
            LongFn_2=LongFn_1;
            LongFn_1=LongFn;
            LongFn=LongFn_2+LongFn_1;
            //---------
            
            if(IntFn<0 && !overflowInt){
                System.out.println("Overflow computing " +String.valueOf(i+1) + "-th term of Fibonacci Sequence(data type: Int) ");
                overflowInt=true;
            }
            if(ShortFn<0 && !overflowShort){
                System.out.println("Overflow computing " +String.valueOf(i+1) + "-th term of Fibonacci Sequence(data type: Short) ");
                overflowShort=true;
            }
            if(LongFn<0 && !overflowLong){
                System.out.println("Overflow computing " +String.valueOf(i+1) + "-th term of Fibonacci Sequence(data type: Long) ");
                overflowLong=true;
            }
            
        }
    }
    
}
