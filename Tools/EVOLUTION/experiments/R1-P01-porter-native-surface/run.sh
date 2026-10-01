#!/bin/sh
set -eu

ACTION="${1:?action required}"

case "$ACTION" in
  install)
    test -n "${LAB_TOKEN:-}"
    printf 'install:%s\n' "${GREETING:-missing}" > /cnab/app/result.txt
    printf 'sensitive-output-present\n' > /cnab/app/sensitive.txt
    echo "credential_injected=yes"
    echo "parameter_value=${GREETING:-missing}"
    ;;

  upgrade)
    test -n "${LAB_TOKEN:-}"
    printf 'upgrade:%s\n' "${GREETING:-missing}" > /cnab/app/result.txt
    printf 'sensitive-output-upgraded\n' > /cnab/app/sensitive.txt
    echo "credential_injected=yes"
    echo "parameter_value=${GREETING:-missing}"
    ;;

  status)
    echo "STATUS_OK greeting=${GREETING:-missing}"
    ;;

  uninstall)
    echo "UNINSTALL_OK"
    ;;

  *)
    echo "unknown action: $ACTION" >&2
    exit 2
    ;;
esac
