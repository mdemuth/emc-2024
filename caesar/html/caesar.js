let ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

function rotateChr(char, rot) {
    if (rot < 0) {
        rot = ALPHABET.length - (-rot % ALPHABET.length);
    }
    plainIndex = ALPHABET.indexOf(char);
    if (plainIndex < 0) {
        return char
    }
    rotIndex = (plainIndex + rot) % ALPHABET.length;
    return ALPHABET[rotIndex];
}

function rotateStr(text, rot) {
    let result = "";
    for (let i = 0; i < text.length; i++) {
        result += rotateChr(text.charAt(i), rot);
    }
    return result
}