var is_debug = false;
var input_stdin = "";
var input_cursor = 0;

function main() {
    let t = nextInt();

    let v0 = 10;
    let v1 = 3;
    let v2 = 5;

    let v3 = 1;
    let v4 = v3 - v3;
    let v5 = v4 - v3;
    let v6 = v3;
    let v7 = v4 - v1;
    let v8 = v0;
    let v9 = v0 + v1;
    let v10 = v4;
    let v11 = v4;
    let v12 = v3;

    while (true) {
        v11 = v11 + v1;
        v10 = v10 + v0;
        let v13 = v10;
        let v14 = v4;
        let v15 = v4;

        while (true) {
            let v16 = v13 + v13;
            if (v16 <= v1) {
                break;
            }
            v13 = v13 - v1;
            v14 = v14 + v3;
            v15 = v15 + v1;
        }

        if (v13 <= v4) {
            v13 = v4 - v13;
        }

        let v17 = v4;
        let v18 = v3;

        while (true) {
            v17 = v17 + v13;
            v18 = v18 + v3;

            if (v18 <= v6) {
                continue;
            }

            v18 = v3;

            while (true) {
                v17 = v17 - v9;
                v18 = v18 + v3;

                if (v18 <= v12) {
                    continue;
                }

                if (v17 >= v4) {
                    v5 = v14;
                    v6 = v12;
                    v7 = v15;
                    v8 = v10;
                    v9 = v13;
                }

                break;
            }

            v12 = v12 + v3;

            if (v12 <= v2) {
                break;
            }
        }

        console.log(v6);
    }

}

if (is_debug) {
    main();
} else {
    process.stdin.resume();
    process.stdin.setEncoding('ascii');
    process.stdin.on('data', function (data) {
        input_stdin += data;
    });
    process.stdin.on('end', function () { main(); });
}

// default parsers for JS.
function nextInt() {
    return parseInt(nextString());
}

function nextFloat() {
    return parseFloat(nextString());
}

function nextString() {
    var next_string = "";
    clearWhitespaces();
    while (input_cursor < input_stdin.length && !isWhitespace(input_stdin[input_cursor])) {
        next_string += input_stdin[input_cursor];
        input_cursor += 1;
    }
    return next_string;
}

function nextChar() {
    clearWhitespaces();
    if (input_cursor < input_stdin.length) {
        return input_stdin[input_cursor++];
    } else {
        return '\0';
    }
}

function isWhitespace(character) {
    return ' \t\n\r\v'.indexOf(character) > -1;
}

function clearWhitespaces() {
    while (input_cursor < input_stdin.length && isWhitespace(input_stdin[input_cursor])) {
        // ignore the next whitespace character
        input_cursor += 1;
    }
}