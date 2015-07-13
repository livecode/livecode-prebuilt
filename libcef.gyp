{
	'includes':
	[
		'../common.gypi',
	],
	
	'targets':
	[
		{
			'target_name': 'libcef',
			'type': 'none',
			
			'direct_dependent_settings':
			{
				'defines':
				[
					'USING_CEF_SHARED=1',
				],
			},
		},
	],
}
