#include <stdio.h>
#include <stdlib.h>

int main()
{



    //Create variables and assign their initial values.
        int IntFn_2,IntFn_1,IntFn;
        IntFn_2=0;  IntFn_1=1;  IntFn=0;
        short  ShortFn_2,ShortFn_1,ShortFn;
        ShortFn_2=0;  ShortFn_1=1;  ShortFn=0;
        long  LongFn_2,LongFn_1,LongFn;
        LongFn_2=0; LongFn_1=1;  LongFn=0;
        unsigned int UIntFn_2,UIntFn_1,UIntFn;
        UIntFn_2 =0;UIntFn_1=1;UIntFn=0;
        unsigned short int USIntFn_2,USIntFn_1,USIntFn;
        USIntFn_2 =0;USIntFn_1=1;USIntFn=0;
        //Auxiliar variables
        int IntAux;
        short ShortAux;
        long LongAux;
        unsigned UIntAux;
        unsigned short int USIntAux;
        //try to compute 100-th term of fibonacci secuence .
        int n= 100;
        int overflowInt=0,overflowShort=0,overflowLong=0,overflowUInt=0,overflowUSInt=0;
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
            UIntAux=UIntFn;
            UIntFn_2=UIntFn_1;
            UIntFn_1=UIntFn;
            UIntFn=UIntFn_2+UIntFn_1;
            //----
            USIntAux=USIntFn;
            USIntFn_2=USIntFn_1;
            USIntFn_1=USIntFn;
            USIntFn=USIntFn_2+USIntFn_1;
            //----

            if(IntFn<0 && !overflowInt){
                printf("%s%i%s","Overflow computing ",i+1,"-th term of Fibonacci Sequence(data type: Int/Signed Int)\n");
                overflowInt=1;
            }
            if(ShortFn<0 && !overflowShort){
                printf("%s%i%s","Overflow computing ",i+1,"-th term of Fibonacci Sequence(data type: Short/Signed Short)\n");
                overflowShort=1;
            }
            if(LongFn<0 && !overflowLong){
                printf("%s%i%s","Overflow computing ",i+1,"-th term of Fibonacci Sequence(data type: Long/Signed Long)\n");
                overflowLong=1;
            }
            if(UIntFn<UIntFn_1 && !overflowUInt){
                printf("%s%i%s","Overflow computing ",i+1,"-th term of Fibonacci Sequence(data type: U.int/U.long int)\n");
                overflowUInt=1;
            }
            if(USIntFn<USIntFn_1 && !overflowUSInt){
                printf("%s%i%s","Overflow computing ",i+1,"-th term of Fibonacci Sequence(data type: U. short int)\n");
                overflowUSInt=1;
            }

        }


    return 0;
}
