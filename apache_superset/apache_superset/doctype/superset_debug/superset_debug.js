// // Copyright (c) 2023, Richard and contributors
// // For license information, please see license.txt

frappe.ui.form.on('Superset Debug', {
	button_1:function(frm){
		frm.call({
			method:"button1Clicked",
			args:{
				doc: frm.doc
			},
			callback:function(r){
				console.log(r.message)
			},
		})
	}
});