#
# CSCS ReFrame settings
#


class ReframeSettings:
    reframe_module = 'reframe'
    job_poll_intervals = [1, 2, 3]
    job_submit_timeout = 60
    checks_path = ['checks/']
    checks_path_recurse = True
    site_configuration = {
        'systems': {
            'daint': {
                'descr': 'Piz Daint',
                'hostnames': ['daint'],
                'modules_system': 'tmod',
                'resourcesdir': '/apps/common/regression/resources',
                'partitions': {
                    'login': {
                        'scheduler': 'local',
                        'modules': [],
                        'access':  [],
                        'environs': ['PrgEnv-cray', 'PrgEnv-gnu',
                                     'PrgEnv-intel', 'PrgEnv-pgi'],
                        'descr': 'Login nodes',
                        'max_jobs': 4
                    },

                    'gpu': {
                        'scheduler': 'nativeslurm',
                        'modules': ['daint-gpu'],
                        'access':  ['--constraint=gpu'],
                        'environs': ['PrgEnv-cray', 'PrgEnv-gnu',
                                     'PrgEnv-intel', 'PrgEnv-pgi'],
                        'descr': 'Hybrid nodes (Haswell/P100)',
                        'max_jobs': 100,
                        'resources': {
                            'switches': ['--switches={num_switches}']
                        }
                    },

                    'mc': {
                        'scheduler': 'nativeslurm',
                        'modules': ['daint-mc'],
                        'access':  ['--constraint=mc'],
                        'environs': ['PrgEnv-cray', 'PrgEnv-gnu',
                                     'PrgEnv-intel', 'PrgEnv-pgi'],
                        'descr': 'Multicore nodes (Broadwell)',
                        'max_jobs': 100,
                        'resources': {
                            'switches': ['--switches={num_switches}']
                        }
                    }
                }
            },

            'dom': {
                'descr': 'Dom TDS',
                'hostnames': ['dom'],
                'modules_system': 'tmod',
                'resourcesdir': '/apps/common/regression/resources',
                'partitions': {
                    'login': {
                        'scheduler': 'local',
                        'modules': [],
                        'access':  [],
                        'environs': ['PrgEnv-cray', 'PrgEnv-gnu',
                                     'PrgEnv-intel', 'PrgEnv-pgi'],
                        'descr': 'Login nodes',
                        'max_jobs': 4
                    },

                    'gpu': {
                        'scheduler': 'nativeslurm',
                        'modules': ['daint-gpu'],
                        'access':  ['--constraint=gpu'],
                        'environs': ['PrgEnv-cray', 'PrgEnv-gnu',
                                     'PrgEnv-intel', 'PrgEnv-pgi'],
                        'descr': 'Hybrid nodes (Haswell/P100)',
                        'max_jobs': 100,
                        'resources': {
                            'switches': ['--switches={num_switches}']
                        }
                    },

                    'mc': {
                        'scheduler': 'nativeslurm',
                        'modules': ['daint-mc'],
                        'access':  ['--constraint=mc'],
                        'environs': ['PrgEnv-cray', 'PrgEnv-gnu',
                                     'PrgEnv-intel', 'PrgEnv-pgi'],
                        'descr': 'Multicore nodes (Broadwell)',
                        'max_jobs': 100,
                        'resources': {
                            'switches': ['--switches={num_switches}']
                        }
                    },
                }
            },

            'kesch': {
                'descr': 'Kesch MCH',
                'hostnames': ['keschln-\d+'],
                'modules_system': 'tmod',
                'resourcesdir': '/apps/common/regression/resources',
                'partitions': {
                    'login': {
                        'scheduler': 'local',
                        'environs': ['PrgEnv-gnu', 'PrgEnv-cray',
                                     'PrgEnv-pgi', 'PrgEnv-gnu-gdr'],
                        'descr': 'Kesch login nodes',
                    },
                    'pn': {
                        'scheduler': 'nativeslurm',
                        'access': ['--partition=pn-regression'],
                        'environs': ['PrgEnv-gnu', 'PrgEnv-cray',
                                     'PrgEnv-pgi', 'PrgEnv-gnu-gdr'],
                        'descr': 'Kesch post-processing nodes'
                    },

                    'cn': {
                        'scheduler': 'nativeslurm',
                        'access': ['--partition=cn-regression'],
                        'environs': ['PrgEnv-gnu', 'PrgEnv-cray',
                                     'PrgEnv-pgi', 'PrgEnv-gnu-gdr'],
                        'descr': 'Kesch compute nodes',
                        'resources': {
                            '_rfm_gpu': ['--gres=gpu:{num_gpus_per_node}']
                        }
                    }
                }
            },

            'leone': {
                'descr': 'Leone',
                'hostnames': ['leone'],
                'modules_system': 'tmod',
                'resourcesdir': '/apps/common/regression/resources',
                'partitions': {
                    'login': {
                        'scheduler': 'local',
                        'environs': ['PrgEnv-gnu'],
                        'descr': 'Leone login nodes',
                        'max_jobs': 1
                    },

                    'normal': {
                        'scheduler': 'nativeslurm',
                        'environs': ['PrgEnv-gnu'],
                        'descr': ('Leone compute nodes - '
                                  'default partition'),
                        'max_jobs': 10
                    },
                }
            },

            'monch': {
                'descr': 'Monch PASC',
                'hostnames': ['monch'],
                'modules_system': 'tmod',
                'resourcesdir': '/apps/common/regression/resources',
                'partitions': {
                    'login': {
                        'scheduler': 'local',
                        'environs': ['PrgEnv-gnu'],
                        'descr': 'Monch login nodes',
                        'max_jobs': 1
                    },

                    'compute': {
                        'scheduler': 'slurm+mpirun',
                        'access': ['--partition=compute'],
                        'environs': ['PrgEnv-gnu'],
                        'descr': 'Monch compute nodes',
                        'max_jobs': 10
                    }
                }
            },

            # Generic system used for cli unit tests
            'generic': {
                'descr': 'Generic example system',
                'partitions': {
                    'login': {
                        'scheduler': 'local',
                        'modules': [],
                        'access': [],
                        'environs': ['builtin-gcc'],
                        'descr': 'Login nodes'
                    }
                }
            }
        },

        'environments': {
            'kesch': {
                'PrgEnv-gnu': {
                    'type': 'ProgEnvironment',
                    'modules': ['PrgEnv-gnu'],
                    'cc': 'mpicc',
                    'cxx': 'mpicxx',
                    'ftn': 'mpif90',
                },
                'PrgEnv-pgi': {
                    'type': 'ProgEnvironment',
                    'modules': ['/apps/common/regression/prgenv_pgi_17.10_aj'],
                    'cc': 'mpicc',
                    'cxx': 'mpicxx',
                    'ftn': 'mpif90',
                },
                'PrgEnv-gnu-gdr': {
                    'type': 'ProgEnvironment',
                    'modules': ['gmvapich2/17.02_cuda_8.0_gdr'],
                    'cc': 'mpicc',
                    'cxx': 'mpic++',
                    'ftn': 'mpif90',
                },
            },
            'leone': {
                'PrgEnv-gnu': {
                    'type': 'ProgEnvironment',
                    'modules': ['PrgEnv-gnu/leone-foss-2016b'],
                    'cc':  'mpicc',
                    'cxx': 'mpicxx',
                    'ftn': 'mpif90',
                },
            },
            'monch': {
                'PrgEnv-gnu': {
                    'type': 'ProgEnvironment',
                    'modules': ['PrgEnv-gnu'],
                    'cc':  'mpicc',
                    'cxx': 'mpicxx',
                    'ftn': 'mpif90',
                }
            },
            '*': {
                'PrgEnv-cray': {
                    'type': 'ProgEnvironment',
                    'modules': ['PrgEnv-cray'],
                },

                'PrgEnv-gnu': {
                    'type': 'ProgEnvironment',
                    'modules': ['PrgEnv-gnu'],
                },

                'PrgEnv-intel': {
                    'type': 'ProgEnvironment',
                    'modules': ['PrgEnv-intel'],
                },

                'PrgEnv-pgi': {
                    'type': 'ProgEnvironment',
                    'modules': ['PrgEnv-pgi'],
                },

                'builtin': {
                    'type': 'ProgEnvironment',
                    'cc':  'cc',
                    'cxx': '',
                    'ftn': '',
                },

                'builtin-gcc': {
                    'type': 'ProgEnvironment',
                    'cc':  'gcc',
                    'cxx': 'g++',
                    'ftn': 'gfortran',
                }
            }
        },

        'modes': {
            '*': {
                'maintenance': [
                    '--exec-policy=async',
                    '--strict',
                    '--output=$APPS/UES/$USER/regression/maintenance',
                    '--perflogdir=$APPS/UES/$USER/regression/maintenance/logs',
                    '--stage=$SCRATCH/regression/maintenance/stage',
                    '--reservation=maintenance',
                    '--save-log-files',
                    '--tag=maintenance',
                    '--timestamp=%F_%H-%M-%S'
                ],
                'production': [
                    '--exec-policy=async',
                    '--strict',
                    '--output=$APPS/UES/$USER/regression/production',
                    '--perflogdir=$APPS/UES/$USER/regression/production/logs',
                    '--stage=$SCRATCH/regression/production/stage',
                    '--save-log-files',
                    '--tag=production',
                    '--timestamp=%F_%H-%M-%S'
                ]
            }
        }
    }

    logging_config = {
        'level': 'DEBUG',
        'handlers': [
            {
                'type': 'file',
                'name': 'reframe.log',
                'level': 'DEBUG',
                'format': '[%(asctime)s] %(levelname)s: '
                          '%(check_info)s: %(message)s',
                'append': False,
            },

            # Output handling
            {
                'type': 'stream',
                'name': 'stdout',
                'level': 'INFO',
                'format': '%(message)s'
            },
            {
                'type': 'file',
                'name': 'reframe.out',
                'level': 'INFO',
                'format': '%(message)s',
                'append': False,
            }
        ]
    }

    perf_logging_config = {
        'level': 'DEBUG',
        'handlers': [
            {
                'type': 'graylog',
                'host': 'your-server-here',
                'port': 12345,
                'level': 'INFO',
                'format': (
                    '%(asctime)s|reframe %(version)s|'
                    '%(check_info)s|jobid=%(check_jobid)s|'
                    '%(check_perf_var)s=%(check_perf_value)s|'
                    'ref=%(check_perf_ref)s '
                    '(l=%(check_perf_lower_thres)s, '
                    'u=%(check_perf_upper_thres)s)'
                ),
                'extras': {
                    'facility': 'reframe',
                    'data-version': '1.0',
                }
            },
            {
                'type': 'filelog',
                'prefix': '%(check_system)s/%(check_partition)s',
                'level': 'INFO',
                'format': (
                    '%(asctime)s|reframe %(version)s|'
                    '%(check_info)s|jobid=%(check_jobid)s|'
                    '%(check_perf_var)s=%(check_perf_value)s|'
                    'ref=%(check_perf_ref)s '
                    '(l=%(check_perf_lower_thres)s, '
                    'u=%(check_perf_upper_thres)s)'
                ),
                'append': True
            }
        ]
    }


settings = ReframeSettings()
