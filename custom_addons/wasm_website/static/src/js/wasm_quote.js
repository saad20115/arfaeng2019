/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.WasmQuoteWidget = publicWidget.Widget.extend({
    selector: '.wasm-quote-form-container',
    events: {
        'change input[type="file"]': '_onFileChange',
        'submit form': '_onSubmitForm',
    },

    _onFileChange: function (ev) {
        const input = ev.currentTarget;
        const fileList = input.files;
        const infoBox = this.$('.wasm-file-list-info');
        const isEn = (document.documentElement.lang && document.documentElement.lang.startsWith("en")) || window.location.pathname.startsWith("/en");

        if (infoBox.length && fileList.length > 0) {
            let names = [];
            for (let i = 0; i < fileList.length; i++) {
                const sizeMB = (fileList[i].size / 1024 / 1024).toFixed(2);
                names.push(
                    '<i class="fa fa-file-pdf-o me-1 text-danger"></i> '
                    + fileList[i].name + ' (' + sizeMB + ' MB)'
                );
            }
            const headerText = isEn
                ? `Selected files for upload (${fileList.length}):`
                : `الملفات المحددة للرفع (${fileList.length}):`;

            infoBox.html(
                '<div class="alert alert-info mt-2 mb-0">'
                + '<strong class="d-block mb-1">' + headerText + '</strong>'
                + names.join('<br/>')
                + '</div>'
            );
        }
    },

    _onSubmitForm: function (ev) {
        const btn = this.$('button[type="submit"]');
        const isEn = (document.documentElement.lang && document.documentElement.lang.startsWith("en")) || window.location.pathname.startsWith("/en");
        if (btn.length) {
            const submittingText = isEn
                ? '<i class="fa fa-circle-o-notch fa-spin me-2"></i> Submitting RFQ &amp; saving attachments...'
                : '<i class="fa fa-circle-o-notch fa-spin me-2"></i> جاري إرسال الطلب وحفظ المرفقات...';
            btn.prop('disabled', true).html(submittingText);
        }
    },
});
