function convertToRoman(num) {
    var M = num % 1000;
    num - 1000*M
    var C = num % 100;
    num - 100*C;
    var X = num % 10;
    num - 10*X;
    var V = num % 5;
    num - 5*V;
    var I = num; 
    return M*'M'+C*'C'+X*'x'+V*'V'+I*'I';
}

console.log(convertToRoman(4));