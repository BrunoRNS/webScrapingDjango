/**
 * Shows the loading animation and hides the form container.
 * 
 * @returns {boolean} - true
 */
function showLoading() {

  const formContainer = document.getElementById('formContainer');
  const loadingContainer = document.getElementById('loadingContainer');
    
  formContainer.style.display = 'none';
  loadingContainer.style.display = 'flex';

  return true;

}


/**
 * Hides the loading animation and shows the form container.
 * 
 * @returns {boolean} - true
 */
function hideLoading() {

  const formContainer = document.getElementById('formContainer');
  const loadingContainer = document.getElementById('loadingContainer');

  loadingContainer.style.display = 'none';
  formContainer.style.display = 'block';

  return true;
  
}