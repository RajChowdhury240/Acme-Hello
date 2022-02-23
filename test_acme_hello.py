import os
import logging

import synapse.common as s_common
import synapse.tests.utils as s_test
import synapse.tools.genpkg as s_genpkg

logger = logging.getLogger(__name__)

dirname = os.path.dirname(__file__)
pkgproto = s_common.genpath(dirname, 'acme-hello.yaml')

# run the test with something like: python -m pytest test_acme_hello.py

class AcmeHelloTest(s_test.SynTest):

    async def test_acme_hello(self):

        async with self.getTestCore() as core:

            await s_genpkg.main((pkgproto, '--push', f'cell://{core.dirn}'))
            # we now have a cortex with our package loaded!

            # some test APIs to simplify async generators and such...
            msgs = await core.stormlist('acme.hello.print --show-prefix --prefix VISI "hello world!"')
            self.stormIsInPrint('VISI hello world!', msgs)

            nodes = await core.nodes('[ inet:email=visi@vertex.link ] | acme.hello.autotag')
            self.len(1, nodes)
            self.true(nodes[0].tags.get('acme.hello') is not None)

            # check that the meta source node got created and linked...
            nodes = await core.nodes('meta:source:name="ACME Hello World" -(seen)> *')
            self.len(1, nodes)
            self.eq(nodes[0].ndef, ('inet:email', 'visi@vertex.link'))

            # check that the description is in the auto generated `--help` output
            msgs = await core.stormlist('acme.hello.print --help')
            self.stormIsInPrint('Print some text', msgs)
