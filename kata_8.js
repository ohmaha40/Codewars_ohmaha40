// Square(n) Sum
function squareSum(numbers){
    let res=0;
      for (let i =0;i<numbers.length;i++)
    { res += Math.pow(numbers[i],2);
    }
    return res;
    }

// Convert a Number to a String!
function numberToString(num) {
    return num.toString();
  }

// Find the smallest integer in the array
class SmallestIntegerFinder {
    findSmallestInt(args) {
      let res = args[0];
      for (let i=0;i<args.length;i++){
  if ( res >= args[i]){
  res = args[i];
  }
  }
      
      return res;
    }
  }

// Convert boolean values to strings 'Yes' or 'No'.
function boolToWord( bool ){
    if(bool) {return "Yes"}
    else return "No";
  }

// Remove String Spaces
function noSpace(x){
    return x.replace(/\s/g, '');
  
  }

// Grasshopper - Summation
var summation = function (num) {
    let res=0;
    for(let i=0;i<=num;i++){
      res += i;
  }return res;
  }

// Reversed Strings
function solution(str){
    return str.split("").reverse().join("");
    } 

// Remove First and Last Character
function removeChar(str){
    return str.substring(1,str.length -1);
    
   }

// Return Negative
function makeNegative(num) {
    if ( num<0) {return num}
    else {return -num};
  }

//   function makeNegative(n) {
//     if (n>0){
//       return n - 2*n;
//     } else return n;
//   }

// Opposite number
function opposite(number) {
    return number - 2*number;
  }

// Sum of positive
function positiveSum(arr) {
    let res =0;
      for (let i = 0; i < arr.length; i++) {
    if ( arr[i] > 0){
    res += arr[i];
    }
    }
      return res;
      
    }

// Even or Odd
function even_or_odd(number) {
    if (number === 0 || number % 2  ==0){
   return "Even"} else return "Odd";
  }

// Twice as old
function twiceAsOld(dadYearsOld, sonYearsOld) {
    let i=0;
      if ((sonYearsOld *2)<dadYearsOld){
    i= dadYearsOld - (sonYearsOld * 2);
    } else {
     i = ((sonYearsOld * 2) - dadYearsOld)
    }
    return i;
      }

// String repeat
function repeatStr (n, s) {
    let a=s.repeat(n);
    return a;
  }

// Multiply
function multiply(a, b){
    return a * b;
  }

// Counting sheep...
// https://www.codewars.com/kata/54edbc7200b811e956000556
function countSheeps(arrayOfSheep) {
    let res= 0;
    arrayOfSheep.forEach(e => {
        if (e === true){
        res += 1;
        }
    });
    return res;
  }

// Is n divisible by x and y?
// https://www.codewars.com/kata/5545f109004975ea66000086
function isDivisible(n, x, y) {
    if ( n % x === 0 && n % y === 0)
    {
        return true;
    } return false;
}
 //kürzer
 function isDivisible(n, x, y) {
    return n % x === 0 && n % y === 0
  }
  // oder
  function isDivisible(n, x, y) {
    return (n % x === 0 && n % y === 0) ? true : false;
  }

// Basic Mathematical Operations
// https://www.codewars.com/kata/57356c55867b9b7a60000bd7
function basicOp(operation, value1, value2)
{
  switch (operation) {
        case "+":
          return value1 + value2;
          break;
        case "-":
          return value1 - value2;
          break;
        case "*":
          return value1 * value2;
          break;
        case "/":
          return value1 / value2;
          break;
  }
}
basicOp('+', 4, 7);

