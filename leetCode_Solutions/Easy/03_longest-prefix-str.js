// Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".

const longestCommonPrefix = (string) => {
    if (!string.length) return '';
    let prefix = string[0];
    for (let i = 1; i < string.length; i++) {
        while (string[i].indexOf(prefix) != 0) {
            prefix = prefix.substring(0, prefix.length - 1);
            if (!prefix.length) return '';
        }
    }
    return prefix;
};

console.log(longestCommonPrefix(["flower", "flow", "flight"]));
console.log(longestCommonPrefix(["dog", "racecar", "car"]));