#!/bin/sh
# Usage: generate-tarball.sh <version>
set -e
rm -rf GPars-release-$1 gpars-$1 release-$1.tar.gz gpars-$1.tar.bz2
wget http://github.com/GPars/GPars/archive/release-$1.tar.gz
tar xf release-$1.tar.gz
mv GPars-release-$1 gpars-$1
rm -rf gpars-$1/{artwork/,docs/,java-demo/,grails-doc/,gradle/wrapper/,lib/,src/main/groovy/groovyx/gpars/extra166y/}
tar cjf gpars-$1.tar.bz2 gpars-$1 
