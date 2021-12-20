var select = document.getElementById('filter')

select.addEventListener('change', function() {
    window.location.href = 'http://127.0.0.1:8000/?filter=' + this.value;
})
