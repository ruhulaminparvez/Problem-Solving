var isPalindrome = function (x) {
    let reverse = 0;
    while (x > 0) {
        reverse = reverse * 10 + x % 10;
        console.log("reverse",reverse);
        x = Math.floor(x / 10);
        console.log("x",x);
    }
    console.log("reverse",reverse, "x",x);
    return reverse === x;
};


const takeInput = 121;
console.log(isPalindrome(takeInput));