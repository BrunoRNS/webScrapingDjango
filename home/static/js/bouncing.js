document.getElementById('downloadForm').addEventListener('submit', function (e) {

    e.preventDefault();

    const form = this;
    const btn = document.getElementById('downloadBtn');
    const input = document.getElementById('id_input_url');

    btn.disabled = true;
    btn.classList.add('bounce');
    btn.innerText = 'Processing...';
    input.disabled = true;

    setTimeout(() => {

        form.submit();

    }, 1);

    setTimeout(() => {

        btn.disabled = false;
        btn.classList.remove('bounce');
        btn.innerText = 'Generate ZIP';
        input.disabled = false;
        
    }, 10000);

});