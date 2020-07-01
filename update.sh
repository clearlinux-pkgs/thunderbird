#!/bin/bash

set -e
set -o pipefail

git pull
VERSION=$(curl -sSf http://ftp.mozilla.org/pub/thunderbird/releases/ | grep href | cut -f3 -d">" | cut -f1 -d"/" | grep -Ex '[0-9.]+' | sort -t . -k 1,1n -k 2,2n -k 3,3n -k 4,4n | tail -1)

if [[ -z "${VERSION}" ]]; then
    echo "Please pass the new version first."
    exit 1
fi

sed thunderbird.spec.in -e "s/\#\#VERSION\#\#/${VERSION}/g" > thunderbird.spec
make generateupstream || exit 1

make bumpnogit
git add thunderbird.spec Makefile release upstream
git commit -s -m "Update to ${VERSION}"
make koji
