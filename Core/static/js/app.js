function scrollToTopic() {
  
    var targetElement = document.getElementById('section1');
    if (targetElement) {
        targetElement.scrollIntoView({ behavior: 'smooth' });
    }
}
