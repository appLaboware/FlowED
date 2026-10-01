#!/bin/sh
set -eu
case "${1:?}" in
  install)
    printf 'v1.0.0:%s\n' "${CHILD_VALUE:-missing}" > /cnab/app/child-result.txt
    echo "CHILD_INSTALL version=v1.0.0 value=${CHILD_VALUE:-missing}"
    ;;
  uninstall)
    echo "CHILD_UNINSTALL version=v1.0.0"
    ;;
esac
