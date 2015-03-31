{
	'includes':
	[
		'../common.gypi',
	],
	
	'targets':
	[
		{
			'target_name': 'libopenssl',
			'type': 'none',

			'link_settings':
			{
				'conditions':
				[
					[
						'OS == "mac"',
						{
							'libraries':
							[
								'lib/mac/libcustomcrypto.a',
								'lib/mac/libcustomssl.a',
							],
						},
					],
					[
						'OS == "linux"',
						{
							'variables':
							{
								'prebuilt_libs': 'prebuilt/lib/linux-i386',
							},
							
							'ldflags':
							[
								'-L<(prebuilt_libs)',
								'-Wl,-whole-archive',
								'-lcustomcrypto',
								'-lcustomssl',
								'-Wl,-no-whole-archive',
							],
						},
					],
				],
			},
		},
	],
}
