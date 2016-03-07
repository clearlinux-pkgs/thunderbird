#!/bin/bash

VERSION="$1"

if [[ -z "${VERSION}" ]]; then
    echo "Please pass the new version first."
    exit 1
fi

sed thunderbird.spec.in -e "s/\#\#VERSION\#\#/${VERSION}/g" > thunderbird.spec
make generateupstream || exit 1

git add thunderbird.spec Makefile release upstream
git commit -s -m "Update to ${VERSION}"
make bump
