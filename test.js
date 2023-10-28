const MOD = 998244353;

// Function to calculate the sum of powers
function sumOfPowers(N, M, S) {
    // Generate all strings of length N
    const allStrings = generateAllStrings(N);

    let totalPower = 0;
    for (let i = 0; i < allStrings.length; i++) {
        const string = allStrings[i];
        // Count occurrences of each S_i string in the generated string
        const counts = countSubstrings(string, S);
        console.log(typeof counts)
        // Calculate the total power for this string
        let totalCount = Object.values(counts).reduce((acc, cur) => acc + cur, 0);
        let power = modularExponentiation(2, totalCount, MOD);

        // Update the total power
        totalPower = (totalPower + power) % MOD;
    }

    return totalPower;
}

// Function to count occurrences of given substrings in a string
function countSubstrings(string, substrings) {
    const counts = {};
    substrings.forEach(s => {
        counts[s] = (string.match(new RegExp(s, 'g')) || []).length;
    });
    return counts;
}


function generateAlStrings(N, alphabet = 'abcdefghijklmnopqrstuvwxyz') {
    const allStrings = [];

    function generateStrings(currentString, length) {
        if (length === 0) {
            allStrings.push(currentString);
            return;
        }

        for (let i = 0; i < alphabet.length; i++) {
            generateStrings(currentString + alphabet[i], length - 1);
        }
    }

    generateStrings('', N);
    return allStrings;
}

// Function to perform modular exponentiation
function modularExponentiation(base, exponent, modulus) {
    if (modulus === 1) return 0;
    let result = 1;
    base = base % modulus;
    while (exponent > 0) {
        if (exponent % 2 === 1) {
            result = (result * base) % modulus;
        }
        exponent = exponent >> 1;
        base = (base * base) % modulus;
    }
    return result;
}

function generateAllStrings(N, alphabet = 'abcdefghijklmnopqrstuvwxyz') {
    const allStrings = [];

    const stack = [];
    stack.push(['', N]);

    while (stack.length > 0) {
        const [currentString, length] = stack.pop();

        if (length === 0) {
            allStrings.push(currentString);
        } else {
            for (let i = 0; i < alphabet.length; i++) {
                stack.push([currentString + alphabet[i], length - 1]);
            }
        }
    }

    return allStrings;
}


c = generateAllStrings(3)
console.log(`count: ${c.length}`)
//console.log(c)

f = sumOfPowers(3, 2, ['ab', 'ba'])
console.log(f)