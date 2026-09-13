/** @odoo-module **/

/**
 * Wasm Video Player — handles video play/pause toggle for showcase videos.
 * Uses event delegation instead of inline onclick handlers for CSP compliance.
 */

function wasmToggleVideoPlay(wrapperEl) {
    const video = wrapperEl ? wrapperEl.querySelector('video') : document.getElementById('wasm_showcase_video');
    const playBtn = wrapperEl ? wrapperEl.querySelector('.wasm-video-play-btn') : document.getElementById('wasm_video_play_btn');

    if (!video) return;

    if (video.paused || video.ended) {
        video.play().then(() => {
            if (playBtn) playBtn.classList.add('is-playing');
        }).catch((err) => {
            console.error('Video play error:', err);
        });
    } else {
        video.pause();
        if (playBtn) playBtn.classList.remove('is-playing');
    }
}

const setupVideoListeners = () => {
    // Attach click handlers to all .wasm-video-wrapper elements via JS (not inline onclick)
    document.querySelectorAll('.wasm-video-wrapper').forEach((wrapper) => {
        wrapper.addEventListener('click', (e) => {
            e.stopPropagation();
            e.preventDefault();
            wasmToggleVideoPlay(wrapper);
        });
    });

    // Also attach to standalone play buttons
    document.querySelectorAll('.wasm-video-play-btn').forEach((btn) => {
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            e.preventDefault();
            const wrapper = btn.closest('.wasm-video-wrapper');
            wasmToggleVideoPlay(wrapper);
        });
    });

    // Video state listeners and autoplay trigger for UI sync
    document.querySelectorAll('.wasm-video-wrapper video').forEach((video) => {
        const wrapper = video.closest('.wasm-video-wrapper');
        const playBtn = wrapper ? wrapper.querySelector('.wasm-video-play-btn') : null;

        video.muted = true;
        video.play().then(() => {
            if (playBtn) playBtn.classList.add('is-playing');
        }).catch((err) => {
            console.log('Autoplay waiting for user interaction:', err);
        });

        video.addEventListener('play', () => {
            if (playBtn) playBtn.classList.add('is-playing');
        });
        video.addEventListener('pause', () => {
            if (playBtn) playBtn.classList.remove('is-playing');
        });
        video.addEventListener('ended', () => {
            if (playBtn) playBtn.classList.remove('is-playing');
        });
    });
};

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setupVideoListeners);
} else {
    setupVideoListeners();
}
