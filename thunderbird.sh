#!/bin/bash

VERSION="##VERSION##"
BASEDIR="/usr/share/thunderbird-stub"
SFILE="${BASEDIR}/thunderbird-${VERSION}.tar.zst"
LFILE="${HOME}/thunderbird/thunderbird"
FDIR="${HOME}/thunderbird"

if [[ -x "${LFILE}" ]] ; then
    exec "${LFILE}" "$@"
    exit 0
fi

if [[ -d "${FDIR}" ]]; then
    echo "Exiting as ${FDIR} exists."
    exit 1
fi

if [[ -x /usr/bin/notify-send ]]; then
    /usr/bin/notify-send -i thunderbird "Preparing Thunderbird" "Thunderbird will launch shortly, please wait for it to be prepared for the first use."
fi

cd "${HOME}"
tar xf "${SFILE}"

exec "${LFILE}" "$@"
