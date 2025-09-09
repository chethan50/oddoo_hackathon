odoo.define('legal_case_management.custom_js', function (require) {
    'use strict';
    var FormController = require('web.FormController');

    FormController.include({
        _onSave: function () {
            this._super.apply(this, arguments);
            alert("✅ Record saved successfully!");
        },
    });
});
