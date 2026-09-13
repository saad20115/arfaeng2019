/** @odoo-module **/

(function () {
    'use strict';

    function initStepSliders() {
        const sliders = document.querySelectorAll('.wasm-auto-slider, .wasm-marquee-slider, .wasm-gallery-marquee-wrapper');
        sliders.forEach(function (slider) {
            if (slider.dataset.sliderInitialized === 'true') return;
            slider.dataset.sliderInitialized = 'true';

            const track = slider.querySelector('.wasm-slider-track, .wasm-marquee-track, .wasm-gallery-marquee-track');
            if (!track) return;

            const originalItems = Array.from(track.children);
            const itemCount = originalItems.length;
            if (itemCount <= 1) return;

            // Clone set 2 times for seamless 3-set buffer
            for (let round = 0; round < 2; round++) {
                for (let i = 0; i < itemCount; i++) {
                    const clone = originalItems[i].cloneNode(true);
                    clone.classList.add('wasm-slider-clone');
                    track.appendChild(clone);
                }
            }

            const direction = slider.dataset.direction || 'left';
            const intervalTime = 2000; // Exactly 2 seconds per step
            let currentIndex = (direction === 'right') ? itemCount : 0;
            let isPaused = false;

            function updatePosition(animate) {
                const firstItem = track.children[0];
                if (!firstItem) return;

                const itemWidth = firstItem.offsetWidth + 24; // Width + gap
                const offset = currentIndex * itemWidth;
                const isRTL = document.documentElement.dir === 'rtl' || document.body.classList.contains('o_rtl') || document.documentElement.lang === 'ar';

                if (animate === false) {
                    track.style.transition = 'none';
                } else {
                    track.style.transition = 'transform 0.6s cubic-bezier(0.25, 1, 0.5, 1)';
                }

                if (isRTL) {
                    track.style.transform = 'translateX(' + offset + 'px)';
                } else {
                    track.style.transform = 'translateX(-' + offset + 'px)';
                }
            }

            // Initial positioning without animation
            updatePosition(false);

            function stepNext() {
                if (direction === 'right') {
                    currentIndex--;
                    updatePosition(true);

                    if (currentIndex <= 0) {
                        setTimeout(function () {
                            currentIndex = itemCount;
                            updatePosition(false);
                        }, 600);
                    }
                } else {
                    currentIndex++;
                    updatePosition(true);

                    if (currentIndex >= itemCount) {
                        setTimeout(function () {
                            currentIndex = 0;
                            updatePosition(false);
                        }, 600);
                    }
                }
            }

            // Step movement every 2 seconds
            setInterval(function () {
                if (!isPaused) {
                    stepNext();
                }
            }, intervalTime);

            // Pause on hover
            slider.addEventListener('mouseenter', function () {
                isPaused = true;
            });

            slider.addEventListener('mouseleave', function () {
                isPaused = false;
            });

            window.addEventListener('resize', function () {
                updatePosition(false);
            });
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initStepSliders);
    } else {
        initStepSliders();
    }

    window.addEventListener('load', initStepSliders);
})();
