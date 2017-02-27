function convertToRoman(num) {
    var M = Math.round(num / 1000);
    num - 1000*M
    var C = Math.round(num / 100);
    num - 100*C;
    var X = Math.round(num / 10);
    num - 10*X;
    var V = Math.round(num / 5);
    num - 5*V;
    var I = num; 
    return 'M'.repeat(M)+'C'.repeat(C)+'X'.repeat(X)+'V'.repeat(V)+'I'.repeat(I);
}

console.log(convertToRoman(4));