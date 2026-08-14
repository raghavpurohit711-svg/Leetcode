int mySqrt(int x) {
    if (x==0){
        return 0;
    }
    double a1 = x;
    double a2 = 0;
    while (true){
        a2 = 0.5*(a1+(x/a1));
        if (abs(a1-a2)<0.001){
            break;
        }
        a1=a2;
    }
    return a2;
}