function checkStr() {
    var string = document.getElementById("input").value;
    // testing string with regexp of denied chars:
    var denied = /[^A-Z0-9_]/;
    var res = denied.test(string);
    // now if we catch some char that matches pattern then fix string
    // by creating new string fixed_str and append normal chars to it:
    if (res) {
        var i = 0;
        var fixed_str = ""
        // iterating trough all string and fix bad chars,
        // don't check just last char, cause user can
        // copy-paste whole string. So even if user appended
        // one char i'll iterate trough all string.
        while (i < string.length) {
            character = string.charAt(i);
            var lowercase = /[a-z]/;
            var allowed = /[0-9_A-Z]/;
            // fixing allowed lowercase:
            // and toggling enable class to
            // make #par disappear
            if (lowercase.test(character)) {
                elem = document.getElementById("par");
                elem.innerHTML = "You've inputted lowercase char: " + character;
                elem.classList.remove('enable');
                setTimeout(function() {
                    elem.classList.add('enable');
                }, 1);
                fixed_str += character.toUpperCase();
            }
            // in this case all is ok, just adding char to fixed_str
            else if (allowed.test(character)) {
                fixed_str += character;
            }
            // don't do anything with char, just
            // toggle class to show message and disappear it
            else {
                elem = document.getElementById("par");
                elem.innerHTML = "You've inputted bad char: " + character;
                elem.classList.remove('enable');
                setTimeout(function() {
                    elem.classList.add('enable');
                }, 1);
            }
            i++;
        }
        //rewriting inputted text:
        document.getElementById("input").value = fixed_str;
    }
}