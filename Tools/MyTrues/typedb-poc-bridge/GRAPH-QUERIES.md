# MyTrues Memory Primitive v0 — Graph Explorer queries

## 1. Entire canonical memory

```typeql
match
  $o isa occurrence, has atom-id $occurrence-id;
  $b isa binding, links (occurrence: $o, key: $k, value: $v);
  $k has atom-id $key-id;
  $v has atom-id $value-id;
select $o, $b, $k, $v, $occurrence-id, $key-id, $value-id;
```

## 2. Cognitive path: npm failure -> influence -> pnpm decision

```typeql
match
  $source isa occurrence, has atom-id "occ:npm-failure-001";
  $rel isa occurrence, has atom-id "occ:influence-001";
  $decision isa occurrence, has atom-id "occ:decision-pnpm-001";

  $bs isa binding, links (occurrence: $rel, key: $ks, value: $source);
  $ks has atom-id "key:source";

  $bt isa binding, links (occurrence: $rel, key: $kt, value: $decision);
  $kt has atom-id "key:target";

select $source, $rel, $decision, $bs, $bt, $ks, $kt;
```

## 3. Original occurrence and later correction

```typeql
match
  $original isa occurrence, has atom-id "occ:variable-alias-001";
  $correction isa occurrence, has atom-id "occ:correction-001";
  $b isa binding, links (occurrence: $correction, key: $k, value: $original);
  $k has atom-id "key:corrects";
select $original, $correction, $b, $k;
```

This deliberately displays the correction beside the original occurrence instead
of rewriting the original.
