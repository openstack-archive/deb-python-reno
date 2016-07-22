# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from __future__ import print_function

from reno import formatter
from reno import loader
from reno import utils


def report_cmd(args, conf):
    "Generates a release notes report"
    reporoot = conf.reporoot
    notesdir = utils.get_notes_dir(conf)
    collapse = conf.collapse_pre_releases
    ldr = loader.Loader(
        reporoot=reporoot,
        notesdir=notesdir,
        branch=conf.branch,
        collapse_pre_releases=collapse,
        earliest_version=conf.earliest_version,
        conf=conf,
    )
    if args.version:
        versions = args.version
    else:
        versions = ldr.versions
    text = formatter.format_report(
        ldr,
        versions,
        title='Release Notes',
    )
    if args.output:
        with open(args.output, 'w') as f:
            f.write(text)
    else:
        print(text)
    return
