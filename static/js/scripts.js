document.addEventListener("DOMContentLoaded", () => {
    const resultDiv = document.getElementById("result");
    
    if (resultDiv) {
        // Add fade-in effect for the result section
        resultDiv.style.opacity = 0;
        setTimeout(() => {
            resultDiv.style.transition = "opacity 1s";
            resultDiv.style.opacity = 1;
        }, 100);
    }
  });
  