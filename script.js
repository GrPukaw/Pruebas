for (let i = 0; i < 1000; i++) {
    const box = document.createElement('div');
    box.className = 'box';
    box.style.transform = `translate3d(${Math.random() * 2000 - 1000}px, ${Math.random() * 2000 - 1000}px, ${Math.random() * 2000 - 1000}px)`;
    document.querySelector('.scene').appendChild(box);
}
