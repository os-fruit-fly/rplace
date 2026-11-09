const motionControl = document.querySelector('.event-motion');
const motionPreference = window.matchMedia('(prefers-reduced-motion: reduce)');
const previews = Array.from(document.querySelectorAll('#event-cards img[data-animation]'), image => ({
  image,
  still: image.getAttribute('src')
}));

function showAnimations(play) {
  for (const { image, still } of previews) {
    image.src = play ? image.dataset.animation : still;
  }
  motionControl.textContent = play ? 'Show still images' : 'Play animations';
}

function followMotionPreference() {
  showAnimations(!motionPreference.matches);
}

motionControl.addEventListener('click', () => {
  const { image, still } = previews[0];
  showAnimations(image.getAttribute('src') === still);
});
motionPreference.addEventListener('change', followMotionPreference);
followMotionPreference();
motionControl.hidden = false;
