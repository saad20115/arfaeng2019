/** @odoo-module **/

function initWasmAiBot() {
    const masterToggle = document.getElementById("wasmFloatingMasterToggle");
    const speedDialStack = document.getElementById("wasmFloatingStack");
    const botToggle = document.getElementById("wasmAiBotToggle");
    const chatWindow = document.getElementById("wasmAiChatWindow");
    const chatClose = document.getElementById("wasmAiChatClose");
    const chatBody = document.getElementById("wasmAiChatBody");
    const chatInput = document.getElementById("wasmAiInput");
    const sendBtn = document.getElementById("wasmAiSend");

    // Toggle Speed Dial Stack (Collapsed by default)
    if (masterToggle && speedDialStack) {
        masterToggle.addEventListener("click", function (e) {
            e.preventDefault();
            e.stopPropagation();
            const isCollapsed = speedDialStack.classList.contains("wasm-collapsed");
            const iconOpen = masterToggle.querySelector(".wasm-icon-open");
            const iconClose = masterToggle.querySelector(".wasm-icon-close");

            if (isCollapsed) {
                speedDialStack.classList.remove("wasm-collapsed");
                speedDialStack.classList.add("wasm-expanded");
                if (iconOpen && iconClose) {
                    iconOpen.classList.add("d-none");
                    iconClose.classList.remove("d-none");
                }
            } else {
                speedDialStack.classList.remove("wasm-expanded");
                speedDialStack.classList.add("wasm-collapsed");
                if (iconOpen && iconClose) {
                    iconOpen.classList.remove("d-none");
                    iconClose.classList.add("d-none");
                }
            }
        });
    }

    if (botToggle && chatWindow) {
        // Toggle Chat Window
        botToggle.addEventListener("click", function (e) {
            e.preventDefault();
            e.stopPropagation();
            chatWindow.classList.toggle("d-none");
            if (!chatWindow.classList.contains("d-none")) {
                chatInput && chatInput.focus();
            }
        });
    }

    chatClose && chatClose.addEventListener("click", function () {
        chatWindow.classList.add("d-none");
    });

    // Chip Clicks
    document.addEventListener("click", function (e) {
        const chip = e.target.closest(".wasm-chip-btn");
        if (chip) {
            const query = chip.getAttribute("data-query");
            if (query) {
                processUserQuery(query);
            }
        }
    });

    // Send Button Click
    sendBtn && sendBtn.addEventListener("click", function () {
        if (chatInput && chatInput.value.trim() !== "") {
            processUserQuery(chatInput.value.trim());
            chatInput.value = "";
        }
    });

    // Enter Key
    chatInput && chatInput.addEventListener("keypress", function (e) {
        if (e.key === "Enter" && chatInput.value.trim() !== "") {
            processUserQuery(chatInput.value.trim());
            chatInput.value = "";
        }
    });

    function processUserQuery(text) {
        const isEn = (document.documentElement.lang && document.documentElement.lang.startsWith("en")) || window.location.pathname.startsWith("/en");

        // Append User Message
        appendMessage(text, "user");

        // Show Typing Indicator
        showTypingIndicator();

        // Simulate AI Thinking Delay
        setTimeout(function () {
            removeTypingIndicator();
            const responseHtml = generateAiResponse(text, isEn);
            appendMessage(responseHtml, "bot");
            if (chatBody) chatBody.scrollTop = chatBody.scrollHeight;
        }, 800);
    }

    function appendMessage(content, sender) {
        if (!chatBody) return;
        const msgDiv = document.createElement("div");
        msgDiv.className = `wasm-ai-message ${sender}`;
        
        const bubbleDiv = document.createElement("div");
        bubbleDiv.className = "wasm-ai-msg-bubble";

        if (sender === "user") {
            bubbleDiv.textContent = content;
        } else {
            bubbleDiv.innerHTML = content;
        }

        msgDiv.appendChild(bubbleDiv);
        chatBody.appendChild(msgDiv);
        chatBody.scrollTop = chatBody.scrollHeight;
    }

    function showTypingIndicator() {
        if (!chatBody) return;
        const typingDiv = document.createElement("div");
        typingDiv.id = "wasmAiTyping";
        typingDiv.className = "wasm-ai-message bot";
        typingDiv.innerHTML = `
            <div class="wasm-ai-msg-bubble">
                <div class="wasm-typing-dots">
                    <span></span><span></span><span></span>
                </div>
            </div>
        `;
        chatBody.appendChild(typingDiv);
        chatBody.scrollTop = chatBody.scrollHeight;
    }

    function removeTypingIndicator() {
        const typingDiv = document.getElementById("wasmAiTyping");
        if (typingDiv) {
            typingDiv.remove();
        }
    }

    function generateAiResponse(query, isEn) {
        const q = query.toLowerCase();

        // Pricing / RFQ / Quote
        if (q.includes("سعر") || q.includes("عرض") || q.includes("تكلفة") || q.includes("quote") || q.includes("price") || q.includes("rfq") || q.includes("cost") || q.includes("طلب")) {
            if (isEn) {
                return `
                    <p class="mb-2">We are delighted to prepare a detailed engineering quotation for your project! 📋</p>
                    <p class="mb-2">Please fill out our quick online RFQ form to route your drawings to our estimating team:</p>
                    <a href="/quote" class="btn btn-sm btn-warning rounded-pill fw-bold text-dark w-100">Proceed to RFQ Form <i class="fa fa-arrow-right ms-1"></i></a>
                `;
            }
            return `
                <p class="mb-2">يسعدنا تقديم عرض سعر تفصيلي لمشروعك وفق الكود السعودي! 📋</p>
                <p class="mb-2">يمكنك تعبئة النموذج الإلكتروني السريع وسيتم تحويله فوراً لقسم الحسابات والبرامج الإنشائية:</p>
                <a href="/quote" class="btn btn-sm btn-warning rounded-pill fw-bold text-dark w-100">الانتقال لنموذج طلب عرض السعر <i class="fa fa-arrow-left ms-1"></i></a>
            `;
        }

        // Saudi Building Code (SBC)
        if (q.includes("كود") || q.includes("sbc") || q.includes("سعودي") || q.includes("معايير") || q.includes("سلامة") || q.includes("code") || q.includes("saudi")) {
            if (isEn) {
                return `
                    <p class="mb-2">Wasm General Contracting strictly adheres to the <strong>Saudi Building Code (SBC 301 - SBC 306)</strong> 🏗️</p>
                    <p class="mb-0">We guarantee full structural compliance, certified concrete testing, and rigid safety quality control for every construction milestone.</p>
                `;
            }
            return `
                <p class="mb-2">تلتزم شركة وسم للمقاولات العامة بالمرجع القياسي <strong>الكود السعودي للبناء (SBC 301 - SBC 306)</strong> 🏗️</p>
                <p class="mb-0">نضمن لك أعلى درجات السلامة الإنشائية، والخرسانات المعتمدة، واختبارات الجودة المخبرية لكل مرحلة بناء.</p>
            `;
        }

        // MEP / HVAC / Mechanical / Electrical / Plumbing
        if (q.includes("تكييف") || q.includes("mep") || q.includes("كهرباء") || q.includes("سباكة") || q.includes("حريق") || q.includes("hvac") || q.includes("cooling") || q.includes("fire")) {
            if (isEn) {
                return `
                    <p class="mb-2">We provide integrated MEP &amp; Central HVAC solutions including: ⚡</p>
                    <ul class="mb-2 ps-3 small">
                        <li>Central Air Conditioning &amp; Ducting (VRF / Chilled Water)</li>
                        <li>Civil Defense Certified Firefighting &amp; Alarm Systems</li>
                        <li>Advanced Plumbing, Water Pumps &amp; Drainage Infrastructure</li>
                        <li>High Voltage Electrical Distribution &amp; Substation Panels</li>
                    </ul>
                    <a href="/services" class="btn btn-sm btn-outline-warning rounded-pill fw-bold text-dark w-100">Explore MEP Services <i class="fa fa-arrow-right ms-1"></i></a>
                `;
            }
            return `
                <p class="mb-2">نوفر حلولاً كهروميكانيكية متكاملة (MEP Systems) تشمل: ⚡</p>
                <ul class="mb-2 ps-3 small">
                    <li>أنظمة التكييف المركزي والدكت (VRV / Chilled Water)</li>
                    <li>شبكات مكافحة الحريق والإنذار المبكر</li>
                    <li>مخططات السباكة والتغذية المائية المتقدمة</li>
                    <li>تجهيز اللوحات الكهروميكانيكية والمولدات</li>
                </ul>
                <a href="/services" class="btn btn-sm btn-outline-warning rounded-pill fw-bold text-dark w-100">استعراض كافة الخدمات <i class="fa fa-arrow-left ms-1"></i></a>
            `;
        }

        // Contact / WhatsApp / Phone / Engineer
        if (q.includes("تواصل") || q.includes("اتصال") || q.includes("واتساب") || q.includes("مهندس") || q.includes("contact") || q.includes("phone") || q.includes("whatsapp") || q.includes("call")) {
            if (isEn) {
                return `
                    <p class="mb-2">You can connect directly with our leading project engineer on WhatsApp: 🟢</p>
                    <a href="https://wa.me/966112345678" target="_blank" class="btn btn-sm btn-success rounded-pill fw-bold text-white w-100 mb-2"><i class="fa fa-whatsapp me-1"></i> Direct WhatsApp Chat</a>
                    <p class="mb-0 small text-muted">Or call us directly: +966 11 234 5678</p>
                `;
            }
            return `
                <p class="mb-2">يمكنك التواصل المباشر مع المهندس المختص عبر الواتساب فوراً: 🟢</p>
                <a href="https://wa.me/966112345678" target="_blank" class="btn btn-sm btn-success rounded-pill fw-bold text-white w-100 mb-2"><i class="fa fa-whatsapp me-1"></i> محادثة واتساب مباشرة</a>
                <p class="mb-0 small text-muted">أو عبر الهاتف: 966112345678+</p>
            `;
        }

        // Projects / Portfolio / Completed Works
        if (q.includes("مشروع") || q.includes("معرض") || q.includes("أعمال") || q.includes("projects") || q.includes("portfolio") || q.includes("work")) {
            if (isEn) {
                return `
                    <p class="mb-2">Wasm General Contracting has successfully delivered over 150+ major commercial, residential, and infrastructure landmarks in Saudi Arabia! 🏢</p>
                    <a href="/projects" class="btn btn-sm btn-dark rounded-pill fw-bold text-white w-100">Browse Projects Portfolio <i class="fa fa-arrow-right ms-1"></i></a>
                `;
            }
            return `
                <p class="mb-2">نفذت شركة وسم أكثر من 150+ مشروعاً هندسياً وإدارياً وسكنياً وتجارياً بالمملكة! 🏢</p>
                <a href="/projects" class="btn btn-sm btn-dark rounded-pill fw-bold text-white w-100">تصفح معرض المشاريع المنفذة <i class="fa fa-arrow-left ms-1"></i></a>
            `;
        }

        // Default response
        if (isEn) {
            return `
                <p class="mb-2">Thank you for reaching out to Wasm AI Engineering Assistant! 🏗️</p>
                <p class="mb-2">We stand ready to execute your structural building, MEP systems, and luxury architectural fitouts with uncompromised precision.</p>
                <div class="d-flex gap-2">
                    <a href="/quote" class="btn btn-sm btn-warning rounded-pill fw-bold text-dark w-50">Request Quote</a>
                    <a href="https://wa.me/966112345678" target="_blank" class="btn btn-sm btn-success rounded-pill fw-bold text-white w-50">WhatsApp Us</a>
                </div>
            `;
        }
        return `
            <p class="mb-2">شكراً لتواصلك مع مساعد شركة وسم الهيكلي! 🏗️</p>
            <p class="mb-2">نحن متأهبون لتنفيذ مشاريع المباني الهيكلية، التشطيبات الفاخرة، والحلول الكهروميكانيكية (MEP) بأعلى درجات الدقة.</p>
            <div class="d-flex gap-2">
                <a href="/quote" class="btn btn-sm btn-warning rounded-pill fw-bold text-dark w-50">طلب عرض سعر</a>
                <a href="https://wa.me/966112345678" target="_blank" class="btn btn-sm btn-success rounded-pill fw-bold text-white w-50">واتساب مباشر</a>
            </div>
        `;
    }
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initWasmAiBot);
} else {
    initWasmAiBot();
}
