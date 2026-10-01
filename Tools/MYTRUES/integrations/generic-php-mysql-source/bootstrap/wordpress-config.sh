#!/bin/sh
set -eu

APP_ROOT="${APP_ROOT:-/opt/app-root/src}"
DB_HOST="${APP_DB_HOST:-127.0.0.1}"
DB_NAME="${APP_DB_NAME:-app}"
DB_USER="${APP_DB_USER:-app}"
DB_PASSWORD="${APP_DB_PASSWORD:-app-pass}"

rand_key() {
  A="$(cat /proc/sys/kernel/random/uuid | tr -d '-')"
  B="$(cat /proc/sys/kernel/random/uuid | tr -d '-')"
  printf '%s%s' "$A" "$B"
}

AUTH_KEY="$(rand_key)"
SECURE_AUTH_KEY="$(rand_key)"
LOGGED_IN_KEY="$(rand_key)"
NONCE_KEY="$(rand_key)"
AUTH_SALT="$(rand_key)"
SECURE_AUTH_SALT="$(rand_key)"
LOGGED_IN_SALT="$(rand_key)"
NONCE_SALT="$(rand_key)"

cat >"$APP_ROOT/wp-config.php" <<PHP
<?php
define('DB_NAME', '$DB_NAME');
define('DB_USER', '$DB_USER');
define('DB_PASSWORD', '$DB_PASSWORD');
define('DB_HOST', '$DB_HOST');
define('DB_CHARSET', 'utf8mb4');
define('DB_COLLATE', '');

define('AUTH_KEY',         '$AUTH_KEY');
define('SECURE_AUTH_KEY',  '$SECURE_AUTH_KEY');
define('LOGGED_IN_KEY',    '$LOGGED_IN_KEY');
define('NONCE_KEY',        '$NONCE_KEY');
define('AUTH_SALT',        '$AUTH_SALT');
define('SECURE_AUTH_SALT', '$SECURE_AUTH_SALT');
define('LOGGED_IN_SALT',   '$LOGGED_IN_SALT');
define('NONCE_SALT',       '$NONCE_SALT');

$table_prefix = 'wp_';

define('WP_DEBUG', false);
define('DISALLOW_FILE_EDIT', true);
define('FS_METHOD', 'direct');

if (!defined('ABSPATH')) {
    define('ABSPATH', __DIR__ . '/');
}

require_once ABSPATH . 'wp-settings.php';
PHP

chmod 0640 "$APP_ROOT/wp-config.php"
