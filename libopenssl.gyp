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
							# Gyp doesn't seem to handle non-absolute paths here properly...
							'library_dirs':
							[
								'<(src_top_dir_abs)/prebuilt/lib/linux/<(target_arch)',
							],
							
							'libraries':
							[
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
