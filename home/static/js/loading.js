const formContainer = document.getElementById('formContainer');
const loadingContainer = document.getElementById('loadingContainer');

function showLoading() {
    
  formContainer.style.display = 'none';
  loadingContainer.style.display = 'flex';

}


function hideLoading() {

  loadingContainer.style.display = 'none';
  formContainer.style.display = 'block';
  
}