from frappe import _

def get_data():
	return {
		# 'heatmap': True,
		'heatmap_message': _('This is based on the Time Sheets created against this project'),
		'fieldname': 'trademark_project',
		'transactions': [
			{
				'label': _('Trademark'),
				'items': ['Task']
			},
			{
				'label': _('Sales'),
				'items': ['Sales Order', 'Delivery Note', 'Sales Invoice']
			},
		]
	}
