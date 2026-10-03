# Generic PHP + MySQL source URL integration

This bundle intentionally does not know what WordPress is.

It accepts:

- a public source archive URL;
- an optional bootstrap script URL;
- a source archive strip depth;
- a MySQL dependency;
- an Azure target.

For the current experiment:

- source archive: official WordPress distribution;
- bootstrap script: application-owned script that writes `wp-config.php`;
- runtime: generic PHP 8.3;
- database: generic MySQL 8.4.

The same bundle could receive another PHP application archive without changing the
deployment model.
