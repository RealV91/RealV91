const form = document.querySelector('form');
form.addEventListener('submit', (event) => {
    event.preventDefault(); 
    alert('Grazie per il tuo messaggio!');
});

document.querySelectorAll('.topnav a').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
      e.preventDefault();
      
      const targetId = this.getAttribute('href');
      const targetElement = document.querySelector(targetId);
      
      targetElement.scrollIntoView({
          behavior: 'smooth'
      });
  });
});
