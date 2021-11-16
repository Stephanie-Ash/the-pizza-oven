## Testing

### Validator Testing
* HTML
    * All pages have been passed through the [W3C validator](https://validator.w3.org/) using URI input. An initial check flagged two spurious end tags and some issues with the iframe styles. These problems have been corrected.
    * No errors are now returned for all pages.
* CSS
    * All pages have been passed through the [Jigsaw validator](https://jigsaw.w3.org/css-validator/) using URI input and the CSS file has also been passed through using direct input.
    * No errors have been found for all pages.
* JS
    * The Javascript snippets have been passed through the [Beautify Tools](https://beautifytools.com/javascript-validator.php) validator. The bootstrap alert on the timeout function is flagged as not defined but is defined elsewhere.
    * No other errors have been found.
* Python
    * All Python files have been passed through the [PEP8 online](http://pep8online.com/) check with no errors flagged.
    * The Gitpod built in linter has also been used throughout development to improve the Python code through the shortening of lines and addition of docstrings.
