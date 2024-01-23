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
	},
    button_2:function(frm){
		frm.call({
			method:"button2Clicked",
			callback:function(r){
				console.log(r.message)
			},
		})
	},
    button_3:function(frm){
		frm.call({
			method:"button3Clicked",
			args:{
				doc: frm.doc
			},
			callback:function(r){
				console.log(r.message)
			},
		})
	},
    button_4:function(frm){
		frm.call({
			method:"button4Clicked",
			callback:function(r){
				console.log(r.message)
			},
		})
	}
});