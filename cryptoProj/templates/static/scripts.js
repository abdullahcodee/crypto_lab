document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('method').addEventListener('change', function() {
        var method = this.value;
        var keyField = document.getElementById('keyField');
        var shiftField = document.getElementById('shiftField');

        if (method === 'caesar') {
            keyField.style.display = 'none';
            shiftField.style.display = 'block';
        } else if (method === 'atbash') {
            keyField.style.display = 'none';
            shiftField.style.display = 'none';
        } else if (method === 'vigenere') {
            keyField.style.display = 'block';
            shiftField.style.display = 'none';
        }
    });
});
