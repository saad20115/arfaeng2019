(function () {
    'use strict';

    function initTypewriter() {
        var targets = document.querySelectorAll(".wasm-typewriter-target");
        targets.forEach(function (el) {
            var fullText = el.getAttribute("data-typewriter-text");
            if (!fullText) {
                fullText = el.textContent.trim();
            }
            if (!fullText) return;

            // If already initialized and currently running, skip re-initialization
            if (el.dataset.typewriterInitialized === "true") return;
            el.dataset.typewriterInitialized = "true";

            // Clear inner HTML and rebuild clean typewriter markup
            el.innerHTML = "";

            var contentSpan = document.createElement("span");
            contentSpan.className = "wasm-typewriter-content";
            contentSpan.style.cssText = "color: #1e293b; font-weight: 600;";

            var cursorSpan = document.createElement("span");
            cursorSpan.className = "wasm-typewriter-cursor";
            cursorSpan.textContent = "|";
            cursorSpan.style.cssText = "display: inline-block; animation: wasmBlink 0.7s infinite; color: #d97706; font-weight: 800; margin-inline-start: 4px;";

            el.appendChild(contentSpan);
            el.appendChild(cursorSpan);

            var words = fullText.split(/\s+/);
            var currentIndex = 0;

            function typeWordByWord() {
                if (currentIndex <= words.length) {
                    var currentText = words.slice(0, currentIndex).join(" ");
                    contentSpan.textContent = currentText;
                    currentIndex++;

                    if (currentIndex <= words.length) {
                        setTimeout(typeWordByWord, 140);
                    } else {
                        // Pause at the end for 4 seconds then loop
                        setTimeout(function () {
                            currentIndex = 0;
                            contentSpan.textContent = "";
                            setTimeout(typeWordByWord, 400);
                        }, 4000);
                    }
                }
            }

            contentSpan.textContent = "";
            setTimeout(typeWordByWord, 200);
        });
    }

    if (document.readyState === "complete" || document.readyState === "interactive") {
        setTimeout(initTypewriter, 100);
    }
    document.addEventListener("DOMContentLoaded", initTypewriter);
    window.addEventListener("load", initTypewriter);

    setInterval(function () {
        if (document.querySelector(".wasm-typewriter-target:not([data-typewriter-initialized='true'])")) {
            initTypewriter();
        }
    }, 500);
})();

