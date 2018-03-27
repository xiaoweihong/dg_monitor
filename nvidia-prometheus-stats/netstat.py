#!/usr/bin/python

import argparse
import logging
import time
import platform

from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
from prometheus_client import start_http_server, core

log = logging.getLogger('netstat')

def _create_parser():
    parser = argparse.ArgumentParser(description='nVidia GPU Prometheus '
                                                 'Metrics Exporter')
    parser.add_argument('--verbose',
                        help='Turn on verbose logging',
                        action='store_true')

    parser.add_argument('-u', '--update-period',
                        help='Period between calls to update metrics, '
                             'in seconds. Defaults to 30.',
                        default=30)

    parser.add_argument('-g', '--gateway',
                        help='If defined, gateway to push metrics to. Should '
                             'be in the form of <host>:<port>.',
                        default=None)

    parser.add_argument('-p', '--port',
                        help='If non-zero, port to run the http server',
                        type=int,
                        default=0)

    return parser


def main():
    parser = _create_parser()
    args = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)
   
    registry = core.REGISTRY

    total_fb_memory = Gauge('gpu_total_fb_memory_mb',
                            'Total installed frame buffer memory (in '
                            'megabytes)',
                            ['device'],
                            registry=registry)
    free_fb_memory = Gauge('gpu_free_fb_memory_mb',
                           'Unallocated frame buffer memory (in '
                           'megabytes)',
                           ['device'],
                           registry=registry)
    used_fb_memory = Gauge('gpu_used_fb_memory_mb',
                           'Allocated frame buffer memory (in megabytes).'
                           ' Note that the diver/GPU will always set '
                           'a small amount of memory fore bookkeeping.',
                           ['device'],
                           registry=registry)
    gpu_utilization = Gauge('gpu_utilization_pct',
                            'Percent of time over the past sample period '
                            'during which one or more kernels was '
                            'executing on the GPU.',
                            ['device'],
                            registry=registry)
    memory_utilization = Gauge('gpu_mem_utilization_pct',
                               'Percent of time over the past sample '
                               'period during which global (device) memory '
                               'was being read or written',
                               ['device'],
                               registry=registry)

    iteration = 0

    try:

        if args.port:
            log.debug('Starting http server on port %d', args.port)
            start_http_server(args.port)
            log.info('HTTP server started on port %d', args.port)

        while True:

            iteration += 1
            log.debug('Current iteration = %d', iteration)

            if args.gateway:
                log.debug('Pushing metrics to gateway at %s...', args.gateway)
                hostname = platform.node()
                push_to_gateway(args.gateway, job=hostname, registry=core.REGISTRY)
                log.debug('Push complete.')
                
            time.sleep(args.update_period)
        

    except Exception as e:
        log.error('Exception thrown - %s', e, exc_info=True)
    finally:
	exit
if __name__ == '__main__':
    main()
