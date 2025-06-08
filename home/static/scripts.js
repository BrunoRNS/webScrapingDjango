function startDownloadAnimation() {

  const btn = document.getElementById('downloadBtn');
  btn.disabled = true;
  btn.classList.add('bounce');
  btn.innerText = 'Processing...';
  
}