#include <iostream>

using namespace std;

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
        bool overflowInt=false,overflowShort=false,overflowLong=false,overflowUInt=false,overflowUSInt=false;
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
                cout << "Overflow computing " << (i+1) << "-th term of Fibonacci Sequence(data type: Int/Signed Int)" <<endl;
                overflowInt=true;
            }
            if(ShortFn<0 && !overflowShort){
                cout << "Overflow computing " << (i+1) << "-th term of Fibonacci Sequence(data type: Short/Signed Short)" <<endl;
                overflowShort=true;
            }
            if(LongFn<0 && !overflowLong){
                cout <<"Overflow computing " << (i+1) << "-th term of Fibonacci Sequence(data type: Long/Signed Long)" <<endl;
                overflowLong=true;
            }
            if(UIntFn<UIntFn_1 && !overflowUInt){
                cout <<"Overflow computing " << (i+1) << "-th term of Fibonacci Sequence(data type: U.int/U.long int)" <<endl;
                overflowUInt=true;
            }
            if(USIntFn<USIntFn_1 && !overflowUSInt){
                cout <<"Overflow computing " << (i+1) << "-th term of Fibonacci Sequence(data type: U. short int)" <<endl;
                overflowUSInt=true;
            }

        }


        return 0;
}
