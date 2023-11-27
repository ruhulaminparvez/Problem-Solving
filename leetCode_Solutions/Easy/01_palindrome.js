var isPalindrome = function (x) {
    let reversed = 0;
    let y = x;
    while (y > 0) {
        reversed = (reversed * 10) + (y % 10);
        y = Math.floor(y / 10);
    }
    return reversed === x;
};

console.log(isPalindrome(-121));